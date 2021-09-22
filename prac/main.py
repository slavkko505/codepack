# На вершині драбинки, яка містить N сходинок, знаходиться м'ячик,
# який починає стрибати по них вниз, до основи.
# М'ячик може стрибнути на наступну сходинку, на сходинку через одну або через дві.
# Тобто, якщо м'ячик лежить на 8-й сходинці, то він може переміститися на 5-у, 6-у або 7-у.
# Потрібно написати програму, яка визначить число всіляких "маршрутів" м'ячика з вершини на землю.

def ContBallWay(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1

    return ContBallWay(n - 1) + ContBallWay(n - 2) + ContBallWay(n - 3)
def EnterNumber():
    while True:
        try:
            n = int(input('Ведіть исоту сходинки '))
            if n == 0:
                print('\nВедіть число відміне від 0 ')
                continue
            break
        except ValueError:
            print('\nВедіть число')
    return n

print(ContBallWay(EnterNumber()))
