def minimum_total(triangle):
    # Начинаем с предпоследней строки и идём вверх
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Обновляем текущий элемент: его значение + минимум из двух соседей снизу
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

# Примеры из условия
triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimum_total(triangle1))  # 11

triangle2 = [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]]
print(minimum_total(triangle2))  # 0