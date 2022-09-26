import re

a = input("Введите адрес e-mail: ")

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$"

regex = re.compile(pattern)

if regex.findall(a):
    
    print("Почтовый сервер: ")
    print(a.split("@")[1])
    
else:
    print("Ошибка")
