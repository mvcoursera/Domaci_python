#zad1##########################
tekst=input("Unesi tekst: ")
char=input("Unesi karakter: ")
def get_words_ends_with_letter(tekst,char):
  lista=[]
  d=len(tekst)
  num_of_dots = tekst.count(".")
  pom_list=[]
  pom_list=tekst.split(".")
  pom_list1=[]
  for i in range(num_of_dots):
    pom_list1 = pom_list[i].split(" ")
    br=0
    for j in range(len(pom_list1)):
      if pom_list1[j].endswith(char):
        lista.append(pom_list1[j])
        br+=1
    lista.append(br)
    
  return(lista)

print(get_words_ends_with_letter(tekst,char))


#zad2##############################
lista=[]
n=int(input("Unesite broj elemenata liste: "))
for _i in range(n):
  el=int(input("Unesite element liste: "))
  lista.append(el)

def proizvod_sekv(lista):
  max_br=0
  max_lista=[]
  pom_lista=[]
  pom_lista.append(lista[0])
  br=1
  for i in range(0,n-1):
    if lista[i]==lista[i+1]:
      br+=1
      pom_lista.append(lista[i+1])
      if br>=max_br:
        max_br=br
        max_lista=pom_lista
    else:
        br=1
        pom_lista=[]
        pom_lista.append(lista[i+1])
  print(max_lista)
  
  proizvod=1
  for j in range(max_br):
    proizvod = proizvod * max_lista[j]
    
  return proizvod

print(proizvod_sekv(lista))



#zad3#############################
niz=[1,2,4,5,6,2,3,2,4,5]
n=len(niz)
def testerasti_podniz(lista):
  podniz = []
  br = 1
  i = 1
  max_br = 0
  max_podniz = []
  podniz.append(lista[0])
  while i < n - 1:
    if lista[i - 1] < lista[i]:
      podniz.append(lista[i])
      br += 1
      if br >= max_br:
        max_br = br
        max_podniz = podniz
      if lista[i] > lista[i + 1]:
        br += 1
        podniz.append(lista[i + 1])
        print(max_podniz)
        if br >= max_br:
          max_br = br
          max_podniz = podniz
        i+=2
      else:
        br=2
        podniz=[]
        podniz.append(lista[i])
        i+=1
    else:
      br = 1
      podniz = []
      podniz.append(lista[i + 1])
      print(podniz)
      i += 2

  return max_podniz


print(testerasti_podniz(niz))




#zad4#######################################
string = 'aabaaacc'
n=len(string)

def ponavljanje(string):
  brojac=1
  pom_br=1
  char=string[0]
  char_pom=''
  for i in range(n-1):
    if string[i] == string[i+1]:
      brojac+=1
      char+=string[i+1]
      if pom_br<=brojac:
        pom_br=brojac
        char_pom=''
        char_pom+=char
    else:
      brojac=1
      char=""
      char+=string[i+1]
      
      
  print(char_pom) 
  return pom_br

print(ponavljanje(string))


#zad5###########################
podcast = [
  { 'naziv': 'Español para principiantes', 'br_pozitivni': 1000, 'br_negativni': 10},
  {'naziv': 'Philophize This!', 'br_pozitivni': 500, 'br_negativni': 30}, 
  {'naziv': 'Science VS.', 'br_pozitivni': 600, 'br_negativni': 45}]

def najgori_odnos(podcast):
  broj_poz=0
  broj_neg=0
  rez=0
  pom_rez=round(podcast[0]['br_pozitivni']/podcast[0]['br_negativni'],2)
  pom_naziv={}
  for i in podcast:
    broj_poz=i['br_pozitivni']
    broj_neg=i['br_negativni']
    rez=round(broj_poz/broj_neg,2)
    print(rez)
    if pom_rez>=rez:
      pom_rez=rez
      pom_naziv=i['naziv']
  print(pom_naziv)
  return pom_rez

print(najgori_odnos(podcast))



