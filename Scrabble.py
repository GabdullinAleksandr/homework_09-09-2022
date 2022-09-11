from random import choices


global dict_letters
dict_letters = {'а': 8, 'б': 2, 'в': 4, 'г': 2, 'д': 4, 'е': 8, 'ё': 1, 'ж': 1, 'з': 2, 'и': 5, 'й': 1, 'к': 4,
                'л': 4, 'м': 3, 'н': 5, 'о': 10, 'п': 4, 'р': 5, 'с': 5, 'т': 5, 'у': 4, 'ф': 1, 'х': 1, 'ц': 1,
                'ч': 1, 'ш': 1, 'щ': 1, 'ъ': 1, 'ы': 2, 'ь': 2, 'э': 1, 'ю': 1, 'я': 2}


def create_list_letters(quantity):
    '''
    Достает из словаря заданное кол-во случайных букв и
    сразу уменьшает кол-во этих букв в словаре
    '''

    list_random = choices(list(dict_letters.keys()), k=quantity)
    for letter in list_random:
        if dict_letters[letter] == 0:
            del dict_letters[letter]
        else:
            dict_letters[letter] = dict_letters[letter] - 1
    return list_random


def check_word(word, list_letter):
    '''
    Проверяет введенное слово на все возможные ошибки и существует ли такое слово
    '''
    flag = False
    if word.isalpha() == False:
        print('Некорректный ввод')
        return 2

    for letter in list(word):
        if letter not in list_letter:
            print(f'У Вас нет такой буквы "{letter}"')
            return 2
            break

    with open('russian_word.txt', 'r', encoding="utf-8") as file_words:
        if flag == True:
            file_words.close()
        for line in file_words:
            line = line.rstrip('\n')
            if line == word:
                print('Такое слово есть')
                return 1
                break
                flag = True
        else:
            return 0


def counts_statistics(user_input):
    dict_score = {2: 2, 3: 3, 4: 6, 5: 7, 6: 8, 7: 10}
    score_user = dict_score[len(user_input)]
    return score_user


def main():
    flag = False
    print('Программа:\nПривет, начинаем играть в Scrabble')
    user_first = input('Как зовут первого игрока?\nПользователь: ').title()
    user_second = input('Как зовут второго игрока?\nПользователь: ').title()
    print(f'Программа:\n{user_first} vs {user_second}\n(Раздаю случайные слова)')
    list_first = create_list_letters(7)
    list_second = create_list_letters(7)
    score_user_first = 0
    score_user_second = 0
    while True:
        print('Что бы остановть игру введите "stop"')
        if len(dict_letters.keys()) < 3:
            flag = True
        if sum(dict_letters.values()) < 5:
            flag = True
        if flag == True:
            print(f'Конец\n{user_first} - {score_user_first} очков\n{user_second} - {score_user_second} очков')
            break
        while True:    #Играет первый пользователь
            check_word_result = ''
            letters_first = ','.join(list_first)
            print(f'{user_first} - буквы: "{letters_first}"')
            user_first_input = input(f'Ходит {user_first}\nПользователь: ').lower()
            check_word_result = check_word(user_first_input, list_first)
            if user_first_input == 'stop':
                flag = True
                break
            if check_word_result == 0:
                letters = create_list_letters(1)
                list_first.extend(letters)
                letters_str = ','.join(letters)
                print(f'Такого слова нет\n{user_first} не получает очков\nДобавляю букву {letters_str}')
                letters.clear()
                break
                print('Не сработал break')
            if check_word_result == 2:
                letters_first = ','.join(list_first)
                print(f'{user_first} - буквы: "{letters_first}"')
                continue
            if check_word_result == 1:
                statistics_word = counts_statistics(user_first_input)
                print(f'{user_first} получает {statistics_word} балла.')
                score_user_first += statistics_word
                list_user_first_input = list(user_first_input)
                for i in list_user_first_input:
                    if i in list_first:
                        list_first.remove(i)
                letters = create_list_letters(len(user_first_input)+ 1)
                list_first.extend(letters)
                letters_str = ','.join(letters)
                print(f'Добавляю буквы {letters_str}')
                letters.clear()
                break
            else:
                print('ERROR')

        if flag == True:
            print(f'Конец\n{user_first} - {score_user_first} очков\n{user_second} - {score_user_second} очков')
            break

        while True:  # Играет второй пользователь
            check_word_result = ''
            letters_second = ','.join(list_second)
            print(f'{user_second} - буквы: "{letters_second}"')
            user_second_input = input(f'Ходит {user_second}\nПользователь: ').lower()
            check_word_result = check_word(user_second_input, list_second)
            if user_second_input == 'stop':
                flag = True
                break
            if check_word_result == 0:
                letters = create_list_letters(1)
                list_second.extend(letters)
                letters_str = ','.join(letters)
                print(f'Такого слова нет\n{user_second} не получает очков\nДобавляю букву {letters_str}')
                letters.clear()
                break
            if check_word_result == 2:
                letters_second = ','.join(list_second)
                print(f'{user_second} - буквы: "{letters_second}"')
                continue
            if check_word_result == 1:
                statistics_word = counts_statistics(user_second_input)
                print(f'{user_second} получает {statistics_word} балла.')
                score_user_second += statistics_word
                list_user_second_input = list(user_second_input)
                for i in list_user_second_input:
                    if i in list_second:
                        list_second.remove(i)
                letters = create_list_letters(len(user_second_input) + 1)
                list_second.extend(letters)
                letters_str = ','.join(letters)
                print(f'Добавляю буквы {letters_str}')
                letters.clear()
                break
            else:
                print('ERROR')



main()
