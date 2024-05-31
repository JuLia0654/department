import string # класс предназначенный для обработки текстовой информации
import json # Основная цель JSON – передавать данные между клиентом и веб-сервером(тут используется для пакетного обмена и извлечения данных из файлов)
#эта функция предназначена для предварительной обработки текстового файла путем удаления знаков препинания и перевода в нижний регистр букв
#полученный результат записывает во временный фаил preprocess.txt
def preprocess(file):
    with open(file, 'r') as fileData:
        for textline in fileData:
            #разделяем слова на буквы
            wordsList = textline.split()
            x = [''.join(c for c in s if c not in string.punctuation) for s in wordsList]
            x = [x.lower() for x in x]
            y = " ".join(x)
            fila = open(prefile, "a")
            fila.write(y+"\n")
#эта функция отчистки текста с файла            
def cleartxt():
    f = open(prefile, "w")
    f.write("")
filename = 'preprocessed1.txt' # переменная для ссылки на фаил
prefile = 'preprocessed.txt' # переменная для ссылки на фаил
preprocess(filename)
dictionary = {} #переменная для подсчета(текст ключ функция)
with open(prefile, "r") as f:
    words = f.read().split()
    words = list(words)
    words = sorted(words)
    for x in words:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
print(open(filename, "r").read(),'\n') # отображает обрабатываемый текст
print("--- результат обработки ---\n",dictionary) # отображает результат обработки текста
with open('wordfreq.txt', 'w') as convert_file: #открыть испоняемый фаил и расшифровать его
     convert_file.write(json.dumps(dictionary)) # применения функции рсшифровки исползуемого ранее текста и ключа
ma = (max(dictionary, key=dictionary.get)) # проверяем максимально повторяющее слово

var = ma
with open('file.txt') as fr:
    lines = [_.replace('\n', '') for _ in fr.readlines()]  # прочитать файл построчно в списке file.txt для сопостовления
    print('\n'.join([str((var == val)) for val in lines]))


#var = ma
#with open('file.txt') as fr:
#    lines = [_.replace('\n', '') for _ in fr.readlines()]  # прочитать файл построчно в списке file.txt для сопостовления
#    print('\n'.join([str((var == val)) for val in lines]))
#print(">>>>вывод жалобы на<<<<\n",ma) # вывод текста самого повторяющего слова
cleartxt()






