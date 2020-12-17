class Jezyk:
    jezyk = ""
    rodzina = ""
    def __init__(self,jezyk, rodzina):
        self.jezyk = jezyk
        self.rodzina= rodzina


class Uzytkownicy:
    panstwo = ""
    jezyk = ""
    uzytkownicy = 0
    urzedowy = "NIE"
    def __init__(self,panstwo,jezyk, uzytkownicy,urzedowy):
        self.panstwo = panstwo
        self.jezyk= jezyk
        self.uzytkownicy = uzytkownicy
        self.urzedowy = urzedowy

class Panstwo:
    panstwo = ""
    kontynent = ""
    populacja = 0
    def __init__(self,panstwo,kontynent, populacja):
        self.panstwo = panstwo
        self.kontynent= kontynent
        self.populacja = populacja

class Statek:
    data = ""
    port = ""
    towar = ""
    zw= ""
    ile_ton= ""
    cena_tona = 0
    def __init__(self,data,port, towar, zw,ile_ton,cena_tona):
        self.data = data
        self.port = port
        self.towar = towar
        self.zw = zw
        self.ile_ton = ile_ton
        self.cena_tona = cena_tona


