def minimum_total(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    return triangle[0][0]

def read_triangle():
    triangle = []
    print("Введите треугольник построчно (пустая строка для завершения):")
    while True:
        line = input().strip()
        if not line:
            break
        # Преобразуем строку в список чисел
        row = list(map(int, line.split(',')))
        triangle.append(row)
    return triangle

def main():
    triangle = read_triangle()
    if not triangle:
        print("Треугольник пуст!")
        return
    
    # Сохраняем копию для вывода пути (упрощённо)
    original = [row[:] for row in triangle]
    
    result = minimum_total(triangle)
    
    print(f"\nМинимальная сумма пути: {result}")
    
    # Простой вывод пути (для демонстрации)
    print("Примерный путь (первый возможный минимум):", end=" ")
    path = []
    col = 0
    for i in range(len(original)):
        path.append(original[i][col])
        if i < len(original) - 1:
            # Выбираем следующий столбец с минимальным значением
            if original[i + 1][col] < original[i + 1][col + 1]:
                col = col
            else:
                col = col + 1
    
    print(" → ".join(map(str, path)))

if __name__ == "__main__":
    main()