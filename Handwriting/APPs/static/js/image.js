function changeImage() {
        var image = document.getElementById('myImage');
        if (image.src.endsWith('my_image.jpg')) {
            image.src = '{% static "images/other_image.jpg" %}';
        } else {
            image.src = '{% static "images/my_image.jpg" %}';
        }
    }