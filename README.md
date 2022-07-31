# practPython (исходники учебного web-сайта на Python)
Пример web-сайта, как можно редактировать строки в таблице из базы данных MySQL с применением языка Python

Главная страница web-сайта представлена, далее.

Представляет собой список из колонок и строк для редактирования:

![image](https://user-images.githubusercontent.com/10297748/182027613-77cd33d7-885b-4470-846a-df76831ebc27.png)

Для создания базы данных необходимо воспользоваться скриптом test.sql из каталога [practUpdate](https://github.com/alex1543/practUpdate)
или программой [ExLzFmySQL](https://github.com/alex1543/ExLzFmySQL) на Lazarus.

При нажатии на ячейку в строке, предлагается редактировать три параметра:

![image](https://user-images.githubusercontent.com/10297748/182027711-fe75c50d-edac-44a9-ae4a-025eb2d17ed4.png)

Web-сайт гаранированно работает в XAMPP Version 7.4.27 с подключенным Python 3.8.

Для подключения интерпретатора Python к web-серверу Apache, необходимо найти секцию <IfModule mime_module> в файле httpd.conf и добавить две строки:
  
  AddHandler cgi-script .py
  
  ScriptInterpreterSource Registry-Strict
  
Затем исправить первую строку в файле index.py из каталога с исходниками на путь к программе Python. Например, так:
  
  #! C:/Users/днс/AppData/Local/Programs/Python/Python38/python.exe

После установки Python 3.8, необходимо установить mysql.connector с помощью команды: pip install mysql.connector
  
  
