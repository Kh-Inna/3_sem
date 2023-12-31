import sys
import math

def get_coef(index, prompt):
    while True:
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
            if (coef_str.startswith('-') and coef_str[1:].isdigit()) or (coef_str.isdigit()):
                coef = float(coef_str)
                return coef
            else:
                print("Wrong!")
                coef_str = None

def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if root > 0:
            root_1 = math.sqrt(root)
            root_2 = -1 * math.sqrt(root)
            result.append(root_1)
            result.append(root_2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        if root1 > 0:
            root_1 = math.sqrt(root1)
            root_2 = -1 * math.sqrt(root1)
            result.append(root_1)
            result.append(root_2)
        if root2 > 0:
            root_1 = math.sqrt(root2)
            root_2 = -1 * math.sqrt(root2)
            result.append(root_1)
            result.append(root_2)
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыри корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4