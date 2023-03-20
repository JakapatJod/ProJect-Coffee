import pymysql
import time

loop_item = 'Y'
date = time.strftime('%d/%m/%Y')

con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
mycursor = con.cursor()

query = 'use userdata'
mycursor.execute(query)

sub_item = 0
while loop_item == 'Y':
    try:
        get_item_name = input("Input you cargo : ")
        query = 'select price from stock_main where coffee_name = %s;'
        mycursor.execute(query,(get_item_name))
        row = mycursor.fetchone()
        x = list(row)[0]

        try:
            get_item_many = int(input("how many you buy : "))
            sub_item_in = x*get_item_many
            sub_item += sub_item_in
            print('Current Spending Amouny',sub_item)
            loop_item = input("Want to buy another cargo Key Y : ")


        except:
            print("Erroe, Please Follow Instruction.")

    except:
        print('Invalid Input Please Check Cargo Name.')

        




print(sub_item)
# query = 'insert into expenses(all_employee_salary ,stock_salary , Date_for_pay) values(%s,%s,%s)'
# mycursor.execute(query,(1000,sub_item,date))



con.commit()
con.close() 