import os
# import random


# alphabet_and_syllables_data = ('а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
#                                'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я', 'аб', 'яб', 'уб', 'юб', 'об', 'эб',
#                                'ыб', 'иб', 'ав', 'яв', 'ув', 'юв', 'ов', 'ёв', 'эв', 'ев', 'ыв', 'ив', 'аг', 'яг', 'уг',
#                                'юг', 'ог', 'ёг', 'эг', 'ег', 'ыг', 'иг', 'яд', 'уд', 'юд', 'од', 'ёд', 'эд', 'ед', 'ыд',
#                                'ид', 'аж', 'яж', 'уж', 'юж', 'ож', 'ёж', 'эж', 'еж', 'ыж', 'иж', 'аз', 'яз', 'уз', 'юз',
#                                'оз', 'ёз', 'эз', 'ез', 'ыз', 'из', 'ай', 'яй', 'уй', 'ой', 'ёй', 'эй', 'ей', 'ый', 'ий',
#                                'ак', 'як', 'ук', 'юк', 'ок', 'ёк', 'эк', 'ек', 'ык', 'ик', 'ал', 'ял', 'ул', 'юл', 'ол',
#                                'ёл', 'эл', 'ел', 'ыл', 'ил', 'ам', 'ям', 'ум', 'юм', 'ом', 'ём', 'эм', 'ем', 'ым', 'им',
#                                'ан', 'ян', 'ун', 'юн', 'он', 'ён', 'эн', 'ен', 'ын', 'ин', 'ап', 'яп', 'уп', 'юп', 'оп',
#                                'ёп', 'эп', 'еп', 'ып', 'ип', 'ар', 'яр', 'ур', 'юр', 'ор', 'ёр', 'эр', 'ер', 'ыр', 'ир',
#                                'ас', 'яс', 'ус', 'юс', 'ос', 'ёс', 'эс', 'ес', 'ыс', 'ис', 'ат', 'ят', 'ут', 'ют', 'от',
#                                'ёт', 'эт', 'ет', 'ыт', 'ит', 'аф', 'яф', 'уф', 'юф', 'оф', 'ёф', 'эф', 'еф', 'ыф', 'иф',
#                                'ах', 'ях', 'ух', 'юх', 'ох', 'ёх', 'эх', 'ех', 'ых', 'их', 'ац', 'яц', 'уц', 'юц', 'оц',
#                                'ёц', 'эц', 'ец', 'ыц', 'иц', 'аш', 'яш', 'уш', 'юш', 'ош', 'ёш', 'эш', 'еш', 'ыш', 'иш',
#                                'ащ', 'ящ', 'ущ', 'ющ', 'ощ', 'ёщ', 'эщ', 'ещ', 'ыщ', 'ищ', 'ба', 'бя', 'бу', 'бю', 'бо',
#                                'бё', 'бэ', 'бе', 'бы', 'би', 'ва', 'вя', 'ву', 'вю', 'во', 'вё', 'вэ', 'ве', 'вы', 'ви',
#                                'га', 'гя', 'гу', 'гю', 'го', 'гё', 'гэ', 'ге', 'гы', 'ги', 'да', 'дя', 'ду', 'дю', 'до',
#                                'дё', 'дэ', 'де', 'ды', 'ди', 'жа', 'жя', 'жу', 'жю', 'жо', 'жё', 'жэ', 'же', 'жи', 'за',
#                                'зя', 'зу', 'зю', 'зо', 'зё', 'зэ', 'зе', 'зы', 'зи', 'ка', 'кя', 'ку', 'кю', 'ко', 'кё',
#                                'кэ', 'ке', 'кы', 'ки', 'ла', 'ля', 'лу', 'лю', 'ло', 'лё', 'лэ', 'ле', 'лы', 'ли', 'ма',
#                                'мя', 'му', 'мю', 'мо', 'мё', 'мэ', 'ме', 'мы', 'ми', 'на', 'ня', 'ну', 'ню', 'но', 'нё',
#                                'нэ', 'не', 'ны', 'ни', 'па', 'пя', 'пу', 'пю', 'по', 'пё', 'пэ', 'пе', 'пы', 'пи', 'ра',
#                                'ря', 'ру', 'рю', 'ро', 'рё', 'рэ', 'ре', 'ры', 'ри', 'са', 'ся', 'су', 'сю', 'со', 'сё',
#                                'сэ', 'се', 'сы', 'си', 'та', 'тя', 'ту', 'тю', 'то', 'тё', 'тэ', 'те', 'ты', 'ти', 'фа',
#                                'фу', 'фо', 'фё', 'фэ', 'фе', 'фы', 'фи', 'ха', 'хя', 'ху', 'хо', 'хё', 'хэ', 'хе', 'хы',
#                                'хи', 'ца', 'цу', 'цо', 'це', 'цы', 'ци', 'ша', 'шу', 'шо', 'шэ', 'ше', 'ши', 'ща', 'щу',
#                                'що', 'ще', 'щи')

