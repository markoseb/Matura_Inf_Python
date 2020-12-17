import sqlite3
from sql_tabclasses import Jezyk
# conn = sqlite3.connect("dataFile\employe.db") #create or connect
conn = sqlite3.connect(':memory:') #for testing. Create new db every single running

c= conn.cursor()

c.execute("""CREATE TABLE jezyki (
            jezyk text,
            rodzina text
            )""") #use """ if you want a few lines


c.execute("INSERT INTO jezyki VALUES ('Mark', 'Ch')")
conn.commit()

def insert_language(jezyk):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("INSERT INTO jezyki VALUES (:jezyk,:rodzina)",{'jezyk': jezyk.jezyk,'rodzina':jezyk.rodzina})#better
        # c.execute("INSERT INTO jezyki VALUES (?,?)",(jezyk1.jezyk,jezyk1.rodzina))

def get_language_by_family(family):
    # c.execute("SELECT * FROM jezyki WHERE rodzina = ?", (family,))
    c.execute("SELECT * FROM jezyki WHERE rodzina = :rodzina", {'rodzina':family})
    return c.fetchall()

def updatte_language(jezyk,parm):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("""UPDATE jezyki SET rodzina=:parm WHERE jezyk=:jezyk
        """,{'jezyk': jezyk.jezyk,'parm':parm})#better


def remove_language(jezyk):
    with conn:#commit, rewrite automatically, simmilar like file using
        c.execute("""DELETE from jezyki WHERE jezyk=:jezyk AND rodzina=:rodzina,
        """,{'jezyk': jezyk.jezyk,'rodzina' : jezyk.rodzina})#better


jezyk1 = Jezyk("AAA","Dupa")

insert_language(jezyk1)

l=get_language_by_family('Dupa1')
print (l)

conn.close()