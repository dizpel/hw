arr = input("Введите элементы массива через пробел: ").split()

new_arr = []

for string in arr:
    
    if len(string) <= 3:
        
        new_arr.append(string)

print("Новый массив строк с длиной <= 3 символам:")
for string in new_arr:
    print(string)