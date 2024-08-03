from PIL import Image


def make_color_transparent(image_path, color_to_replace):
    # Открываем изображение
    image = Image.open(image_path)

    # Преобразуем изображение в режим RGBA, если оно ещё не в нём
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    # Получаем данные пикселей
    pixel_data = image.load()
    width, height = image.size

    # Проходимся по каждому пикселю
    for y in range(height):
        for x in range(width):
            rgba = pixel_data[x, y]

            # Проверяем, совпадает ли текущий цвет с цветом, который нужно сделать прозрачным
            if rgba[:3] == color_to_replace:
                # Устанавливаем альфа-канал пикселя в 0 (прозрачность)
                pixel_data[x, y] = (rgba[0], rgba[1], rgba[2], 0)

    # Сохраняем изменённое изображение
    image.save('SoulReborn/MainMenuSprites/output.png')


# Пример использования
make_color_transparent('SoulReborn/MainMenuSprites/Settings_PrefScroll_bar.png', (255, 255, 255))
