"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
        number_of_words = 0
        string_length = 0
        
        for line in f:
            line = line.lower()
            line = line.replace('\n','')
            number_of_words += len(line.split())
            string_length += len(line)
            line = line.replace('.','!')
            
        print(f'Коллисество слов в тексте:{number_of_words}')
        print(f'Длина строки:{string_length}')
        print(line)


    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(line)




if __name__ == "__main__":
    main()
