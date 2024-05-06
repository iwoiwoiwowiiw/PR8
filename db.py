import sqlite3

connection = sqlite3.connect("KarpovE217.db")
cursor = connection.cursor()


cursor.execute(
    '''CREATE TABLE IF NOT EXISTS _group(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL
    )''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    avatar TEXT,
    member_since DATE
    )''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS group_user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_group INTEGER,
    id_user INTEGER,
    balance REAL,
    FOREIGN KEY(id_group)  REFERENCES _group(id),
    FOREIGN KEY (id_user)  REFERENCES user(id)
    )''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS bill(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_group INTEGER,
    title TEXT,
    amount REAL,
    date DATE,
    created_by TEXT,
    FOREIGN KEY (id_group)  REFERENCES _group(id)
    )''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS bill_user_owes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_bill INTEGER,
    id_user INTEGER,
    owes TEXT,
    FOREIGN KEY(id_bill)  REFERENCES bill(id),
    FOREIGN KEY (id_user)  REFERENCES user(id)
    )''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS bill_user_paid(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_bill INTEGER,
    id_user INTEGER,
    paid TEXT,
    FOREIGN KEY(id_bill)  REFERENCES bill(id),
    FOREIGN KEY (id_user)  REFERENCES user(id)
    )''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS note(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_bill INTEGER,
    id_user INTEGER,
    message TEXT,
    created TEXT,
    FOREIGN KEY(id_bill)  REFERENCES bill(id),
    FOREIGN KEY (id_user)  REFERENCES user(id)
    )''')


flag = 1
menu = 10
print("choose table \n 1: group \n 2: user \n 3: group_user \n 4: bill \n 5: bill_user_owes \n 6: bill_user_paid \n"
      " 7: note \n 8: all data \n for separate table : 1+1 = 11. \n 0: exit")
while flag == 1:
    menu = int(input("Enter num: "))
    if menu == 0:
        break
    elif menu == 1:
        name = input("Enter name: ")
        balance = float(input("Enter balance: "))
        cursor.execute('''INSERT INTO _group (name, balance) 
                VALUES (?, ?)''', (name, balance))
    elif menu == 2:
        name = input("Enter name: ")
        email = input("Enter email: ")
        avatar = input("Enter avatar: ")
        member_since = input("Enter member_since: ")
        cursor.execute('''INSERT INTO user (name, email, avatar, member_since) 
                VALUES (?, ?, ?, ?)''', (name, email, avatar, member_since))
    elif menu == 3:
        id_group = input("Enter id_group: ")
        id_user = input("Enter id_user: ")
        balance = float(input("Enter balance: "))
        cursor.execute('''INSERT INTO group_user (id_group, id_user, balance) 
                VALUES (?, ?, ?)''', (id_group, id_user, balance))
    elif menu == 4:
        id_group = input("Enter id_group: ")
        title = input("Enter title: ")
        amount = input("Enter amount: ")
        date = input("Enter date: ")
        created_by = input("Enter created_by: ")
        cursor.execute('''INSERT INTO bill (id_group, title, amount, date, created_by) 
                VALUES (?, ?, ?, ?, ?)''', (id_group, title, amount, date, created_by))
    elif menu == 5:
        id_bill = input("Enter id_bill: ")
        id_user = input("Enter id_user: ")
        owes = input("Enter owes: ")
        cursor.execute('''INSERT INTO bill_user_owes (id_bill, id_user, owes) 
                VALUES (?, ?, ?)''', (id_bill, id_user, owes))
    elif menu == 6:
        id_bill = input("Enter id_bill: ")
        id_user = input("Enter id_user: ")
        paid = input("Enter paid: ")
        cursor.execute('''INSERT INTO bill_user_paid (id_bill, id_user, paid) 
                VALUES (?, ?, ?)''', (id_bill, id_user, paid))
    elif menu == 7:
        id_bill = input("Enter id_bill: ")
        id_user = input("Enter id_user: ")
        message = input("Enter message: ")
        created = input("Enter created: ")
        cursor.execute('''INSERT INTO note (id_bill, id_user, message, created) 
                VALUES (?, ?, ?, ?)''', (id_bill, id_user, message, created))
    elif menu == 8:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            print(f"Data from table {table_name}:")
            cursor.execute(f"SELECT * FROM {table_name};")
            data = cursor.fetchall()
            for row in data:
                print(row)
    elif menu == 11:
        cursor.execute("SELECT * FROM _group")
        data = cursor.fetchall()
        for row in data:
            print(row)
    elif menu == 22:
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        for row in data:
            print(row)
    elif menu == 33:
        cursor.execute("SELECT * FROM group_user")
        data = cursor.fetchall()
        for row in data:
            print(row)
    elif menu == 44:
        cursor.execute("SELECT * FROM bill")
        data = cursor.fetchall()
        for row in data:
            print(row)
    elif menu == 55:
        cursor.execute("SELECT * FROM bill_user_owes")
        data = cursor.fetchall()
        for row in data:
            print(row)
    elif menu == 66:
        cursor.execute("SELECT * FROM bill_user_paid")
        data = cursor.fetchall()
        for row in data:
            print(row)
    elif menu == 77:
        cursor.execute("SELECT * FROM note")
        data = cursor.fetchall()
        for row in data:
            print(row)
    else:
        print("n/a")


connection.commit()
connection.close()