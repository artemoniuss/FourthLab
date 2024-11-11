import random

def get_square_circle():
    """Возвращает список площадей кругов с радиусами от 10 до 100"""
    pi = 3.1415926
    res = []
    for i in range(0, 5):
        r = random.randint(10, 100)
        sq = pi * r ** 2
        res.append(round(sq, 2))
    return res

if __name__ == "__main__":
    print(get_square_circle())