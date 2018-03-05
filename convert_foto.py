# Домашнее задание к лекции 2.5 «Вызов внешних программ»
# Задача №1
# Есть программа (Image Magick для Windows и Linux, либо встроенная утилиту sips для mac), которая сжимает фотографии,
# и есть папка «Source» с самими фотографиями.
# Каждую фотографию мы хотим уменьшить до 200px в ширину (высота меняется пропорционально). Нужно для каждой фотографии
# запустить программу и результат работы положить в папку «Result».
# Обратите внимание, что папки «Result» у пользователя нет и программа будет запущена несколько раз.
#
# Пример (ImageMagic):
#
# convert input.jpg -resize 200 output.jpg
#
import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "Source")
result_dir = os.path.join(current_dir, "Result")


def dir_exists_create(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def convert_filename(dirname):
    dir_exists_create(result_dir)
    for file in os.listdir(dirname):
        command_line = os.path.join(current_dir, "convert.exe") + ' ' + os.path.join(source_dir, file) + \
                       ' -resize 200 ' + os.path.join(result_dir, file)
        process = subprocess.run(command_line)
        if process.returncode == 0:
            print('Команда: ', command_line, 'выполнена успешно.  returncode=', process.returncode)
        else:
            print('Внимание команда: ', command_line, 'завершилось с ошибкой.  returncode=', process.returncode)


if __name__ == '__main__':
    convert_filename(source_dir)
    pass
