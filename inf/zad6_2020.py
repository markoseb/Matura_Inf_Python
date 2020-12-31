import sqlite3
from sql_tabclasses import Statek
import datetime
import calendar
from dateutil.relativedelta import relativedelta
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

def zad6_2():

    write_line(text="zad6_2\n", file_path="wyniki6.txt")

    c.execute("""SELECT data, ZW, port FROM statek
        GROUP BY data
        ORDER BY data
    """)
    date= datetime.date.today()
    i=0
    for elment in c.fetchall():
        if date != datetime.date.today():
            if (datetime.datetime.strptime(elment[0], '%Y-%m-%d').date()-date).days >21:#pełne dni. Nie liczymy dnia wypłynięcia i wpłynięcia
                i+=1
        date =datetime.datetime.strptime(elment[0], '%Y-%m-%d').date()

    write_line(text = f"Liczba kursow {i}\n", file_path="wyniki6.txt")


def zad6_3(file ="wyniki6.txt"):

    write_line(text="zad6_3\n", file_path=file)

    date_tab=["2016-02-01","2018-08-01"]
    for date in date_tab:
        c.execute("""SELECT data, Towar, 
            SUM(CASE When ZW = :Z Then Ile_ton Else 0 End) -
            SUM(CASE When ZW = :W Then Ile_ton Else 0 End) as Suma
            FROM statek
            WHERE data < :data1
            GROUP BY Towar
            ORDER BY Suma;
        """, {'data1': date, "Z": "Z", "W": "W"})
        towar_list= c.fetchall()
        write_line(text = f"MAX : {towar_list[-1]}\nMIN : {towar_list[0]}\n", file_path=file)


def zad6_4(file ="wyniki6.txt"):

    write_line(text="zad6_4\n", file_path=file)
    write_line(text=f"Miesiac   Zaladunek Wyladunek", file_path=file)
    d = datetime.date(2016, 1, 1)
    while d <datetime.date(2018, 12, 18):

        c.execute("""SELECT
                   SUM(CASE When ZW = :Z Then Ile_ton Else 0 End) as ZZ,
                   SUM(CASE When ZW = :W Then Ile_ton Else 0 End) as WW
                   FROM statek
                   WHERE Towar = :T5 AND data<:date2 AND data>=:date1
               """, {'T5': "T5", "date1": d,"date2": d+relativedelta(months=+1),
                     "Z":"Z","W":"W"})
        towar_list = c.fetchall()[0]
        write_line(text=f"{d.year}-{d.month}    {towar_list[0]}    {towar_list[1]}", file_path=file)
        d = d+relativedelta(months=+1)

def zad6_5(file ="wyniki6.txt"):

    write_line(text="\nzad6_5\n", file_path=file)

    c.execute("""SELECT data,ZW,                
                SUM(CASE When ZW = :Z Then money Else 0 End) as ZZ,
                SUM(CASE When ZW = :W Then money Else 0 End) as WW
                FROM (SELECT data, ZW, cena_tona*Ile_ton as money FROM statek)
                GROUP BY data
               """,{"Z":"Z","W":"W"})
    Total = 500000
    max_saldo={"date":"","saldo":0,"min":500000}
    for towar_list in  c.fetchall():
        # write_line(text=f"{towar_list[0]}   {towar_list[1]} {towar_list[2]} {towar_list[3]}", file_path=file)
        Total = Total -towar_list[2] +towar_list[3]
        if Total < max_saldo["min"]:
            max_saldo["min"] = Total
        if Total > max_saldo["saldo"]:
            max_saldo["date"] = towar_list[0]
            max_saldo["saldo"] = Total

    text=f"""a)\nStan kasy na 18.12.2018: {Total}
Max stan kasy dnia: {max_saldo['date']}
f"Max stan {max_saldo['saldo']}
b)\nMinimum talarow  {500000 - max_saldo['min']}"""

    write_line(text=text, file_path=file)




if __name__ == '__main__':
    conn.close()
