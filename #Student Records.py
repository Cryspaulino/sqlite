#Student Records
import sqlite3

# Connect to the database
con = sqlite3.connect("students.db")
cur = con.cursor()

# # Create the table (run only once)
cur.execute("CREATE TABLE IF NOT EXISTS personalinfo(stid TEXT, name TEXT, birthday TEXT, email TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS schoolinfo(stid TEXT, name TEXT, major TEXT, year TEXT, grade FLOAT)")

while True:

    # Menu
    menu = print('1- Add data \n2- Update data \n3- See data \n4- Create table \n5- Delete table \n6- Close')
    decision = input('Write the number of the option you want to execute: ')

    if decision == "1":
            stid = input('Student ID: ')
            name = input('Name: ')
            birthday = input('Birth Date (MM-DD-YYYY): ')
            email = input('Email (byui.edu): ')
            
            cur.execute("INSERT INTO personalinfo VALUES (?, ?, ?, ?)", (stid, name, birthday, email))
            con.commit()

            major = input('Major: ')
            year = input('Freshman, Sophomore, Junior or Senior: ')
            grade = float(input('Grade (x.x): '))
            
            cur.execute("INSERT INTO schoolinfo VALUES (?, ?, ?, ?, ?)", (stid, name, major, year, grade))
            con.commit()
            print("Student information added!")
    
    elif decision == '2':
            updatefield = input('Which field do you want to update: \n1- Name \n2- Birth Date \n3- Email \n4- Major \n5- Year \n6- Grade \n')
            if updatefield == '1':
                  new_name = input('Enter the new name: ')
                  cur.execute("UPDATE personalinfo SET name = ? WHERE name = ?", (new_name, name))
                  print('The name has been updated.')



    elif decision == '3':
            #        # See personalinfo
            #     print("\n--- Personal Info ---")
            #     cur.execute("SELECT * FROM personalinfo")
            #     for row in cur.fetchall():
            #         print(row)

            # # See schoolinfo
            #     print("\n--- School Info ---")
            #     cur.execute("SELECT * FROM schoolinfo")
            #     for row in cur.fetchall():
            #        print(row)

            #    cur.execute("""SELECT * FROM personalinfo
            #     JOIN schoolinfo ON personalinfo.name = schoolinfo.name
            #     """)
            #    rows = cur.fetchall()
            #    for row in rows:
            #           print(row)



            # IF THE TABLE EXISTS THEN DO THIS

            cur.execute("""
            SELECT personalinfo.stid, personalinfo.name, birthday, email, major, year, grade
            FROM personalinfo
            JOIN schoolinfo ON personalinfo.stid = schoolinfo.stid
            """)
            rows = cur.fetchall()

            # Format output nicely
            print(f"{'Student ID':<10}  {'Name':<15}  {'Birth Date':<13}  {'Email':<21}  {'Major':<16}  {'Year':<11}  {'Grade':<5} ")
            for stid, name, birthday, email, major, year, grade in rows:
                print(f"{stid:<10} | {name:<15} | {birthday:<12} | {email:<20} | {major:<15} | {year:<10} | {grade:<4}")
        


    elif decision == '5':
            tablename = input('What table do you want to delete? ')
            todelete = input(f'Are you sure you want to DELETE the {tablename} table? ')
            if todelete == 'Yes':
                cur.execute(f"DROP TABLE IF EXISTS {tablename}")
            # else:
            #     print(menu)

    elif decision == '6':
        print("Thanks!")
        break

    else:
         print('This is not one of our options. Please select again.')









