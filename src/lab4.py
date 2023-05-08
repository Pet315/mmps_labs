import math


def single_channel_with_rejections(l, m):
    p0 = round(m / (l + m), 2)
    p1 = round(l / (l + m), 2)
    return f"""\nМатематичною моделлю є одноканальна СМО з відмовами
    1) ймовірність того, що канал вільний: p0 = {p0}
    2) ймовірність того, що канал зайнятий: p1 = {p1}
    3) ймовірність відмови: P відм = {p1}
    4) відносна пропускна здатність системи: Q = {p0}
    5) абсолютна пропускна здатність системи: A = {round(l * p0, 2)}
    6) середній час обслуговування одного виклику: t обс = {round(1 / m, 2)}
    7) середній час простою каналу: tl = {round(1 / l, 2)}"""


def multi_channel_with_rejections(l, m, n):
    ro = round(l / m, 2)
    p_0 = 1
    for i in range(1, n + 1):
        p_0 += ro**i / math.factorial(i)
    p_0 = round(1 / p_0, 2)
    p = f'\n\t\tp0 = {p_0}'

    p_n = 0
    for k in range(1, n + 1):
        p_k = round((ro**k / math.factorial(k)) * p_0, 2)
        p += f'\n\t\tp{k} = {p_k}'
        if k == n:
            p_n = p_k

    return f"""\nМатематичною моделлю є {n}-канальна СМО з відмовами
    1) приведена інтенсивність: ro = {ro}
    2) граничні ймовірності станів: {p}
    3) ймовірність відмови: P відм = {p_n}
    4) відносна пропускна здатність системи: Q = {round(1-p_n, 2)}
    5) абсолютна пропускна здатність системи: A = {round(l * (1-p_n), 2)}
    6) середня кількість зайнятих каналів: k = {round(ro * (1-p_n), 2)}
    """


def single_channel_with_expectations(l, m, n):
    ro = round(l / m, 2)
    p_0 = round((1 - ro) / (1 - ro**(n+2)), 3)
    p = f'\n\t\tp0 = {p_0}'

    p_n_plus_1 = 0
    for k in range(1, n + 2):
        p_k = round(ro**k * p_0, 3)
        p += f'\n\t\tp{k} = {p_k}'
        if k == n + 1:
            p_n_plus_1 = p_k

    Q = round(1-p_n_plus_1, 3)
    r = round(((1 - ro**n * (n + 1 - n*ro)) * ro**2) / ((1 - ro**(n+2)) * (1 - ro)), 3)
    w = round((ro - ro**5) / (1 - ro**5), 3)

    return f"""\nМатематичною моделлю є одноканальна СМО з відмовами
    1) приведена інтенсивність: ro = {ro}
    2) граничні ймовірності станів: {p}
    3) ймовірність відмови: P відм = {p_n_plus_1}
    4) відносна пропускна здатність системи: Q = {Q}
    5) абсолютна пропускна здатність системи: A = {round(l * Q, 3)}
    6) середня кількість клієнтів, які очікують в черзі: r = {r}
    7) середня кількість клієнтів, які знаходяться під обслуговуванням: w = {w}
    8) середня кількість клієнтів, що перебувають в системі: k = {r + w}
    9) середній час очікування клієнта в черзі: t оч = {round(r / l, 3)}
    10) середній час, витрачений на обслуговування одного клієнта: t обс = {round(Q / m, 3)}
    11) середній час, який клієнт проводить в системі: t сист = {round(r / l + Q / m, 3)}
    """


def main_params(n_desc=''):
    l = float(input('Введіть інтенсивність потоку викликів (l): '))
    m = float(input('Введіть інтенсивність потоку обслуговування (m): '))
    if n_desc != '':
        n = int(input(f'Введіть {n_desc} (n): '))
        return l, m, n
    return l, m


if __name__ == '__main__':
    process = 1
    while process == 1:
        print("""Види СМО: 
        1 - одноканальна СМО з відмовами;
        2 - багатоканальна СМО з відмовами;
        3 - одноканальна СМО з очікуванням з обмеженою чергою.
        """)
        try:
            type = int(input('Оберіть вид СМО, або введіть 4 для завершення: '))
        except:
            print('Вводьте тільки числа\n')
            continue
        match type:
            case 1:
                try:
                    l, m = main_params()
                except:
                    print('Вводьте тільки числа\n')
                    continue
                print(single_channel_with_rejections(l, m))
            case 2:
                try:
                    l, m, n = main_params('кількість каналів')
                except:
                    print('Вводьте тільки числа\n')
                    continue
                print(multi_channel_with_rejections(l, m, n))
            case 3:
                try:
                    l, m, n = main_params('довжину черги')
                except:
                    print('Вводьте тільки числа\n')
                    continue
                print(single_channel_with_expectations(l, m, n))
            case 4:
                break
            case _:
                print('Програма працює лише для трьох видів СМО')
        try:
            process = int(input('\nВведіть 1 для продовження: '))
        except:
            break
        print('\n')
    input('Гарного дня! Натисніть Enter, щоб закрити вікно...')