#zad6######################################
class Televizor():
  def __init__( self, _broj_kanala, _naziv_kanala, _kanali, _jacina_tona):
    self._broj_kanala=0
    self._naziv_kanala=""
    self._kanali=[]
    self._jacina_tona=0

  def get_broj_kanala(self):
    return self._broj_kanala

  def set_broj_kanala(self,broj_kanala):
    if broj_kanala>=0 and broj_kanala<len(self._kanali):
      self._broj_kanala=broj_kanala
    else:
      print("Nepostojeci kanal!")

  def get_naziv_kanala(self):
    return self._naziv_kanala

  def set_naziv_kanala(self,naziv_kanala):
    self._naziv_kanala=naziv_kanala

  def get_kanali(self):
    return self._kanali
  
  def get_jacina_tona(self):
    return self._jacina_tona

  def dodaj_kanal(self,naziv_kanala):
    self._kanali.append(naziv_kanala)

  def obriši_kanal(self,naziv_kanala):
    if naziv_kanala in self._kanali:
      self._kanali.remove(naziv_kanala)
    else:
      print("Nepostojeci kanal.")

  def uvecaj_ton(self):
    if self._jacina_tona<10:
      self._jacina_tona+=1
    else:
      print("Ne moze se vise pojacati ton!")

  def ime_kanala(self,broj_kanala):
    if self._broj_kanala>=1 and self._broj_kanala<len(self._kanali):
      return self._kanali[broj_kanala-1]
    else:
      print("Kanal ne postoji..")

tv=Televizor(0,"",["Prvi","Drugi"],0)
tv.dodaj_kanal("Treci")
tv.set_broj_kanala(1)
tv.set_naziv_kanala("Novi kanal")
tv.uvecaj_ton()
print(tv.get_naziv_kanala())
print(tv.get_jacina_tona())
print(tv.get_kanali())



#zad7##########################################
class Book():
  def __init__(self, naslov, autor, god_izdavanja, br_kopija):
    self.naslov= naslov
    self.autor=autor
    self.god_izdavanja=god_izdavanja
    self.br_kopija=br_kopija
  
  def __repr__(self): #reprezentacija objekta
    return f"Naslov knjige: {self.naslov}, Autor: {self.autor},	Godina izdavanja: {self.god_izdavanja}, Broj kopija: {self.br_kopija}"

  
  def get_naslov(self):
    return self.naslov

  def get_autor(self):
    return self.autor

  def get_god_izdavanja(self):
    return self.god_izdavanja

  def get_br_kopija(self):
    return self.br_kopija

  def set_naslov(self, naslov):
    self.naslov=naslov

  def set_autor(self, autor):
    self.autor=autor

  def set_god_izdavanja(self, god_izdavanja):
    self.god_izdavanja=god_izdavanja

  def set_br_kopija(self, br_kopija):
    self.br_kopija=br_kopija


class Library():

  def __init__(self):
    self.knjige=[]

  def dodavanje_knjige(self, knjiga):
    self.knjige.append(knjiga)


  def brisanje_knjige(self, naslov):
    #self.knjige.remove(naslov)
    self.knjige = [knjiga for knjiga in self.knjige if knjiga.get_naslov() != naslov]


  def pretraga_po_naslovu(self, naslov):
    return [knjiga for knjiga in self.knjige if knjiga.get_naslov().lower()==naslov.lower()]

  def pretraga_po_autoru(self, autor):
    return [knjiga for knjiga in self.knjige if knjiga.get_autor().lower()==autor.lower()]

  def prikaz_dostupnih(self): #naslov, autor, god_izdavanja):
    print(self.knjige)
      #print("Naslov: {0}, autor: {1}, godina izdavanja: {2} ".format( knjiga.get_naslov(), knjiga.get_autor(), knjiga.get_god_izdavanja()))


bibl=Library()
br=0
while  br != -1 :
  print("1 - Dodavanje knjige\n 2 - Brisanje knjige\n 3 - Pretraga po naslovu\n 4 - Pretraga po autoru\n 5 - Prikaz dostupnih knjiga\n -1 Izlaz")
  br=int(input("Unesi zeljenu opciju: "))
  if br==1:
    bibl.dodavanje_knjige(Book(input("Unesi naslov knjige: "), input("Unesi autora knjige: "), input("Unesi godinu izdavanja knjige: "), input("Unesi broj kopija knjige: ")))
  elif br==2:
    bibl.brisanje_knjige((input("Unesi naslov knjige koju zelis da izbrises: ")))
  elif br==3:
    bibl.pretraga_po_naslovu(input("Unesi naslov knige koju zelis pretraziti: "))
  elif br==4:
    bibl.pretraga_po_autoru(input("Unesi autora knjige koju zelis pretraziti: "))
  elif br==5:
    bibl.prikaz_dostupnih()
  elif br == -1:
    print("Izlaz")	
  else:
    print("Pogresan unos!")
    
    
