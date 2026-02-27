# 1
def validate_INN():
    while True:
        try:
            INN = int(input("Введите ваш ИНН (12 цифр): "))
        except ValueError:
            print(" Ошибка ввода. Пожалуйста, введите **целое число**.")
        else:
            if len(str(INN)) == 12:
              print(" ИНН состоит ровно из 12 цифр.")
              return INN
            else:
              print("Неправильно")



validate_INN()

# 2

while True:
    try:
        price = float(input("Введите цену товара: "))
    except ValueError:
        print("Ошибка: введите число.")
    except KeyboardInterrupt:
        print("ну пж введи число")
    else:
        if price > 0 and price <= 1_000_000:
            print("Принято")
            break
        else:
            print("Цена должна быть положительной и не превышать 1 000 000.")

# 3
def get_password():
    while True:
        password = input("Введите пароль: ")
        if 8 <= len(password) <= 20:
            has_upper = any(c.isupper() for c in password)
            has_digit = any(c.isdigit() for c in password)
            if has_upper and has_digit:
                return password
            else:
                print("Пароль должен содержать хотя бы одну заглавную букву и хотя бы одну цифру.")
        else:
            print("Длина пароля должна быть от 8 до 20 символов.")

get_password()

