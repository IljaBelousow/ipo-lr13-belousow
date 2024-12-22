from repos.image_handler import ImageHandler
from repos.image_processor import ImageProcessor
from PIL import Image

def end_see():
    print("Программа завершена. ОНА МУЧИЛАСЬ РОВНО РАЗ !!!!!!!!!")

def menu():
    print("""
        1 - Вывести изображение 
        2 - Изменить размер изображения
        3 - Изменить формат изображения на JPG
        4 - Повернуть изображение на 45 градусов
        5 - Применить фильтр повышения резкости
        6 - Добавить рамку вокруг изображения
        7 - Закрыть программу
        """)

def main():
    filename = "kartinka.rar"  
    image_handler = ImageHandler(filename)
    image_handler.load_image()
    image_processor = ImageProcessor(image_handler.img) 
    brik_close = True

    while brik_close:
        menu()
        try:
            user_input = int(input("Введите действие какое хотите выполнить: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите число от 1 до 7")
            continue
        
        if user_input == 1:
            image_handler.img.show()
        
        elif user_input == 2:
            try:
                user_input_sizeW = int(input("Введите ширину картинки: "))
                user_input_sizeH = int(input("Введите высоту картинки: "))
                image_handler.size_image(user_input_sizeW, user_input_sizeH)
                image_handler.save_image("kartinka_thumbnail.jpg")
            except ValueError:
                print("Введите нормальный размер")

        elif user_input == 3:
            image_handler.jpeg_image("kartinkaJpeg.jpg")
        
        elif user_input == 4:
            image_handler.rotate_image(45)
            image_handler.save_image("kartinka_rotated.jpg")

        elif user_input == 5:
            sharpen_image = image_processor.image_sharpness()
            sharpen_image.show() 
        
        elif user_input == 6:
            bord_image = image_processor.image_border(15)  
            bord_image.show() 
        
        elif user_input == 7:
            end_see()
            brik_close = False

if __name__ == "__main__":
    main()
