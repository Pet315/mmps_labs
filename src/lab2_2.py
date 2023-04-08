from tabulate import tabulate


class LinearSystem:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def system_of_equations(self):
        sys = []
        for i in range(4):
            eq = '{ '
            for j in range(4):
                eq += f'{self.a[i][j]}x{j+1}'
                if i < 4 and j < 3:
                    eq += ' + '
            sys.append(f'{eq} = {self.b[i]}')
        return sys

    def swap_rows(self):
        self.a = [self.a[3], self.a[1], self.a[0], self.a[2]]
        self.b = [self.b[3], self.b[1], self.b[0], self.b[2]]
        return self.system_of_equations()

    def gauss_seidel_method(self):
        x = [[]]
        for i in range(4):
            x[0].append(0)
        k = 0
        next = True
        faults = []

        while next:
            appr = []
            fault = []
            for i in range(4):
                indexes = []
                for j in range(4):
                    if j != i:
                        indexes.append(j)

                m1 = 1 / self.a[i][i]  # множник 1
                m2 = self.b[i] # множник 2
                for index in indexes:
                    if index < i:
                        m2 -= self.a[i][index] * appr[index]
                    else:
                        m2 -= self.a[i][index] * x[k][index]
                xi = round(m1 * m2, 3)

                appr.append(round(xi, 3))
                fault.append(round(appr[i] - x[k][i], 3))

            x.append(appr)
            faults.append(fault)
            if -0.001 < fault[-1] < 0.001:  # -1 - останній елемент списку
                next = False
            k += 1

        return x, faults


if __name__ == '__main__':
    matrix_a = [
        [-9, 4, 64, 0],
        [10, 50, 0, -4],
        [0, -14, 7, 80],
        [40, 9, 0, 0]
    ]
    matrix_b = [24, -5, 14, 29]

    ls = LinearSystem(matrix_a, matrix_b)
    system = ls.system_of_equations()
    print('1. Система рівнянь:')
    for eq in system:
        print(eq)

    system = ls.swap_rows()
    print('\n2. СЛАР, в якій поміняли рівняння місцями (4,2,1,3):')
    for eq in system:
        print(eq)

    x, faults = ls.gauss_seidel_method()
    print('\n3. Обчислені наближені значення x1, x2, x3, x4:')
    x_headers = []
    for i in range(1, 5):
        x_headers.append(f'x{i}')
    for i in range(len(x)):
        print(f'k={i}:')
        print(tabulate([x_headers, x[i]], tablefmt="fancy_grid"))

    print('\n4. Значення похибки після кожної ітерації:')
    for i in range(len(faults)):
        print(f'k={i+1}:')
        f_headers = []
        for j in range(4):
            f_headers.append(f'X{i+1}-X{i}')
        print(tabulate([f_headers, faults[i]], tablefmt="fancy_grid"))

    print("\n5. Pозв'язок системи:")
    print(tabulate([x_headers, x[-1]], tablefmt="fancy_grid"))  # -1 - останній елемент списку
