def sort_string(s):
    """Возвращает список двузначных чисел из строки"""
    res = s.split(" ")
    def filter_metod(a):
        if int(a) < 10:
            return False
        if int(a) > 99:
            return False
        return  True
    return list(filter(filter_metod, res))

if __name__ == "__main__":
    print(sort_string("1 1 1 1 12 2 12 12 12 12 123 4 5 3"))