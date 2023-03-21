# частота использования буквы +
# доля слов в которых встречается конкретная буква
# количество слов +
# количество абзацев +
# количество слов с русскими и английскими буквами +
import re


def text_stat(filename: str):
    data_dict = dict(paragraph_amount=0, word_amount=0, bilingual_word_amount=0)
    try:
        with open(filename, "r", encoding='utf-8') as f:
            line = f.readline()
            while line:
                # убираем все знаки препинания и числа для счета слов
                line = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', line)

                # считаем абзацы
                if line == '\n' and data_dict["paragraph_amount"] == 0:  # первый пропуск значит два абзаца
                    data_dict["paragraph_amount"] += 2
                    line = f.readline()
                    continue
                elif line == '\n':  # следующие добавляют один
                    data_dict["paragraph_amount"] += 1
                    line = f.readline()
                    continue

                # считаем слова с латиницей и кириллицей
                line_list = line.split()
                bilingual_word_counter = 0
                for i in line_list:
                    if bool(re.search('[a-z]', i.lower())) and bool(re.search('[а-я]', i.lower())):
                        bilingual_word_counter += 1
                data_dict["bilingual_word_amount"] += bilingual_word_counter

                # считаем слова
                data_dict["word_amount"] += len(line.split())

                line = f.readline()
            # возвращаемся в начало
            f.seek(0)
            lines = f.readlines()
            # убираем все знаки препинания и числа для счета только букв
            for i in range(len(lines)):
                lines[i] = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', lines[i])

            s = ' '.join(lines).lower().split()

            # считаем частоту символов
            for i in lines:
                for char in i.lower():
                    if char not in data_dict:
                        data_dict[char] = 1
                    else:
                        data_dict[char] += 1

            # считаем частоту
            data_list = []
            for letter in data_dict.keys():
                if letter in ['paragraph_amount', 'word_amount', 'bilingual_word_amount']:
                    continue
                data_list.append([letter, len([i for i in s if letter in i])/data_dict['word_amount']])
            # обновляем словарь
            for i in data_list:
                data_dict[i[0]] = (data_dict[i[0]], i[1])

            # убираем пробелы и переходы
            data_dict.pop(' ')
            data_dict.pop('\n')

        return data_dict
    except Exception as e:
        return {'error': e}


print(text_stat('Files_for_number2/1file.txt'))