import random
from string import ascii_lowercase, ascii_uppercase

to_emails = ascii_lowercase + ascii_uppercase + "0123456789_"

def generate_emails(email_length: int = 8, email_count: int = 7):
    """Возвращает список случайно сгенерированных почт с длинной названия аккаунта email_length и количеством email_count"""
    if email_count <= 0:
        raise ValueError("Количество генерируемых почт не может быть меньше либо равно 0")
    if email_length <= 0:
        raise ValueError("Длина пароля не может быть меньше либо равно 0")
    res = []
    for i in range(0, email_count):
        s = ""
        for j in range(0, email_length):
            s += random.choice(to_emails)
        s += '@mail.ru'
        res.append(s)
    return res

if __name__ == "__main__":
    print(generate_emails())
