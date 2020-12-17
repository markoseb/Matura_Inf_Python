import sqlite3
from sql_tabclasses import Statek

from zad4_1_2020 import  read_file,write_line
conn = sqlite3.connect("dataFile\zad6_2020.db") #create or connect
# conn = sqlite3.connect(':memory:') #for testing. Create new db every single running

c= conn.cursor()


# c.execute("""CREATE TABLE statek (
#     data DATE,
#     port TEXT,
#     towar TEXT,
#     zw TEXT,
#     ile_ton INT,
#     cena_tona INT
#             )""") #use """ if you want a few lines
#
# conn.commit()

def insert_ship(statek):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("INSERT INTO statek VALUES (:DATE,:Port,:Towar,:ZW,:Ile_ton,:Cena_tona)",
                  {'DATE': statek.data,'Port':statek.port,'Towar': statek.towar,'ZW': statek.zw,'Ile_ton': statek.ile_ton,'Cena_tona': statek.cena_tona})

def Add_ship_to_db():
    inputData = read_file(file_name="statek.txt",sep= "\t")

    for [data, port, towar, zw,ile_ton,cena_tona] in inputData:
        if data !="data":
            statek= Statek(data,port, towar, zw,ile_ton,cena_tona.replace("\n",""))
            insert_ship(statek)



def zad6_1():

    write_line(text="zad6_1\n", file_path="wyniki6.txt")

    c.execute("""SELECT Towar, SUM(Ile_ton) as Calkowita_masa FROM statek
        WHERE ZW = :ZW
        GROUP BY Towar
        ORDER BY COUNT(Towar) DESC
        LIMIT 1;
    """, {'ZW':"Z"})
    for elment in c.fetchall():
        write_line(text = f"{elment}\n", file_path="wyniki6.txt")

if __name__ == '__main__':
    zad6_1()
    conn.close()
