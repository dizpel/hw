arr = input("Введите элементы массива через пробел: ").split()

new_arr = []

for string in arr:
    
    if len(string) <= 3:
        
        new_arr.append(string)