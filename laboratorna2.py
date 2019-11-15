while True:
    def number(text):
        for letter in set(text):
            if letter.isalpha():
                x = text.count(letter)
                print(letter, "=", x)


    def words(text):
        res = []
        for word in text.split():
            if len(word)>2:
                if word not in res:
                    res.append(word)
        Words = res
        Words.sort()
        result = " ".join(Words)
        print(result)
         

    print("""Що ви бажаєте виконати: 
    1. Порахувати літери
    2. Відсортувати текст
    3. Вихід
    """)

    choice = input("Введіть свій вибір: ")

    print()

    if choice == "1":
        text = input("Введіть текст: ")
        number(text)
    elif choice == "2":
        text = input("Введіть текст: ")
        words(text)
    elif choice == "3":
        print("Дякую що використовуєте нашу програму)")
        break
    else:
        print("Некоректний ввід")

    print()
