def find_number(lst: list) -> list:
    n = len(lst)
    result = []
    for i in range(n):
        i = lst.count(i)
        result.append(i)
    return result


def main():
    n = int(input('Введите количество элементов списка: '))
    info = []
    for i in range(n):
        print(f'Введите {i+1} элемент списка:\n ')
        temp = int(input())
        info.append(temp)
    result = find_number(info)
    for i in range(len(result)):
        print(result[i], end = ' ')


main()