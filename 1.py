################################Добавление библиотек##################################################################################################################
import os # библиотека для удаление файла(именно в данном случае, а так большая библиотека для работы с функциями операционки)
import shutil# библиотека для копирования файлов
from tkinter import *# библиотека для создания интерфейса
from tkinter import Menu # класс для добавления меню в программу
from tkinter import ttk # класс для добавление вкладок в программу
from tkinter import scrolledtext # класс для добавление скорла (ввода данных вкладка обращения)
from tkinter import messagebox # класс для добавление всплывающих сообщений
from tkinter import filedialog # класс для создания диалоговых окон открытия и сохранения файлов
import string # класс предназначенный для обработки текстовой информации
import json # Основная цель JSON – передавать данные между клиентом и веб-сервером(тут используется для пакетного обмена и извлечения данных из файлов)
######################################################################################################################################################################
################################Добавление Функции чтоб испольщовать дальше в программе ##############################################################################
def clicked():  # обявляем функцию для кнопки (Подтвердить ввод)
    res = "Привет {}".format(txt1.get()) # get функция вывода введенного текста
    lbl1.configure(text=res) # Метод configure() используется для изменения атрибутов или параметров виджета в Tkinter
                             # text() в Python используется для извлечения текста из объекта
# Выход
def exit(): #обявляем функцию для кнопки закрыть
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?') # команда выводит соощения с тектом в отельном окне с вопросом да нет
    if answer: # в случии положительного ответа выполнит команду
        window.destroy()# команда закрытия приложения
# Открыть файл
def open_file():# упомянули выше
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))#запрос на открытие окна выбора
    if file_path: # что сделаем в случае выполнения команды
        txt5.delete('1.0', END) # удалит в виджете скорла вкладка обращения весь текст
        txt5.insert('1.0', open(file_path, encoding='utf-8').read()) # добавит из документа в скрол текст
# Сохранить файл
def save_file():# упомянули выше
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))# команда запускет окно выбора места сохранения файла
    f = open(file_path, 'w', encoding='utf-8') # команда открывает фаил и декодирует
    text = txt5.get('1.0', END) # команда выводит текст из файла
    f.write(text)# команда записывает текст из скрола в фаил
    f.close() # команда закрывает фаил
 # сохранения временного файла для обработчика текста
def save_file1():# упомянули выше
    f1 = open('preprocessed1.txt', 'w', encoding='utf-8') # команда открывает фаил и декодирует
    text = txt5.get('1.0', END) # команда выводит текст из файла
    f1.write(text)# упомянули выше
    f1.close() # упомянули выше
#эта функция предназначена для предварительной обработки текстового файла путем удаления знаков препинания и перевода в нижний регистр букв
#полученный результат записывает во временный фаил preprocess.txt
def cal_t2():
    import t2
    
#    shutil.copy2('test1.txt', 'dir2/test1.txt') #делает копию файла для проверки только


#   os.remove("test1.txt")# удаление временного файла
    
#######################################################################################################################################################################
#####################Создания окна программы###########################################################################################################################
window = Tk() # функция открытия окна
window.title("Программа отправки обращений в ведомства") # функция наименования окна программы
window.geometry('800x600') # определяем размер окна
#######################################################################################################################################################################
####################Создание меню для программы########################################################################################################################
menu = Menu(window)  # функция создания меню программы (тоесть создали переменную меню и привизали к нему функцию меню)
new_item = Menu(menu,tearoff=0 )  # создаем подпункт для меню (тоесть обявили функцию для переменной как до этого)
                                  #,tearoff=0 - отключвает отображение меню в отдельном окне
new_item.add_command(label='Создать новое обращение')  # присваиваем имя к нашему подпунту меню
new_item.add_command(label='Открыть', command=open_file)# упомянули выше
new_item.add_command(label='Сохранить', command=save_file)# упомянули выше
new_item.add_command(label='Закрыть', command=exit)# упомянули выше
menu.add_cascade(label='Файл', menu=new_item)  # присваеваем имя основному меню и делаем подпункты каскадом для выбора
                                                # можно добавлять пункты меню в любое меню с помощью функции add_cascade()
window.config(menu=menu) # само добавление меню в программу
#######################################################################################################################################################################
#########Добавление вкладок в программу################################################################################################################################
tab_control = ttk.Notebook(window)  # создаем элемент управления вкладкой, с помощью класса Notebook
tab1 = ttk.Frame(tab_control)  # создаем вкладку используя класс Frame
tab2 = ttk.Frame(tab_control)  # обьяснял выше
tab_control.add(tab1, text='Ввод Фио') # обьяснял выше 
tab_control.add(tab2, text='Текст обращения')  # обьяснял выше
tab_control.pack(expand=1, fill='both') #Запаковка элемента управления вкладкой, чтобы он стал видимым в окне
#######################################################################################################################################################################
##############################Тело программы вкладка ввод ФИО##########################################################################################################
lbl1 = Label(tab1, text="укажите вашу Фамилию", font=("Arial Bold", 10))  #класс Label — это виджет,
                                                 #который отображает текст в окне и служит в основном для информационных целей #tab 1(в какой вкладке отображать)
lbl1.grid(column=0, row=1) # функция grid определит место расположения текста
                          #column=0, row=0 кординаты на окне если просто(обезательно без нее текста не будет видно)
lbl2 = Label(tab1, text="укажите ваше Имя", font=("Arial Bold", 10))  # упомянули выше
lbl2.grid(column=0, row=2) # упомянули выше
lbl3 = Label(tab1, text="укажите ваше Отчество", font=("Arial Bold", 10))  # упомянули выше
lbl3.grid(column=0, row=3) # упомянули выше
lbl4 = Label(tab1, text="укажите ваш Номер телефона", font=("Arial Bold", 10)) # упомянули выше 
lbl4.grid(column=0, row=4) # упомянули выше

txt1 = Entry(tab1,width=20)  #Entry - функция которая вызывает пользовательский ввод
txt1.grid(column=2, row=1) # упомянули выше
# txt1.focus() #сразу предлагает вводить текст без наведения курсором
txt2 = Entry(tab1,width=20)  # упомянули выше
txt2.grid(column=2, row=2) # упомянули выше
txt3 = Entry(tab1,width=20)  # упомянули выше
txt3.grid(column=2, row=3) # упомянули выше
txt4 = Entry(tab1,width=20)  # упомянули выше
txt4.grid(column=2, row=4) # упомянули выше

btn = Button(tab1, text="Подтвердить ввод", bg="black", fg="red",command=clicked )   # функция Button создает кнопку на которую можно нажать
                                                                                    #command=clicked запуск функции которую обьявляли в начале
btn.grid(column=3, row=4)  # упомянули выше
#######################################################################################################################################################################
##############################Тело программы вкладка Обращение#########################################################################################################
txt5 = scrolledtext.ScrolledText(tab2, width=40, height=10) # Создание скрокла с определением размеров
txt5.grid(column=0, row=0)# упомянули выше
btn1 = Button(tab2, text="сохранение текста для обработки", bg="black", fg="red",command=save_file1 )  # обьяснял выше
btn1.grid(column=3, row=4)  # упомянули выше
btn2 = Button(tab2, text="запуск обработки текста", bg="black", fg="red",command=cal_t2)  # обьяснял выше
btn2.grid(column=4, row=4)  # упомянули выше


#######################################################################################################################################################################
#######################################################################################################################################################################
window.mainloop() # функция вызывает бесконечный цикл окна, поэтому окно будет ждать любого взаимодействия с пользователем, пока не будет закрыто.
#######################################################################################################################################################################