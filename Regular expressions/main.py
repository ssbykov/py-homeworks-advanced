import csv
import re

def add_dict(contact):
    # обработка полей ФИО
    if contact[1:3] == ['', '']:
        contact[:len(contact[0].split())] = contact[0].split(' ')
    elif contact[2] == '': 
        contact[1:1 + len(contact[1].split())] = contact[1].split(' ')
    #формирование словаря с контактами
    key_contact = ' '.join(contact[:2])
    if contact[5]:
        format_phone()
    if  key_contact not in contacts_dic:
        contacts_dic[key_contact] = contact
    else:
    #соединение данных в случае дублирования
        for i in range(2, 7):
            if not contacts_dic[key_contact][i] and contact[i]:
                contacts_dic[key_contact][i] = contact[i] 

def format_phone():
    # contact[5] = re.sub(r'(\s+)?\(?(доб.)(\s+)?(\d+)\)?', r' доб.\4', contact[5])
    # contact[5] = re.sub(r'(\+7|8)\s?\(?(\d{3})\)?[\s-]?((\d{3}))[\s-]?((\d{2}))[\s-]?((\d{2}))', r'+7(\2)\4-\6-\8', contact[5])
    contact[5] = re.sub(r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]?((\d{3}))[\s-]?((\d{2}))[\s-]?(\d{2})(\s*)\(?(доб.)?\s*(\d+)?\)?', r'+7(\2)\4-\6-\7\8\9\10', contact[5])

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts_dic = {0: ['lastname','firstname','surname','organization','position','phone','email']}
    for contact in contacts_list[1:]:
        add_dict(contact)
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list(contacts_dic.values()))