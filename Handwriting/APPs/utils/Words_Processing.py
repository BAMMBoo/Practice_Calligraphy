import os.path
import django
import cv2
import numpy as np
from django.conf import settings
from skimage.metrics import structural_similarity as compare_ssim

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Handwriting.settings')
django.setup()


# 定义感知哈希
def phash(img):
    # step1：调整大小32x32
    img = cv2.resize(img, (32, 32))
    img = img.astype(np.float32)

    # step2:离散余弦变换
    img = cv2.dct(img)
    img = img[0:8, 0:8]
    sum = 0.
    hash_str = ''
    # step3:计算均值
    # avg = np.sum(img) / 64.0
    for i in range(8):
        for j in range(8):
            sum += img[i, j]
    avg = sum / 64

    # step4:获得哈希
    for i in range(8):
        for j in range(8):
            if img[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# 计算汉明距离
def hmdistance(hash1, hash2):
    num = 0
    assert len(hash1) == len(hash2)
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            num += 1
    return num


def getPicture(standard1, written1):
    # 获取图片路径
    # SWord = os.path.join(settings.STATIC_ROOT, 'img', 'standard_font.jpg')
    # WWord = os.path.join(settings.STATIC_ROOT, 'img', 'cls.jpg')
    # #通过路径获取图片，standard是标准字，written是手写字
    # standard1 = cv2.imread(SWord)
    # written1 = cv2.imread(WWord)

    # 获取图片A的尺寸
    height_a, width_a, _ = standard1.shape
    # 调整图片B的尺寸为与图片A相同
    written_resized = cv2.resize(written1, (width_a, height_a))
    # 获取调整后的图片B的尺寸
    height_b, width_b, _ = written_resized.shape
    # 计算字居中的位置
    x_offset = (width_a - width_b) // 2
    y_offset = (height_a - height_b) // 2
    # 创建一个与图片A相同尺寸的空画布
    canvas = standard1.copy()
    # 将调整后的图片B复制到画布上，居中显示
    canvas[y_offset:y_offset + height_b, x_offset:x_offset + width_b] = written_resized
    return standard1, canvas


# 保存结果
# cv2.imwrite('written.jpg', canvas)

def IfSimilarity(standard, written):
    # 灰度处理
    standard1 = cv2.cvtColor(standard, cv2.COLOR_BGR2GRAY)
    written1 = cv2.cvtColor(written, cv2.COLOR_BGR2GRAY)
    # 使用中值滤波器进行降噪处理，滤波器的孔径大小为5
    median1 = cv2.medianBlur(standard1, 5)
    median2 = cv2.medianBlur(written1, 5)
    # 边缘检测函数，100和200是Canny算法的两个阈值参数。在边缘连接阶段，梯度幅值大于200被认为是强边缘，梯度幅值介于100和200之间的被认为是弱边缘。
    canny1 = cv2.Canny(median1, 100, 200)
    canny2 = cv2.Canny(median2, 100, 200)
    cv2.imwrite('standerd.jpg', canny1)
    cv2.imwrite('cls1.jpg', canny2)
    # 对图片进行分块
    canny1 = canny1[10:40, 45:115]
    canny2 = canny2[10:40, 45:115]

    cv2.imshow("canny1", canny1)
    cv2.imshow("canny2", canny2)

    # 得到感知哈希
    hash1 = phash(canny1)
    hash2 = phash(canny2)
    print(hash1)
    print(hash2)
    # 通过哈希值计算出明汉距离，距离越小，说明图片越相似
    dist = hmdistance(hash1, hash2)
    #print('距离为：', dist)

    ssim_score, _ = compare_ssim(canny1, canny2, full=True)

    #print(f"ssim_score is:{ssim_score}")
    if ssim_score <= 0.8 and dist > 20:
        return 0
    else:
        return 1




SWord = os.path.join(settings.STATIC_ROOT, 'img', 'standard_font.jpg')
WWord = os.path.join(settings.STATIC_ROOT, 'img', 'written_txt.jpg')
standard1 = cv2.imread(SWord)
written1 = cv2.imread(WWord)

#处理图片
standard, written = getPicture(standard1, written1)
result = IfSimilarity(standard, written)
if result == 0:
    print("重写重写重写重写重写重写重写重写重写重写重写重写重写重写重写重写重写重写重写重写")
else:
    template = standard[10:40, 45:115]
    match = cv2.matchTemplate(written, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match >= 0.89898)
    w = 50
    h = 30
    for p in zip(*locations[::-1]):
        x1, y1 = p[0], p[1]
        x2, y2 = x1 + w, y1 + h
        cv2.rectangle(standard, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("Write", standard)
    cv2.imwrite('yong.jpg', standard)



# cv2.imshow("Write", canny1)
# cv2.imshow("Stander", canny2)
# cv2.imwrite('output.jpg', standard1)
cv2.waitKey()