# alphabet_and_syllables_data = ('аб', 'яб', 'уб', 'юб', 'об', 'эб', 'ыб', 'иб', 'ав', 'яв', 'ув', 'юв', 'ов', 'ёв', 'эв',
#                                'ев', 'ыв', 'ив', 'аг', 'яг', 'уг', 'юг', 'ог', 'ёг', 'эг', 'ег', 'ыг', 'иг', 'яд', 'уд',
#                                'юд', 'од', 'ёд', 'эд', 'ед', 'ыд', 'ид', 'аж', 'яж', 'уж', 'юж', 'ож', 'ёж', 'эж', 'еж',
#                                'ыж', 'иж', 'аз', 'яз', 'уз', 'юз', 'оз', 'ёз', 'эз', 'ез', 'ыз', 'из', 'ай', 'яй', 'уй',
#                                'ой', 'ёй', 'эй', 'ей', 'ый', 'ий', 'ак', 'як', 'ук', 'юк', 'ок', 'ёк', 'эк', 'ек', 'ык',
#                                'ик', 'ал', 'ял', 'ул', 'юл', 'ол', 'ёл', 'эл', 'ел', 'ыл', 'ил', 'ам', 'ям', 'ум', 'юм',
#                                'ом', 'ём', 'эм', 'ем', 'ым', 'им', 'ан', 'ян', 'ун', 'юн', 'он', 'ён', 'эн', 'ен', 'ын',
#                                'ин', 'ап', 'яп', 'уп', 'юп', 'оп', 'ёп', 'эп', 'еп', 'ып', 'ип', 'ар', 'яр', 'ур', 'юр',
#                                'ор', 'ёр', 'эр', 'ер', 'ыр', 'ир', 'ас', 'яс', 'ус', 'юс', 'ос', 'ёс', 'эс', 'ес', 'ыс',
#                                'ис', 'ат', 'ят', 'ут', 'ют', 'от', 'ёт', 'эт', 'ет', 'ыт', 'ит', 'аф', 'яф', 'уф', 'юф',
#                                'оф', 'ёф', 'эф', 'еф', 'ыф', 'иф', 'ах', 'ях', 'ух', 'юх', 'ох', 'ёх', 'эх', 'ех', 'ых',
#                                'их', 'ац', 'яц', 'уц', 'юц', 'оц', 'ёц', 'эц', 'ец', 'ыц', 'иц', 'аш', 'яш', 'уш', 'юш',
#                                'ош', 'ёш', 'эш', 'еш', 'ыш', 'иш', 'ащ', 'ящ', 'ущ', 'ющ', 'ощ', 'ёщ', 'эщ', 'ещ', 'ыщ',
#                                'ищ')
alphabet_and_syllables_data = ('аба', 'ага', 'аза', 'азу', 'азы', 'ака', 'Ама', 'ара', 'ату', 'аул', 'аут', 'Ева',
                               'его', 'еда', 'еду', 'еды', 'едь', 'ежа', 'ель', 'ёрш', 'ещё', 'ибо', 'ива', 'иго',
                               'иди', 'ила', 'или', 'имя', 'инь', 'Ира', 'ифа', 'йод', 'йух', 'оба', 'ого', 'Оля',
                               'она', 'они', 'оно', 'опа', 'опт', 'ору', 'оса', 'осе', 'осу', 'осы', 'ось', 'Оши',
                               'УАЗ', 'угу', 'уже', 'Узи', 'ума', 'уму', 'ура', 'усы', 'уха', 'ухо', 'уют', 'эго',
                               'эко', 'эль', 'Эля', 'эму', 'эра', 'эта', 'это', 'эхо', 'юга', 'юла', 'Юля', 'Юра',
                               'Ява', 'явь', 'яга', 'Яго', 'яма', 'яму', 'Яна', 'ярд', 'Яша', 'сыр')


