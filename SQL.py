import sqlite3

conn = sqlite3.connect('table_text.db')

conn = sqlite3.connect('table_num.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS table_text(id INTEGER PRIMARY KEY, col_1 TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS table_num(id INTEGER PRIMARY KEY, col_1 INT)''')


a = [1, 2, 3, 4, "one", "two", "three", "four"]

text = []
num = []

for i in a:
    if type(i) is str:
        text.append(i)
        n = len(i)
        num.append(n)

    elif type(i) is int:
        if int(i) % 2 == 0:
            num.append(i)
        else:
            text.append("odd")


cursor.execute('''INSERT INTO table_text(col_1) VALUES (?)''', (text, ))
cursor.execute('''INSERT INTO table_num(col_1) VALUES (?)''', (num, ))


if len(num) < 5:
    cursor.execute('''UPDATE table_text SET col_1="hello" WHERE id=1''')
elif len(num) > 5:
    cursor.execute('''DELETE from table_text WHERE id=1''')

query = cursor.fetchall()
print(query)






