import zadanie1Module
import timeit
from random import randint

a = [randint(0, 100) for i in range(15)]
print(f"Массив a = {a}")
print("Быстрая сортировка")
timer = timeit.default_timer()
zadanie1Module.quickSort(a)
endtimer = timeit.default_timer() - timer
print(f"Массив отсортировался за {endtimer} секунд {a}")
print("-----------------------------")
a = [randint(0, 100) for i in range(15)]
print(f"Массив a = {a}")
print("Сортировка расчёской")
timer = timeit.default_timer()
zadanie1Module.combSort(a)
endtimer = timeit.default_timer() - timer
print(f"Массив отсортировался за {endtimer} секунд {a}")

