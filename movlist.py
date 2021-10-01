import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",passwd="eva@k2001",database="movierecord")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE MOV_LIST(Name VARCHAR(30),Actor VARCHAR(30),Actress VARCHAR(30),Director VARCHAR(30),Year_of_release INT NOT NULL,PRIMARY KEY(Name))")
sql = "INSERT INTO MOV_LIST (Name, Actor, Actress,Director,Year_of_release) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Titanic','James Cameron','Leonardo DiCaprio','Kate Winslet',1997),
  ('Twilight',' Catherine Hardwicke','Robert Pattinso','Kristen Stewart',2008),
  ('The Parent Trap',' Nancy Meyers','Dennis Quaid','Lindsay Lohan',1998),
  ('The Holiday',' Nancy Meyers','Jude Law','Kate Winslet',2014),
  ('The Last Letter from Your Lover','Augustine Frizzell','Callum Turner','Shailene Woodley',2021),
  ('Gladiator','Ridley Scott','Russell Crowe','Connie Nielsen',2000),
  ('Cast Away','Robert Zemeckis','Tom Hanks','Helen Hunt',2000),
  ('Robin Hood','Ridley Scott','Russell Crowe','Cate Blanchet',2005)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Contents inserted.")
mycursor.execute(" SELECT * FROM MOV_LIST")
for i in mycursor:
    print(i)
mycursor.execute("SELECT Name,Actor FROM MOV_LIST ORDER BY Actor")
for j in mycursor:
    print(j)
mydb.close()