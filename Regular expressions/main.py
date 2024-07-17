# https://github.com/netology-code/py-homeworks-advanced/tree/master/5.Regexp

"""Здравствуйте. Я бы рекомендовал следующий алгоритм.
1. Открываете файл на чтение и запускаете цикл по строкам этого файла. При этом первую строку с заголовками можно пропустить.
2. В цикле сначала можно "раскидать" ФИО по первым трем элементам, поскольку есть записи, где они не на местах.
3. Дальше с помощью регулярки привести в нужный вид телефон.
4. Далее, как вариант, собирать данные в словарь, где ключи ФИ, а значения полные данные по записи.
При добавлении очередного элемента в словарь, проверяете наличия ключа ФИ. Если ключ уже есть, то объединяете данные
 по двум записям.
5. Объединять записи можно во внутреннем цикле перебирая элементы одной из записей, проверяя их на пустоту.
 Если элемент пустой, то класть элемент из дублирующей записи.
6. На последнем шаге уже записать значение элементов словаря в результирующий файл. """


import csv
import re


#второй вариант
if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts_dic = {0: ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']}
    for contact in contacts_list[1:]:
        # обработка полей ФИО
        fio = ' '.join(contact[:2]).strip().split(' ')
        contact[:len(fio)] = fio
        # формирование словаря с контактами
        key_contact = ' '.join(contact[:2])
        if contact[5]:
            contact[5] = re.sub(
                r'(\+7|8)?\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s?)\(?(доб.)?\s?(\d+)?\)?',
                r'+7(\2)\3-\4-\5\6\7\8', contact[5])
        if key_contact not in contacts_dic:
            contacts_dic[key_contact] = contact
        else:
            # соединение данных в случае дублирования
            contacts_dic[key_contact] = [x if x else contact[i] for i, x in enumerate(contacts_dic[key_contact])]
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list(contacts_dic.values()))