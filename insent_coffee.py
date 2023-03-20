import pymysql
import random
import time

x = random.randint(100,1000)
billnumber = 'Cake'

sub = 80

date = '65'


con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
mycursor = con.cursor()

query = 'use userdata'
mycursor.execute(query)

query = 'insert into stock_main(coffee_name ,quantity , price) values(%s,%s,%s)'
mycursor.execute(query,(billnumber,date,sub))
con.commit()
con.close() 