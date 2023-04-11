a = input("Массив А\nВведите цифры через запятую: ").split(",")
b = input("Массив B\nВведите цифры через запятую: ").split(",")

sort_dict = dict(zip(b, a))
sorted_b = sorted(b)
sorted_a = [sort_dict[value] for value in sorted_b]

print("Массив А, отсортированный по элементам массива B: ", sorted_a)
