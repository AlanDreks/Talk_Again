import os
# import random


def viewing(file_name_func, date_today_func):
    alphabet_file_statistic = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', file_name_func)
        , 'r', encoding='utf-8')
    for letter in alphabet_file_statistic:
        if letter != '\n':
            print(letter)
    alphabet_file_statistic.close()


def choice_user(file_name_func, date_today_func):
    test_file = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', file_name_func)
        , 'r', encoding='utf-8')
    dict_all_parts = dict()
    for part in test_file:
        if part != '\n':
            all_parts = part.split()
            dict_all_parts[all_parts[0]] = all_parts[1]
    test_file.close()

    average_condition = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', file_name_func)
        , 'w', encoding='utf-8')
    average_condition.write('               {}'.format(date_today_func))
    average_condition.close()

    test_file = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', file_name_func)
        , 'a', encoding='utf-8')
    for key_part, val_part in dict_all_parts.items():
        print('\n' + key_part)
        user_index_part = int(input('\nКак хорошо прошло повторение(от 1 до 5): '))
        if val_part == '0':
            index_part = str(user_index_part)
        else:
            index_part = (float(val_part) + user_index_part) / 2
        letter = key_part + '          ' + str(index_part)
        test_file.write('\n\n   ' + letter)
    test_file.close()


def user_choice_test(choice_test_alpha_syl_word):
    if choice_test_alpha_syl_word == '1':
        return 'alphabet_file_statistic.txt'
    elif choice_test_alpha_syl_word == '2':
        return 'syllables_list_file_statistic.txt'
    elif choice_test_alpha_syl_word == '3':
        return 'finish_list_words.txt'


def make_words(file_name_make_words, date_today_func):
    test_file_make_words = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', file_name_make_words)
        , 'r', encoding='utf-8')
    dict_syllable = {}
    for syllable in test_file_make_words:
        if syllable != '\n':
            all_parts = syllable.split()
            if float(all_parts[1]) >= 3:
                dict_syllable[all_parts[0]] = all_parts[1]
    test_file_make_words.close()
    step = 1
    for syl_key, syl_val in dict_syllable.items():
        print('{}/{}'.format(step, len(dict_syllable)))
        step += 1
        for syl_key_2, syl_val_2 in dict_syllable.items():
            dal_file_write_word = open(
                os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', 'words_list_file_statistic.txt')
                , 'r', encoding='utf-8')
            for dal_word in dal_file_write_word:
                dal_word_fin = dal_word[:-1].lower()
                syl_key_1_2 = syl_key + syl_key_2
                if dal_word_fin == syl_key_1_2:
                    print(dal_word_fin)
                    test_file_write_word = open(
                        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/', 'finish_list_words.txt')
                        , 'a', encoding='utf-8')
                    test_file_write_word.write('\n' + syl_key + syl_key_2)
                    test_file_write_word.close()


date_today = input('Введите дату формата хх.хх.хх :')

# Choice start
while True:

    print('1. Начать обучение')
    print('2. Просмотреть статистику по списку слогов')
    print('3. Просмотреть статистику по списку слов')
    print('4. Составить слова из легкопроизносимых слогов')
    user_answer = input('Выберите действие(укажите соответствующую цифру): ')
    if user_answer in ['1', '2', '3', '4']:
        break


# 1. Пройти тест(Закончено)
if user_answer == '1':
    # Проходим тест на повторение:
    # 5 - может прочитать четко
    # 4 - может прочитать с дефектами
    # 3 - может повторить четко
    # 2 - может повторить с дефектами
    # 1 - не может повторить
    choice_test = input('Выберите тест(1 - буквы, 2 - слоги, 3 - слова): ')
    user_choice_test = user_choice_test(choice_test)
    choice_user(user_choice_test, date_today)


# 2. Просмотреть статистику по буквам и слогам(Закончено)
if user_answer == '2':
    file_name = 'syllables_list_file_statistic.txt'
    viewing(file_name, date_today)

# 3. Просмотреть статистику по списку слов(Закончено)
if user_answer == '3':
    file_name = 'finish_list_words.txt'
    viewing(file_name, date_today)


# 4. Составить слова из легкопроизносимых слогов
if user_answer == '4':
    file_name = 'syllables_list_file_statistic.txt'
    make_words(file_name, date_today)
