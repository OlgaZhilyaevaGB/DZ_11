#f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0
import numpy as np
import matplotlib.pyplot as plt
import sympy 
x=np.arange(-10,10,1)
corny= [-12, -18, 5, 10]

def func(x):
    function=-12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
    return function

y = -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30    
#возрастание, убывание
min_func = min(func(x))
print(f'минимум:{min_func}')
my_dif = np.diff(func(x))
print(f'вершина :{max(my_dif)}')

# простороение графика

fig, ax = plt.subplots()
plt.title(f'Корни функции: {round(np.roots(corny)[0], 2)}, {round(np.roots(corny)[1], 2)}, {round(np.roots(corny)[2], 2)}')
plt.xlabel('Ось абцис (Х)')
plt.ylabel('Ось ординат (Y)')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x, y,'b', label='f=-12x^4*sin(cos(x))-18x^3+5x^2+10x-30')
ax.plot(x, y, linewidth =2.0)
fig.set(facecolor = 'g')
ax.set(facecolor = 'w')
plt.legend()
plt.grid(which='major', linewidth=1.2)
plt.show()