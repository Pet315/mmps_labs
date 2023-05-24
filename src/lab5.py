import lab4
import math
import matplotlib.pyplot as plt


def multi_channel_with_unlimited_queue(l, m, n):
    ro = round(l / m, 2)
    p_0 = 1
    for i in range(1, n):
        p_0 += ro ** i / math.factorial(i)
    p_0 += math.factorial(n) * (n - ro)
    p_0 = round(1 / p_0, 2)

    y = round(ro / n, 2)
    r = round((ro ** (n+1) * p_0) / (n * math.factorial(n) * (1 - y) ** 2), 2)

    return f"""\nМатематичною моделлю є {n}-канальна СМО з відмовами
        1) приведена інтенсивність: ro = {ro}
        2) гранична ймовірність того, що немає заявок: р0 = {p_0}
        3) ймовірність відмови: P відм = 0
        4) відносна пропускна здатність системи: Q = 1
        5) абсолютна пропускна здатність системи: A = {l}
        6) середня кількість заявок у черзі: r = {r}
        7) середня кількість зайнятих каналів: z = {round(ro, 2)}
        8) середня кількість заявок, пов’язаних із системою: k = {round(r + l / y, 2)}
        9) середній час очікування заявки в черзі: t оч = {round(r / l, 2)}
        """


def multi_channel_with_limited_queue(n, l, t, m):
    ro = round(l / (1 / t), 2)
    p_0 = 1
    for i in range(1, n):
        p_0 += ro ** i / math.factorial(i)
    p_0 += (ro ** (n+1) * (1 - (ro / n) ** m)) / (n * math.factorial(n) * (1 - ro / n))
    p_0 = round(1 / p_0, 2)
    p_n_m = round((ro ** (n+m) * p_0) / (n**m * math.factorial(n)), 3)
    Q = 1 - p_n_m
    z = round(ro * (1 - (ro ** (n+m) * p_0) / (n**m * math.factorial(n))), 2)
    y = round(ro / n, 2)
    r = round(((ro**(n+1) * p_0) / (n * math.factorial(n))) * ((1 - (m+1) * y**m + m * y**(m+1)) / ((1-y)**2)), 2)

    return [f"""\nМатематичною моделлю є {n}-канальна СМО з відмовами
            1) приведена інтенсивність: ro = {ro}
            2) гранична ймовірність того, що немає заявок: р 0 = {p_0}, p n+m = {p_n_m}
            3) ймовірність відмови: P відм = {p_n_m}
            4) відносна пропускна здатність системи: Q = {Q}
            5) абсолютна пропускна здатність системи: A = {l * Q}
            6) середня кількість зайнятих каналів: z = {z} 
            7) середня кількість заявок у черзі: r = {r}
            8) середня кількість заявок, пов’язаних із системою: k = {round(r + z, 2)}
            9) середній час очікування заявки в черзі: t оч = {round(r / l, 2)}
            10) cередній час перебування заявки в системі: t сист = {round(t + Q / (1 / t), 2)}
            """, p_n_m, l * Q, r / l]


def plot_desc(func_name):
    plt.xlabel('t')
    plt.ylabel(func_name)
    plt.title(f'Графік функції {func_name}(t)')
    plt.grid(True)
    plt.show()


def make_plots(n, l, m):
    t, f, g, h = [], [], [], []
    for i in range(1, 11):
        t.append(i)
        chars = multi_channel_with_limited_queue(n, l, i, m)
        f.append(chars[1])
        g.append(chars[2])
        h.append(chars[3])
        print(f't = {i}')
        print(chars[0])
    plt.plot(t, f, marker='o')
    plot_desc('f')
    plt.plot(t, g, marker='o')
    plot_desc('g')
    plt.plot(t, h, marker='o')
    plot_desc('h')


def select_type(type):
    match type:
        case 1:
            try:
                l, m = lab4.main_params()
            except:
                print('Вводьте тільки числа\n')
                return
            print(lab4.single_channel_with_rejections(l, m))
        case 2:
            try:
                l, m, n = lab4.main_params('кількість каналів')
            except:
                print('Вводьте тільки числа\n')
                return
            print(lab4.multi_channel_with_rejections(l, m, n))
        case 3:
            try:
                l, m, n = lab4.main_params('довжину черги')
            except:
                print('Вводьте тільки числа\n')
                return
            print(lab4.single_channel_with_expectations(l, m, n))
        case 4:
            try:
                l, m, n = lab4.main_params('кількість каналів')
            except:
                print('Вводьте тільки числа\n')
                return
            print(multi_channel_with_unlimited_queue(l, m, n))
        case 5:
            try:
                n = int(input(f'Введіть кількість каналів (n): '))
                l = float(input('Введіть інтенсивність потоку викликів (l): '))
                t = float(input('Введіть середній час обслуговування (t): '))
                m = float(input('Введіть число місць в черзі (m): '))
            except:
                print('Вводьте тільки числа\n')
                return
            print(multi_channel_with_limited_queue(n, l, t, m)[0])
            # make_plots(n, l, m)
        case 6:
            return
        case _:
            print("Програма працює лише для п'ятьох видів СМО")


def main():
    process = 1
    while process == 1:
        print("""Види СМО: 
            1 - одноканальна СМО з відмовами;
            2 - багатоканальна СМО з відмовами;
            3 - одноканальна СМО з очікуванням з обмеженою чергою;
            4 - багатоканальна СМО з очікуванням з необмеженою чергою;
            5 - багатоканальна СМО з очікуванням з обмеженою чергою;
            """)
        try:
            type = int(input('Оберіть вид СМО, або введіть 6 для завершення: '))
        except:
            print('Вводьте тільки числа\n')
            continue
        select_type(type)
        if type == 6:
            break
        try:
            process = int(input('\nВведіть 1 для продовження: '))
        except:
            break
        print('\n')
    input('Натисніть Enter, щоб закрити вікно...')


if __name__ == '__main__':
    main()
    