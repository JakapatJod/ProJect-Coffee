import pymysql

list_row = []

con = pymysql.connect(host = "localhost" ,user = "root" ,password = "Bunnapon122")
mycursor = con.cursor()

query = 'use userdata'
mycursor.execute(query)

query = 'select price from stock_main ;'
mycursor.execute(query)
row = mycursor.fetchall()
for i in row:
    list_row.append(i[0])

s1 = list_row[0] ; s2 = list_row[1] ; s3 = list_row[2] ; s4 = list_row[3] ; s5 = list_row[4] ; s6 = list_row[5] ; s7 = list_row[6]; s8 = list_row[7] ; s9 = list_row[8] ; s10 = list_row[9] ; s11 = list_row[10] ; s12 = list_row[11];  s13 = list_row[12];  s14 = list_row[13];  s15= list_row[14]; s16 = list_row[15] ; s17 = list_row[16] ; s18 = list_row[17]

print(s12)



