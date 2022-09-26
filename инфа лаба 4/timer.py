import laba4
import laba4dop1
import time

start_time = time.time()
for i in range(10):
    laba4.main()
print("Базовый вариант требует", time.time() - start_time, "сек.")

start_time = time.time()
for i in range(10): 
    laba4dop1.main()
print("Вариант с готовыми библиотеками требует", time.time() - start_time, "сек.")
