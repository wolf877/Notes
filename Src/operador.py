import sqlite3

conn = sqlite3.connect("./database/database.sqlite")

cursor = conn.cursor()

# name = str(input('Name of Student '))

# try:
#     cursor.execute("SELECT AV1, AV2, AV3, AV4 FROM Class WHERE Aluno like '{0}'".format(name))
#     a = cursor.fetchall()
# except IndexError:
#     print("Could not find")

# T = a[0]
# a, b, c, d = T
# print(c)
cursor.execute("DROP TABLE Class_1")
# print(c)
cursor.execute("DROP TABLE ClassAvalutions")

conn.commit()
conn.close()