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
    if word.isalpha() == False:
        print('Некорректный ввод')
        return 2

    for letter in list(word):
        if letter not in list_letter:
            print(f'У Вас нет такой буквы "{letter}"')
            return 2
            break

    with open('russian_word.txt', 'r', encoding="utf-8") as file_words:
        for line in file_words:
            line = line.rstrip('\n')
            if line == word:
                print('Такое слово есть')
                return 1
                break
        else:
            return 0


def counts_statistics(user_input):
    '''
    Подсчитывает кол-во баллов за слово
    '''
    dict_score = {2: 2, 3: 3, 4: 6, 5: 7, 6: 8, 7: 10}
    score_user = dict_score[len(user_input)]
    return score_user


def plays(user, list_user, score_user, user_input):
    '''
    Цикл проверки ввода игра и начисления баллов при вернном вводе
    '''
    attempt = 0
    while True:
        check_word_result = check_word(user_input, list_user)
        if check_word_result == 0:
            letters = create_list_letters(1)
            list_user.extend(letters)
            letters_str = ','.join(letters)
            print(f'Такого слова нет\n{user} не получает очков\nДобавляю букву "{letters_str}"')
            letters.clear()
            return list_user, score_user
            break
        if check_word_result == 2:
            letters_print = ','.join(list_user)
            print(f'{user} - буквы: "{letters_print}"')
            if attempt == 0:
                user_input = input('У вас осталась одна попытка до передачи хода - ')
                attempt += 1
                continue
            else:
                print('Передача хода')
                return list_user, score_user
                break
        if check_word_result == 1:
            statistics_word = counts_statistics(user_input)
            print(f'{user} получает {statistics_word} балла.')
            score_user += statistics_word
            list_user_input = list(user_input)
            for i in list_user_input:
                if i in list_user:
                    list_user.remove(i)
            letters = create_list_letters(len(user_input) + 1)
            list_user.extend(letters)
            letters_str = ','.join(letters)
            print(f'Добавляю буквы {letters_str}')
            letters.clear()
            return list_user, score_user
            break


def main():
    '''
    Проводит основной цикл игры
    '''
    print('Программа:\nПривет, начинаем играть в Scrabble')
    user_first = input('Как зовут первого игрока?\nПользователь: ').title()
    user_second = input('Как зовут второго игрока?\nПользователь: ').title()
    print(f'Программа:\n{user_first} vs {user_second}\n(Раздаю случайные слова)')
    list_first = create_list_letters(7)
    list_second = create_list_letters(7)
    score_user_first = 0
    score_user_second = 0
    turn_game = 0
    flag = False
    while True:
        if len(dict_letters.keys()) < 3:
            flag = True
        if sum(dict_letters.values()) < 5:
            flag = True
        if flag == True:
            print(f'Конец\n{user_first} - {score_user_first} очков\n{user_second} - {score_user_second} очков')
            break
        turn_game += 1
        user = user_first if turn_game % 2 != 0 else user_second
        list_user = list_first if turn_game % 2 != 0 else list_second
        score_user = score_user_first if turn_game % 2 != 0 else score_user_second
        letters_print = ','.join(list_user)
        print('Что бы остановть игру введите "stop"')
        print(f'{user} - буквы: "{letters_print}"')
        user_input = input(f'Ходит {user}\nПользователь: ').lower()
        if user_input == 'stop':
            flag = True
            continue
        result_plays = plays(user, list_user, score_user, user_input)
        if turn_game % 2 != 0:
            list_first, score_user_first = result_plays
            continue
        else:
            list_second, score_user_second = result_plays
            continue


main()
