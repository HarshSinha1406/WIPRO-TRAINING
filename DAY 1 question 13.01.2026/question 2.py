data = [1, 2, 3, 4, 5, 6, 2, 4]

squares_list = [x**2 for x in data]

even_set = {x for x in data if x % 2 == 0}

cube_dict = {x: x**3 for x in data}

print("Squares List:", squares_list)
print("Unique Even Set:", even_set)
print("Cube Dictionary:", cube_dict)