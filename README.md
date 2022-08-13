# practPython 
Это - исходники учебного web-сайта на Python. Пример web-сайта, как можно редактировать строки в таблице из базы данных MySQL с применением языка Python.
Главная страница web-сайта представлена далее, которая представляет собой список из колонок и строк для редактирования:

![scr1](https://user-images.githubusercontent.com/10297748/184474152-c0211202-ca8b-4194-9a3f-010b499bb135.png)


Для создания базы данных необходимо воспользоваться скриптом test.sql из каталога [practUpdate](https://github.com/alex1543/practUpdate)
или программой [ExLzFmySQL](https://github.com/alex1543/ExLzFmySQL) на Lazarus.

При нажатии на ячейку в строке, предлагается редактировать три параметра:

![scr2](https://user-images.githubusercontent.com/10297748/184474156-aba1c1a1-1dce-4cd6-b574-60eabd133d90.png)


Web-сайт гаранированно работает в XAMPP Version 7.4.27 с подключенным Python 3.8.

Для подключения интерпретатора Python к web-серверу Apache, необходимо найти секцию < IfModule mime_module > в файле httpd.conf и добавить две строки:
  
  AddHandler cgi-script .py
  
  ScriptInterpreterSource Registry-Strict
  
Найти блок < IfModule dir_modul e> ... < /IfModule > и добавить названия файлов: index.py, default.py, home.py
  
Затем исправить первую строку в файле index.py из каталога с исходниками на путь к программе Python. Например, так:
  
  #! C:/Users/днс/AppData/Local/Programs/Python/Python38/python.exe

После установки Python 3.8, необходимо установить mysql.connector с помощью команды: pip install mysql.connector
  
  
