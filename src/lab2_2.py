def system_of_equations(a, b):
    sys = []
    for i in range(4):
        eq = '{ '
        for j in range(4):
            eq += f'{a[i][j]}x{j+1}'
            if i < 4 and j < 3:
                eq += ' + '
        sys.append(f'{eq} = {b[i]}')
    return sys


def gauss_seidel_method(a, b):
    x = [[]]
    for i in range(4):
        x[0].append(0)
    k = 1

    while 1:
        fault = []
        for i in range(4):
            indexes = []
            for j in range(4):
                if j != i:
                    indexes.append(j)
            print(indexes)

            try:
                m1 = 1/a[i][i]
            except ZeroDivisionError:
                return '∅'

            # m1 = 1 / a[i][i]
            m2 = b[i]
            for index in indexes:
                # if index < len(x[k-1]):
                #     appr = x[k][index]
                # else:
                #     appr = x[k-1][index]
                # print(f'{index}: -= {a[i][index]} * {appr}')
                # m2 -= a[i][index] * appr

                print(f'{index}: -= {a[i][index]} * {x[k-1][index]}')
                m2 -= a[i][index] * x[k-1][index]
            xi = round(m1 * m2, 3)
            print(f'{round(m1, 3)} * {m2} = {xi}')

            if i == 0:
                x.append([xi])
            else:
                x[k].append(xi)

            fault.append(xi - x[k][i])
            print('x_k:', x[k])

        if fault[-1] < 0.001:
            return x
        k += 1


if __name__ == '__main__':
    matrix_a = [
        [-9, 4, 64, 0],
        [10, 50, 0, -4],
        [0, -14, 7, 80],
        [40, 9, 0, 0]
    ]
    matrix_b = [24, -5, 14, 29]
    system = system_of_equations(matrix_a, matrix_b)
    # print('1. Система рівнянь:')
    # for eq in system:
    #     print(eq)

    print('2. Обчислені наближені значення x1, x2, x3, x4:')
    print(gauss_seidel_method(matrix_a, matrix_b))