def viewing(file_name_func, date_today_func):
    alphabet_file_statistic = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/Talk_Again_Project/', file_name_func)
        , 'r', encoding='utf-8')
    for letter in alphabet_file_statistic:
        if letter != '\n':
            print(letter)
    alphabet_file_statistic.close()


def choice_user(date_today_func, alphabet_and_syllables_data_func):
    dict_today_home_work = dict()
    dict_today_home_work['\n\nдата'] = date_today_func
    user_index_part = ''
    step = 0
    for part_syllables in alphabet_and_syllables_data_func:
        step += 1
        if user_index_part == 'stop':
            break
        print('\n{}/{}                          {}'.format(step, len(alphabet_and_syllables_data_func), part_syllables))
        while True:
            user_index_part = input('\nКак хорошо прошло повторение(от 1 до 5): ')
            if user_index_part in ['0', '1', '2', '3', '4', '5']:
                dict_today_home_work[part_syllables] = user_index_part
                break
            elif user_index_part not in ['0', '1', '2', '3', '4', '5', 'stop']:
                print('\nВведите оценку или стоп-слово')
                continue
            elif user_index_part == 'stop':
                for part_syllables_2 in alphabet_and_syllables_data_func:
                    if part_syllables_2 not in dict_today_home_work.keys():
                        dict_today_home_work[part_syllables_2] = 0
                break
    # average_condition = open('alphabet_syllables_list_file_statistic.txt', 'a', encoding='utf-8')
    average_condition = open('finish_list_words.txt', 'a', encoding='utf-8')
    average_condition.write(str(dict_today_home_work))
    average_condition.close()

def user_choice_test(choice_test_alpha_syl_word):
    if choice_test_alpha_syl_word == '1':
        return 'alphabet_syllables_list_file_statistic.txt'
    elif choice_test_alpha_syl_word == '2':
        return 'finish_list_words.txt'


def make_words(file_name_make_words, date_today_func):
    test_file_make_words = open(
        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/Talk_Again_Project/', file_name_make_words)
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
                os.path.join(
                    '/media/alan/5C546A3B546A1852/Talk_Again/Talk_Again_Project/words_list_file_statistic.txt')
                , 'r', encoding='utf-8')
            for dal_word in dal_file_write_word:
                dal_word_fin = dal_word[:-1].lower()
                syl_key_1_2 = syl_key + syl_key_2
                if dal_word_fin == syl_key_1_2:
                    print(dal_word_fin)
                    test_file_write_word = open(
                        os.path.join('/media/alan/5C546A3B546A1852/Talk_Again/Talk_Again_Project/finish_list_words.txt')
                        , 'a', encoding='utf-8')
                    test_file_write_word.write('\n' + syl_key + syl_key_2)
                    test_file_write_word.close()


date_today = input('Введите дату формата хх.хх.хх: ')

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
    while True:
        choice_test = input('Выберите тест(1 - слоги, 2 - слова): ')
        if choice_test == '1' or choice_test == '2':
            user_choice_test = user_choice_test(choice_test)
            choice_user(date_today, alphabet_and_syllables_data)
            break
        else:
            print('Неправильный ввод! Выберите 1 или 2!')

# 2. Просмотреть статистику по буквам и слогам
if user_answer == '2':
    file_name = 'alphabet_syllables_list_file_statistic.txt'
    viewing(file_name, date_today)

# 3. Просмотреть статистику по списку слов
if user_answer == '3':
    file_name = 'finish_list_words.txt'
    viewing(file_name, date_today)


# 4. Составить слова из легкопроизносимых слогов
if user_answer == '4':
    file_name = 'syllables_list_file_statistic.txt'
    make_words(file_name, date_today)
