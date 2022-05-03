
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def m_int(a, b):
    return a * b

# поиск владельца документа по номеру документа
def find_people(docs, document_number):
    # document_number = input('Введите номер документа:')
    for  document in docs:
        if document_number == document["number"]: 
            # print (f'Документ принадлежит: {document["name"]}.')
            return document["name"]
    print('Документ не найден.')

#поиск полки по номеру документа
def find_document_directory(shelves):
    document_number = input('Введите номер документа:')
    for  directory in shelves:
        if document_number in shelves[directory]: 
            print (f'Документ находится на полке {directory}.')
            return
    print('Документ не найден.')

# вывод списка всех документов
def list_of_documents(docs):
    print('Список всех документов:')
    for  document in docs:
        print (f'{document["type"]} "{document["number"]}" "{document["name"]}"')

# функция добввления нового документа
def add_document(docs, shelves):
    document_type = input('Введите тип документа:')
    document_number = input('Введите номер документа:')
    for  document in docs:
        if document_number == document["number"]: 
            print (f'Документ с таким номером уже существует и принадлежит: {document["name"]}.')
            return    
    name_of_owner = input('Введите имя владельца:')
    directory_number = check_shelves(shelves)
    docs.append({"type": document_type, "number": document_number, "name": name_of_owner})
    shelves[directory_number].append(document_number)
    print(f'Документ с номером "{document_number}" добавлен на полку {directory_number}.')

# функция удаления документа
def del_document(docs, shelves):
    document_number = input('Введите номер удаляемого документа:')
    for  document in docs:
        if document_number == document["number"]: 
            docs.remove(document)
            for  directory in shelves:
                if document_number in shelves[directory]: 
                    shelves[directory].remove(document_number)
                    print(f'Документ с номером "{document_number}" удален с полки {directory}.')
            return
    print('Документ не найден.')

# функция переноса документа на другую полку
def move_document(docs, shelves):
    document_number = input('Введите номер переносимого документа:')
    for  document in docs:
        if document_number == document["number"]: 
            directory_number = check_shelves(shelves)
            for  directory in shelves:
                if document_number in shelves[directory]: 
                    shelves[directory].remove(document_number)
                    shelves[directory_number].append(document_number)
                    print(f'Документ с номером "{document_number}" перемещен на полку {directory_number}.')
                    return
    print('Документ не найден.')

# функция добавления новой полки
def add_directory(shelves):
    directory_number = input('Введите номер новой полки:')
    while directory_number in shelves: 
        print('Полка уже существует.') 
        directory_number = input('Введите другой номер новой полки:')
    shelves[directory_number] = []
    print(f'Полка с номером {directory_number} добавлена.')

# функция проверки наличия полки
def check_shelves(shelves):
    directory_number = input('Введите номер полки:')
    while directory_number not in shelves:
        print('Полка не найдена.') 
        directory_number = input('Введите другой номер полки:')
    return directory_number

# функция выбора команды
def select_func(docs,shelves):
    while True:
        user_cmd = input('Введите команду:')
        if user_cmd =='p':
            find_people(docs)          
        elif user_cmd =='s':
            find_document_directory(shelves)          
        elif user_cmd =='l':
            list_of_documents(docs)          
        elif user_cmd =='a':
            add_document(docs,shelves)
        elif user_cmd =='d':
            del_document(docs,shelves)
        elif user_cmd =='m':
            move_document(docs,shelves)
        elif user_cmd =='as':
            add_directory(shelves)          
        elif user_cmd =='sl':
            for shelf, value in shelves.items():
                print(shelf, ': ',value)          
        elif user_cmd =='q':
            print('Выход из программы.')
            break          

if __name__ == '__main__':
    select_func(documents, directories)