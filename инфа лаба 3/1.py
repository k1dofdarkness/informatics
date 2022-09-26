import re

text = input("Введите текст: ")

regex = re.findall(r"\bX-\|\b|$", text)

count = len(regex)

print("Количество смайликов:", count)
