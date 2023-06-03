from tabulate import tabulate


def cubic_function(d1, d2, d3, d4, x):
    return d1 * x**3 + d2 * x**2 + d3 * x + d4


def interval_halving_method(d1, d2, d3, d4, a, b, e):
    k = 0
    x_c = a + b / 2
    table = []
    process = True
    while process:
        L = b - a
        f_x_c = cubic_function(d1, d2, d3, d4, x_c)
        y = a + L/4
        z = b - L/4
        f_y = cubic_function(d1, d2, d3, d4, y)
        f_z = cubic_function(d1, d2, d3, d4, z)
        table.append([round(k,3), round(a,3), round(b,3), round(x_c,3), f'[{round(a,3)}; {round(b,3)}]', round(L,3)])
        if f_y < f_x_c:
            b = x_c
            x_c = y
        else:
            if f_z > f_x_c:
                a = y
                b = z
            else:
                a = x_c
                x_c = z
        if L < e:
            return table
        k += 1


def main():
    process = 1
    while process == 1:
        print('Вкажіть коефіцієнти d1,d2,d3,d4 функції f(x) = d1*x^3 + d2*x^2 + d3*x + d4')
        d = []
        try:
            for i in range(1, 5):
                d_i = float(input(f'\td{i}: '))
                d.append(d_i)
            print('Вкажіть інтервал [a,b] для х')
            a = float(input('\ta: '))
            b = float(input('\tb: '))
            if b <= a:
                print('b повинно бути більшим, ніж а')
                continue
            e = float(input('Вкажіть точність (е): '))
        except:
            print('Вводьте тільки числа')
            try:
                process = int(input('\nВведіть 1 для продовження роботи програми: '))
            except:
                break
            continue
        table = interval_halving_method(d[0], d[1], d[2], d[3], a, b, e)
        headers = ['k', 'a_k', 'b_k', 'x_c_k', 'L_2k', '|L_2k|']
        rows = [headers]
        for t in table:
            rows.append(t)
        print(tabulate(rows, tablefmt="fancy_grid"))
        print(f'Оптимальне значення х = {rows[-1][3]}')
        print(f'Мінімальне значення функції f(x) = {round(cubic_function(d[0], d[1], d[2], d[3], float(rows[-1][3])),3)}')
        try:
            process = int(input('\nВведіть 1 для продовження: '))
        except:
            break
        print('\n')
    input('Натисніть Enter, щоб закрити вікно...')


if __name__ == '__main__':
    main()
