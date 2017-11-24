#!/usr/bin/python3
import PyMySQL
# Setup MySQL Conection
db = mariadb.connect(user='root', password='0095', database='python')
cursor = db.cursor()

# Insert a row into our table
cursor.execute("INSERT INTO users (firstname) VALUES ('kyle')")

# Save changes to database
db.commit()

#originally I was using just python along the top and the code wouldn't work
#had to add in the "3" after it and then it was fine following tutorial from
#https://blog.udacity.com/2015/03/write-your-first-python-application.html
#was doing this on Solus but mysql is not in the repo tried mariadb
#but i need the MYSQL-python 1.2.5 package which I can't get
#i'll have to boot into Ubuntu and install MySQL or Mariadb
#when installing mariadb it never asked for a root password so I had to google
#how to reset it. Answer found here:
#https://stackoverflow.com/questions/30815971/mariadb-installed-without-password-prompt
def checkName(name):
    checkName = input("Is your name " + name + "? ")

    if checkName.lower() == "yes":
        print ("Hello,", name)
    else:
       name = input("we're sorry about that, what's ur name?")
       print ("welcome,",name)

checkName("yes")
