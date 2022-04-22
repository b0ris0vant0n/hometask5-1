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

def people(docs):
    number = input('Введите номер документа: ')
    presence = bool
    for document in docs:
        if number in document.values():
            return document['name']
            presence = True
    if presence != True:
        return 'Нет такого номера'


def shelf(dir):
    number = input('Введите номер документа: ')
    presence = bool
    for key, values in dir.items():
        if number in values:
            return key
            presence = True
    if presence != True:
        return 'Нет такого номера'

def list_(docs):
    for document in docs:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')

def add(docs, dir):
    number = input('Введите номер документа: ')
    type = input('Введите тип документа: ')
    name = input('Введите имя владельца документа: ')
    directory = input('Введите номер папки: ')
    presence = bool
    docs.append({'type' : type, 'number' : number, 'name' : name})
    for key,value in dir.items():
        if directory == key:
            value.append(number)
            presence = True
    if presence != True:
        dir[directory] = [number]
        print(f'Такой папки не существует, документ добавлен в новую папку "{directory}"')
    return docs, dir

def delete(docs, dir):
    number = input('Введите номер документа: ')
    presence = bool
    for i in range(0, len(docs)):
        if number == docs[i]["number"]:
            presence = True
            del docs[i]
            break
    for key, values in dir.items():
        if number in values:
            values.remove(number)
            break
    if presence != True:
        print('Нет такого номера')
    return docs, dir

def move(dir):
    presence_number = bool
    presence_folder = bool
    number = input('Введите номер документа: ')
    for value in dir.values():
        if number in value:
            value.remove(number)
            presence_number = True
    folder = input('Введите номер папки: ')
    if presence_number == True:
        for key, value in dir.items():
            if key == folder:
                presence_folder = True
                value.append(number)
        if presence_folder != True:
            dir[folder] = [number]
            print(f'Такой папки не существует, документ добавлен в новую папку "{folder}"')
    else:
        print('Нет такого номера документа')

def add_shelf(dir):
    directory = input('Введите номер папки: ')
    if directory in dir:
        print('Такая папка существует!')
    else:
        dir[directory] = []
    return dir

def list_folders(dir):
    for key,value in dir.items():
        print(f'в Папке {key} находятся документы: {value}')

def main(docs,dir):
    while True:

        commands = {'p': people,
                    's': shelf,
                    'l': list_,
                    'a': add,
                    'd': delete,
                    'm': move,
                    'as': add_shelf,
                    'lf': list_folders,
                    'q': []}
        commands[input('Введите команду: ')]()
        break

main(documents,directories)

