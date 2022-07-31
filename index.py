#! C:/Users/днс/AppData/Local/Programs/Python/Python38/python.exe

print("Content-Type: text/html\n")

with open('head.inc') as file:
    for line in file:
        print(line.rstrip())

print('<table class=\'tView1\'>')

import mysql.connector
myconn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', db = 'test', charset='utf8', use_unicode = True)
cur = myconn.cursor()
cur.execute("SET NAMES utf8;")
cur.execute("USE test;")

# обновление строки в БД
import os
query_string = os.environ['QUERY_STRING']
if query_string is not '':
    import urllib.parse
    urlGets = urllib.parse.parse_qs(query_string)
    if urlGets['textId']!='' and urlGets['textEd1']!='' and urlGets['textEd2']!='' and urlGets['textEd3']!='':
        textId=str(urlGets['textId']).replace('[\'','').replace('\']','')
        textEd1=str(urlGets['textEd1']).replace('[\'','').replace('\']','')
        textEd2=str(urlGets['textEd2']).replace('[\'','').replace('\']','')
        textEd3=str(urlGets['textEd3']).replace('[\'','').replace('\']','')
       # print(textId, textEd1, textEd2, textEd3)
        cur.execute("UPDATE myarttable SET text='"+textEd1+"', description='"+textEd2+"', keywords='"+textEd3+"' WHERE id = "+textId)    
        myconn.commit()
# конец обновления в БД

try: 
    cur.execute("SELECT * FROM myarttable WHERE id>14 ORDER BY id DESC;")
    result = cur.fetchall()
    for line in result:
        print('<tr>')
        iR=0
        for cell in line:
            sCellNew = str(str(cell).strip().encode('utf-8'), 'cp1251')
            sNewView = '<td><a href="#" class="js-open-modal" data-modal="1" id=\"id'+str(iR)+'_' + str(line[0]).strip() + '">' + sCellNew + '</a></td>'
            print(sNewView);
            iR+=1
        print('</tr>');
except: 
    myconn.rollback() 
 
myconn.close() 

print('</table>')

with open('foot.inc') as file:
    for line in file:
        print(line.rstrip())