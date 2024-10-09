import math as n
def f(x):
    return m.log10(abs(x + m.sqrt(x)))
a = float(input("a: "))
b = float(input("b: "))
h = float(input("h: "))
values = []
x = a
while x <= b:
    try:
        result = f(x)
        values.append(result)
        print(f"f({x}) = {result}")
    except ValueError:
        print(f"f({x})")
    x += h
    print(values)
if values:
    max_value = max(values)
    min_value = min(values)
    max_index = values.index(max_value)
    min_index = values.index(min_value)
    print(f"\nНайбільше значення: {max_value} на індексі {max_index}")
    print(f"Найменше значення: {min_value} на індексі {min_index}")
else:
    print("\nСписок значень порожній, немає доступних значень.")