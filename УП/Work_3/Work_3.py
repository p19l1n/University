import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('nature.bmp')

# Преобразование изображения в список для ручной обработки
image_list = image.tolist()

# 1. Увеличение ширины в 2 раза
new_width = []
for row in image_list:
    new_row = []
    for pixel in row:
        new_row.append(pixel)
        new_row.append(pixel)
    new_width.append(new_row)

# 2. Уменьшение высоты в 2 раза (берем каждую вторую строку)
reduced_height = new_width[::2]

# Определение размеров измененного изображения
h = len(reduced_height)
w = len(reduced_height[0]) if h > 0 else 0

# Вычисление 5% площади изображения
total_pixels = h * w
region_area = int(total_pixels * 0.05)

# Расчет высоты области для инверсии (5% от высоты изображения)
region_height = max(1, int(round(h * 0.05)))
start_row = h - region_height

# Инверсия всех пикселей в нижней области
for i in range(start_row, h):
    for j in range(w):
        pixel = reduced_height[i][j]
        inverted = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2]]
        reduced_height[i][j] = inverted


# Преобразование обратно в numpy массив
result_image = np.array(reduced_height, dtype=np.uint8)

# Отображение результата
cv2.imshow('Processed Image', result_image)
cv2.waitKey(0)

# Сохранение в формате BMP
output_filename = 'result.bmp'
cv2.imwrite(output_filename, result_image)
print(f"Изображение сохранено как {output_filename}")

cv2.destroyAllWindows()