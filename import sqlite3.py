import sqlite3

# Connect to the database
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# Create the table (run only once)
# cur.execute("CREATE TABLE movie(title TEXT, year INTEGER, score INTEGER)")

# Menu
print('1- Add data \n2- Delete data \n3- See data \n4- Close')
decision = input('Write the number of the option you want to execute: ')

while (decision != '4'):
    # Add data
    if decision == "1":
        title = input('Title: ')
        year = int(input('Year: '))
        score = int(input('Score: '))
        
        cur.execute("INSERT INTO movie VALUES (?, ?, ?)", (title, year, score))
        con.commit()
        print("Movie added!")

    # Show all data
    res = cur.execute("SELECT * FROM movie")
    rows = res.fetchall()
    for row in rows:
        print(row)
else:
    print('Thank you!')

con.close()
