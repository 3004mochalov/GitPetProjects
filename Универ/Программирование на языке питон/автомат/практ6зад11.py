from PIL import Image

def main(w, h, zoom, cX, cY, moveX, moveY, maxIter):
    bitmap = Image.new("RGB", (w, h), "white") #создаём изображение
    pix = bitmap.load() #выделяем оперативную память
    for x in range(w):
        for y in range(h): #рисуем фракталы жюлия
            zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX
            zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + moveY
            i = maxIter
            while zx * zx + zy * zy < 4 and i > 1:
                zy, zx = 2.0 * zx * zy + cY, zx * zx - zy * zy + cX #применение формулы z^2 + c, где c - комплексный параметр.
                i -= 1
            pix[x, y] = (i << 21) + (i << 10) + i * 8 #преобразование byte в RGB
    bitmap.show()

main(15360, 8640, 1, -0.7, 0.27015, 0.0, 0.0, 255)