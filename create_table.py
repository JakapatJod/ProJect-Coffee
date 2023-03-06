import pymysql

try:
    con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
    mycursor = con.cursor()

except:
    print('Error','Database Connectivity Issue, Please check You Password Or User And Try Again')

try:
    query = 'use userdata'
    mycursor.execute(query)

except:
    print('Error',"Don't Have Database")

try:
    query = 'Create table stock_main(goods_id int auto_increment key not null ,coffee_name varchar(50) ,quantity int(100) ,price int(100))'
    mycursor.execute(query)

except:
    try:
        query = 'Create table sale(sales_id int auto_increment key not null ,username varchar(50) ,Date_for_sales varchar(100))'
        mycursor.execute(query)

    except:
        try:
            query = 'Create table details_of_sale(detail_id int auto_increment key not null ,total_sales varchar(100))'
            mycursor.execute(query)
        
        except:
            try:
                query = 'Create table expenses(expenses_id int auto_increment key not null ,all_employee_salary varchar(50) ,Date_for_pay varchar(100))'
                mycursor.execute(query)
            
            except:
                print('Error','You Already Create This Table')
