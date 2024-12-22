from PIL import Image

class ImageHandler: 
    # Принимать путь к изображению при инициализации.
    def __init__(self, filename):
        self.filename = filename
        self.img = None


    # Содержать методы для загрузки изображения, 
     # сохранения и изменения его размера.
    def load_image(self):
        with Image.open(self.filename) as img:
            self.img = img.copy()  
            self.img.load()
            print(f"Изображение загружено: {self.img.size}")
        
    def size_image(self, w, h):    
        new_size = (w, h)
        self.img = self.img.resize(new_size, Image.LANCZOS)
        print(f"Новое размер изображения: {self.img.size}")
    
    def save_image(self, file_name):
        self.img.save(file_name)
        print(f"Изображение сохранено как {file_name}")
    
    # Реализовать метод для изменения формата изображения на JPG.
    def jpeg_image(self, new_filename):
        rgb_image = self.img.convert("RGB")
        rgb_image.save(new_filename, "JPEG")
        print(f"Изображение сохранено в формате JPG как {new_filename}")

    # Реализовать метод для поворота изображения на 45 градусов.
    def rotate_image(self, ugol):
        self.img = self.img.rotate(ugol, expand=True)
        print(f"Изображение повернуто на {ugol} градусов.")
