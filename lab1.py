import math as m
from tabulate import tabulate

h = 0.1
headers = ['i', 'xi', 'yi', 'f(xi,yi)', 'yi+1', 'y точне']


def euler_explicit_method(yi, f_xi_yi):
    return round(yi + h * f_xi_yi, 4)


def euler_cauchy_method(yi, f_xi_yi, xi_plus1):
    f = yi + h * f_xi_yi + m.cos(xi_plus1 / m.sqrt(7))
    return round(yi + h/2 * (f_xi_yi+f), 4)


def perfected_em(yi, f_xi_yi, xi):
    f = yi + h/2 * f_xi_yi + m.cos((xi + h/2) / m.sqrt(7))
    return round(yi + h*f, 4)


def runge_kutta_method(yi, f_xi_yi, xi):
    k0 = f_xi_yi
    k1 = (yi + h/2 * k0) + m.cos((xi + h/2) / m.sqrt(7))
    k2 = (yi + h/2 * k1) + m.cos((xi + h/2) / m.sqrt(7))
    k3 = (yi + h * k2) + m.cos((xi + h) / m.sqrt(7))
    return round(yi + h/6 * (k0 + 2*k1 + 2*k2 + k3), 4)


def main(method='Метод Ейлера'):
    print('\n' + method + ':')

    xi_column = [headers[1]]
    xi = 0.5
    while xi < 1.6:
        xi_column.append(round(xi, 1))  # round - округлення до сотих
        xi += 0.1

    i_row = [headers[0]]
    yi_row = [headers[2], 0.6]
    f_xi_yi_row = [headers[3]]
    y_i_plus1_row = [headers[4]]
    y_exact_row = [headers[5]]

    for i in range(11):
        i_row.append(i)
        f_xi_yi = yi_row[i + 1] + m.cos(xi_column[i + 1] / m.sqrt(7))
        f_xi_yi_row.append(round(f_xi_yi, 4))

        y_i_plus1 = ''  # на випадок останньої ітерації в методі Ейлера-Коші
        if method == 'Метод Ейлера':
            y_i_plus1 = euler_explicit_method(yi_row[i + 1], f_xi_yi)
        elif method == 'Метод Ейлера-Коші' and i+2 < 12:
            y_i_plus1 = euler_cauchy_method(yi_row[i + 1], f_xi_yi, xi_column[i+2])
        elif method == 'Вдосконалений метод Ейлера':
            y_i_plus1 = perfected_em(yi_row[i + 1], f_xi_yi, xi_column[i+1])
        elif method == 'Метод Рунге-Кутта четвертого порядку':
            y_i_plus1 = runge_kutta_method(yi_row[i + 1], f_xi_yi, xi_column[i+1])

        y_i_plus1_row.append(y_i_plus1)
        yi_row.append(y_i_plus1)

        y_exact = m.sqrt(7) / 8 * m.sin(xi_column[i + 1] / m.sqrt(7)) - 7 / 8 * m.cos(
            xi_column[i + 1] / m.sqrt(7)) + 0.8475 * m.exp(xi_column[i + 1])
        y_exact_row.append(round(y_exact, 4))

    yi_row.pop()
    data = [i_row, xi_column, yi_row, f_xi_yi_row, y_i_plus1_row, y_exact_row]
    print(tabulate(data, tablefmt="fancy_grid"))


if __name__ == '__main__':
    main('Метод Ейлера')
    main('Метод Ейлера-Коші')
    main('Вдосконалений метод Ейлера')
    main('Метод Рунге-Кутта четвертого порядку')