#zad8####################################
class Player():

  def __init__(self, x, y, width, height, health):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.health = health

  def get_x(self):
    return self.x

  def set_x(self, x):
    self.x = x

  def get_y(self):
    return self.y

  def set_y(self, y):
    self.y = y

  def get_width(self):
    return self.width

  def set_width(self, width):
    self.width = width

  def get_height(self):
    return self.height

  def set_height(self, height):
    self.height = height

  def get_health(self):
    return self.health

  def set_health(self, health):
    if 0 <= health <= 100:
      self.health = health
    else:
      print("Greska1.")


class Enemy():

  def __init__(self, x, y, width, height, damage):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.damage = damage

  def get_x(self):
    return self.x

  def set_x(self, x):
    self.x = x

  def get_y(self):
    return self.y

  def set_y(self, y):
    self.y = y

  def get_width(self):
    return self.width

  def set_width(self, width):
    self.width = width

  def get_height(self):
    return self.height

  def set_height(self, height):
    self.height = height

  def get_damage(self):
    return self.damage

  def set_damage(self, damage):
    if 0 <= damage <= 100:
      self.damage = damage
    else:
      print("Greska2.")

def check_collision(player, enemy):
  player_x_range = range(player.get_x(), player.get_x() + player.get_width())
  player_y_range = range(player.get_y(), player.get_y() + player.get_height())
  enemy_x_range = range(enemy.get_x(), enemy.get_x() + enemy.get_width())
  enemy_y_range = range(enemy.get_y(), enemy.get_y() + enemy.get_height())
  if any(x in enemy_x_range
         for x in player_x_range) and any(y in enemy_y_range for y in player_y_range):
    return True
  return False

def decreate_health(player, enemy):
  if check_collision(player, enemy):
    player.set_health(player.get_health() - enemy.get_damage())
  
player1 = Player(x=10, y=20, width=30, height=40, health=90)
enemy1 = Enemy(x=10, y=40, width=30, height=40, damage=20)
enemy2 = Enemy(x=70, y=80, width=25, height=25, damage=30)
print(check_collision(player1, enemy1))
print(player1.get_health())
decreate_health(player1, enemy1)
print(player1.get_health())


#zad9#######################################
import random

class Turnir():
  def __init__(self, naziv_turnira,  broj_igraca, broj_rundi):
    self.naziv_turnira = naziv_turnira
    self.lista_igraca = [] # lista_igraca
    self.poeni=0
    self.broj_igraca=broj_igraca
    self.broj_rundi = broj_rundi
    

  def get_naziv_turnira(self):
    return self.naziv_turnira

  def set_naziv_turnira(self, novi_naziv):
    self.naziv_turnira=novi_naziv

  def get_lista_igraca(self):
    return self.lista_igraca

  def set_lista_igraca(self, nova_lista):
    self.lista_igraca=nova_lista

  def get_broj_igraca(self):
    return self.broj_igraca

  def set_broj_igraca(self, novi_broj):
    self.broj_igraca=novi_broj

  def get_broj_runadi(self):
    return self.broj_rundi

  def set_broj_rundi(self, nova_runda):
    if 0<nova_runda<10:
      self.broj_rundi=nova_runda

  def dodaj_igraca(self,ime_igraca, poeni): #lista_igrača (lista torki oblika ime, broj_bodova)
    self.lista_igraca.append((ime_igraca, poeni))

  def obrisi_igraca(self,ime_igraca):
    self.lista_igraca = [(ime, bodovi) for ime, bodovi in     self.lista_igraca if ime != ime_igraca ]

  def prikazi_najboljeg_igraca(self):
    najbolji_igrac = max(self.lista_igraca, key=lambda x: x[1])
    return najbolji_igrac[0] 

  def pokreni_rundu(self):
    igrac1 = random.randint(0,len(self.lista_igraca)-1)
    igrac2 = random.randint(0,len(self.lista_igraca)-1)

    if random.random() < 0.6:
      pobjednik = igrac1
      gubitnik = igrac2
    else:
      pobjednik = igrac2
      gubitnik = igrac1

    self.broj_rundi += 1


turnir = Turnir(naziv_turnira="Veliki turnir", broj_igraca=3, broj_rundi=0)
turnir.dodaj_igraca("Igrac1",3)
turnir.dodaj_igraca("Igrac2",5)
turnir.dodaj_igraca("Igrac3",9)

print(f"Najbolji igrac: {turnir.prikazi_najboljeg_igraca()}")

turnir.pokreni_rundu()






