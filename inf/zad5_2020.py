import sqlite3
from sql_tabclasses import Jezyk, Uzytkownicy, Panstwo

from zad4_1_2020 import  read_file,write_line
conn = sqlite3.connect("dataFile\zad5_2020.db") #create or connect
# conn = sqlite3.connect(':memory:') #for testing. Create new db every single running

c= conn.cursor()

#
# c.execute("""CREATE TABLE jezyki (
#             Jezyk text,
#             Rodzina text
#             )""") #use """ if you want a few lines
#
# c.execute("""CREATE TABLE uzytkownicy (
#             Panstwo text,
#             Jezyk text,
#             Uzytkownicy FLOAT,
#             Urzedowy text
#             )""") #use """ if you want a few lines


# c.execute("""CREATE TABLE panstwa (
#              Panstwo text,
#              Kontynent text,
#             Populacja FLOAT
#           )""") #use """ if you want a few lines
#
# conn.commit()

def insert_language(jezyk):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("INSERT INTO jezyki VALUES (:Jezyk,:Rodzina)",{'Jezyk': jezyk.jezyk,'Rodzina':jezyk.rodzina})#better
        # c.execute("INSERT INTO jezyki VALUES (?,?)",(jezyk1.jezyk,jezyk1.rodzina))

def insert_users(uzytkownik):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("INSERT INTO uzytkownicy VALUES (:Panstwo,:Jezyk,:Uzytkownicy,:Urzedowy)",{'Panstwo': uzytkownik.panstwo,'Jezyk': uzytkownik.jezyk,'Uzytkownicy':uzytkownik.uzytkownicy,'Urzedowy':uzytkownik.urzedowy})

def insert_countries(panstwo):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("INSERT INTO panstwa VALUES (:Panstwo,:Kontynent,:Populacja)",{'Panstwo': panstwo.panstwo,'Kontynent': panstwo.kontynent,'Populacja':panstwo.populacja})


def get_language_by_family(family):
    c.execute("SELECT * FROM jezyki WHERE Rodzina = ?", (family,))
    # c.execute("SELECT * FROM jezyki WHERE rodzina = :rodzina", {'rodzina':family})
    return c.fetchall()



def Add_familiy_to_db():
    inputData = read_file(file_name="jezyki.txt",sep= "\t")


    for [jezyk, rodzina] in inputData:
        if jezyk !="Jezyk":
            jezyk_obj = Jezyk(jezyk,rodzina.replace("\n",""))
            insert_language(jezyk_obj)


def Add_users_to_db():
    uzytkownicyData = read_file(file_name="uzytkownicy.txt", sep="\t")

    for [panstwo, jezyk, uzytkownicy, urzedowy] in uzytkownicyData:
        if panstwo != "Panstwo":
            uzytkownicy_obj = Uzytkownicy(panstwo, jezyk, uzytkownicy.replace(",", "."), urzedowy.replace("\n", ""))
            insert_users(uzytkownicy_obj)


def Add_countries_to_db():
    uzytkownicyData = read_file(file_name="panstwa.txt", sep="\t")

    for [panstwo, kontynent, populacja] in uzytkownicyData:
        if panstwo != "Panstwo":
            panstwo_obj = Panstwo(panstwo, kontynent, populacja.replace("\n", ""))
            insert_countries(panstwo_obj)

def zad5_1():
    # Add_familiy_to_db()
    # COUNT(jezyk) - total number of lanugage.
    # GROUP BY - create langugage groups for every familiy langiage
    # ORDER BY COUNT(jezyk) - set the smaller numbers of language first
    # DESC set descending
    write_line(text="\nzad5_1\n", file_path="wyniki5.txt")
    c.execute("""SELECT Rodzina, COUNT(Jezyk) FROM jezyki 
                GROUP BY  Rodzina ORDER BY COUNT(Jezyk) DESC""")
    for elment in c.fetchall():
        write_line(text = f"{elment[0]} {elment[1]}\n", file_path="wyniki5.txt")

def zad5_2():
    # Add_familiy_to_db()
    # Add_users_to_db()
    write_line(text="zad5_2\n", file_path="wyniki5.txt")
    # different  get only different values - not duplicate!
    c.execute("""SELECT COUNT(Jezyk) FROM (SELECT DISTINCT jezyk FROM uzytkownicy 
                WHERE Jezyk NOT IN 
                (SELECT Jezyk FROM uzytkownicy WHERE Urzedowy = :Urzedowy))""",
                {'Urzedowy':'tak'})
    write_line(text=f"{c.fetchall()[0]}\n", file_path="wyniki5.txt")

def zad5_3():
    # Add_familiy_to_db()
    # Add_users_to_db()
    write_line(text="zad5_3\n", file_path="wyniki5.txt")
    # different  get only different values - not duplicate!
    # INNER JOIN ON- connect two tables
    c.execute("""SELECT Jezyk FROM
        (SELECT * FROM uzytkownicy INNER JOIN 
        panstwa ON uzytkownicy.Panstwo = panstwa.Panstwo 
        GROUP BY kontynent,jezyk) 
        GROUP BY jezyk HAVING Count(*)>=4;
    """)
    for elment in c.fetchall():
        write_line(text = f"{elment[0]}\n", file_path="wyniki5.txt")

def zad5_4():
    # Add_familiy_to_db()
    # Add_users_to_db()
    write_line(text="zad5_4\n", file_path="wyniki5.txt")
    # different  get only different values - not duplicate!
    # INNER JOIN ON- connect two tables
    c.execute("""SELECT Jezyk, Rodzina, SUM(Uzytkownicy) as Total FROM
        (SELECT * FROM uzytkownicy 
        INNER JOIN panstwa ON uzytkownicy.Panstwo = panstwa.Panstwo 
        INNER JOIN jezyki ON uzytkownicy.Jezyk = jezyki.Jezyk
        ) 
        WHERE (Kontynent = :Kontynent1 OR Kontynent = :Kontynent2) AND Rodzina !=:Rodzina 
        GROUP BY Jezyk
        ORDER BY SUM(Uzytkownicy) DESC
        LIMIT 6;
    """, {'Kontynent1':"Ameryka Polnocna",'Kontynent2':"Ameryka Poludniowa", 'Rodzina':"indoeuropejska"})
    for elment in c.fetchall():
        write_line(text = f"{elment}\n", file_path="wyniki5.txt")

def zad5_5():
    # Add_familiy_to_db()
    # Add_users_to_db()
    write_line(text="zad5_5\n", file_path="wyniki5.txt")
    # different  get only different values - not duplicate!
    # ROUND zaokrąglij do 3 miejsca(2 parametr)
    c.execute("""SELECT Panstwo, Jezyk, ROUND(Uzytkownicy/Populacja * 100,3) as Procent FROM
        (SELECT * FROM uzytkownicy 
        INNER JOIN panstwa ON uzytkownicy.Panstwo = panstwa.Panstwo) 
        WHERE Urzedowy = :Urzedowy AND Procent>=30
        GROUP BY Jezyk
        ORDER BY Procent DESC;
    """, {'Urzedowy':"nie"})
    for elment in c.fetchall():
        write_line(text = f"{elment}\n", file_path="wyniki5.txt")


if __name__ == '__main__':
    zad5_1()
    zad5_2()
    zad5_3()
    zad5_4()
    zad5_5()
    conn.close()
