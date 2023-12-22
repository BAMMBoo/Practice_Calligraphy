from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)

#笔画
class WSkills(models.Model):
    SkillName = models.CharField(max_length=30, unique=True)
    SkillDec = models.TextField(max_length=288)
#写字
class WordSkills(models.Model):
    SkillName = models.CharField(max_length=30, unique=True)
    SkillDec = models.TextField(max_length=288)






