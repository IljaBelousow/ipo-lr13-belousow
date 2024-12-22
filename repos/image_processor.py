from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from repos.image_handler import ImageHandler

class ImageProcessor():
    # Принимать изображение, переданное из ImageHandler.
    def __init__(self, image):
        self.img = image

    # Содержать методы для применения
     # различных фильтров, добавления текста и других эффектов.
    
    # Применить фильтр повышения резкости (SHARPEN).
    def image_sharpness(self):
        sharpen_image = self.img.filter(ImageFilter.SHARPEN)
        print("Резкость добавлена")
        return sharpen_image
        

    # Добавить рамку вокруг изображения с шириной 15 пикселей.
    def image_border(self, size):
        bord_image = ImageOps.expand(self.img, border=size)
        print("Рамка добавлена")
        return bord_image
       
