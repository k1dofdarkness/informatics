import re

regex = re.compile(r'(?<!:)(2[0-3]|[01]\d):[0-5]\d(:[0-5]\d)?')

text = input("Введите текст: ")

text = re.sub(regex, '(TDB)', text)

print(text)
