import sqlite3

conn = sqlite3.connect("./database/database.sqlite")

cursor = conn.cursor()
while True:
    try:
        Number = int(input('Number '))
        break
    except ValueError:
        print('Enter with a valide number')

def CreateDatabase(Number):
    i = 1
    sql ='''CREATE TABLE Class(
            Aluno VARCHAR NOT NULL,'''

    while i <= Number:
        if i == Number:
            sql += '''AV{0} FLOAT
            )'''.format(i)
        else:
            sql += ''' AV{0} FLOAT,'''.format(i)
        i += 1
    cursor.execute(sql)

def RegisterStudent(Number):
    #Student = int(input('Student'))
    #Number_avs = int(input('Number'))
    sql = '''INSERT INTO Class(
        Aluno, '''
    i = 1 
    while i <= Number:
        if i == Number:
            sql += '''AV{0}) VALUES 
            ('''.format(i)
        else:
            sql += '''AV{0}, '''.format(i)
        i += 1
    #j = 1
    y = 1

    nome = str(input('Name of Student '))
    sql += "'{0}', ".format(nome)
    while y <= Number:
        try:
             N = float(input('Note '))
        except ValueError:
            N = "NULL"
        if y == Number:
            sql += '{0})'.format(N)
        else:
            sql += '{0}, '.format(N)
        y += 1

    cursor.execute(sql)
    conn.commit()

        
    # sql = '''INSERT INTO Class(
    #         Aluno, AV1, AV2, AV3, AV4) VALUES 
    #         ('Ramya', 10, 8, NULL, 9)'''
    #cursor.execute(sql)
    #print(sql)

while True:
    try:
        Number = int(input('Number '))
        break
    except ValueError:
        print('Enter with a valide number')

Exist = cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Class'")

if Exist.fetchone()[0] == 1:
    print("Already exist")
else:
    CreateDatabase(Number)
    print("CreateDatabase")

while True:
    RegisterStudent(Number)

    while True:
        Again = str(input("Register more? "))
        if Again =='Yes' or Again == 'yes':
            break
        elif Again =='No' or Again == 'no':
             break
        else:
            continue

    if Again =='Yes' or Again == 'yes':
        continue
    elif Again =='No' or Again == 'no':
        print("Good bye!")
        break


#cursor.execute('DROP TABLE Class;')
# sql ='''CREATE TABLE Class(
#             NAME VARCHAR NOT NULL,
#    AV1 FLOAT, AV2 FLOAT,
#    AV3 FLOAT,
#    AV4 FLOAT
# )'''
# cursor.execute(sql)

# Exist = cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Class'")

# if Exist.fetchone()[0] == 1:
#     print(Exist)
#conn.commit()
conn.close()

print("works")