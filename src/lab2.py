import sympy as sp
import matplotlib.pyplot as plt

x_interp = [-3, -2, 1, 3]  # абсциси точок для інтерполювання
y_interp = [-4, 19, -8, 14]  # ординати точок для інтерполювання
n = 3  # тому що задано 4 точки для інтерполювання


def lagrange_polynomial(x=sp.Symbol('x')):
    L_n_x = 0
    for i in range(n + 1):
        x_interp_ex_i = []  # список, що міститиме всі абсциси точок для інтерполювання, окрім хі, що йде за циклом
        for x_interp_el in x_interp:
            x_interp_ex_i.append(x_interp_el)
        x_interp_ex_i.pop(i)  # видалення хі

        num = 1  # знаменник дробу l_i_x
        den = 1  # чисельник дробу l_i_x
        for j in range(n):
            num *= x - x_interp_ex_i[j]
            den *= x_interp[i] - x_interp_ex_i[j]
        l_i_x = num / den
        L_n_x += y_interp[i] * l_i_x
    return L_n_x


if __name__ == '__main__':
    L_n_x = lagrange_polynomial()
    print('1. Формула многочлена Лагранжа:')
    print('Ln(x) =', L_n_x)
    print('Ln(x) =', sp.expand(L_n_x))

    print('2. Обчислені значення многочлена в заданих точках:')
    x = [-1.5, 0.5, 1.5, 2]
    for i in range(len(x)):
        print(f'f({x[i]}) =', round(lagrange_polynomial(x[i]), 3))

    print('3. Графік')
    y = L_n_x
    sp.plot(y)
    plt.show()
