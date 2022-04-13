from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import re
import csv
with open('phonebook_raw.csv', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=',')
  contacts_list = list(rows)
pprint(contacts_list)
# разбиваем имена по столбцам
for element in contacts_list:
  if len(element[0].split()) > 1:
    split_name = []
    split_name = element[0].split()
    element[0] = split_name[0].strip()
    element[1] = split_name[1].strip()
    if len(split_name) >2:
      element[2] = split_name[2].strip()
for element in contacts_list:
  if len(element[1].split()) > 1:
    split_name2 = []
    split_name2 = element[1].split()
    element[1] = split_name2[0].strip()
    element[2] = split_name2[1].strip()
for i in range(0,len(contacts_list)-1):
  if contacts_list[i][0] == contacts_list[i+1][0] and contacts_list[i][1] == contacts_list[i+1][1]:
    for x in range(0,len(contacts_list[0])-1):
      if not contacts_list[i][x]:
        contacts_list[i][x] = contacts_list[i+1][x]







