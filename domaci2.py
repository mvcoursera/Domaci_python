#zad 1######################################
broj=int(input("Unesite broj: "))
if broj%2==0:
  print("Portal se otvara!")
else:
  print("Portal ostaje zatvoren!")
  

#zad2#############################################
p=int(input("Petar je ubrao p jabuka: "))
m=int(input("Milos je ubrao m jabuka: "))
if p > m :
  print("Petar je pobjednik!")
else:
  print("Milos je pobjednik!")
  
 
#zad3###############################################################
sem=int(input("Jesu li predati seminarski 1-jesu, 0-nisu: "))
pris=int(input("Procenat na prisustvu: "))
if pris>75 and sem == 1:
  print("Student moze da polaze ispit!")
else:
  print("Student ne moze da polaze ispit!")
  

#zad4######################################################
vrijeme=float(input("Unijeti koliko je sati: "))
if (vrijeme > 6 and vrijeme < 13) or (vrijeme >17 and vrijeme < 22) :
  print("Radovi se mogu izvoditi!")
else:
  print("Radovi se ne mogu izvoditi!")
  
  
#zad5###################################################
a=float(input("Unijeti duzinu a: "))
b=float(input("Unijeti duzinu b: "))
c=float(input("Unijeti duzinu c: "))
if (a + b > c and a + c > b and b + c > a) :
  print("Moze se napraviti basta!")
else:
  print("Ne moze se napraviti basta!")
  
  
#zad6##############################################
ozX=float(input("Unesi poziciju pcele x: "))
pozY=float(input("Unesi poziciju pcele y: "))

if (pozY == 2*pozX + 5 ) :
  print("Pcela se krece po zici!")
else:
  print("Pcela se ne krece po zici!")
  
#zad7##########################################





#zad8################################################
prosjek=float(input("Unesi prosjek ucenika: "))

if (prosjek >= 4.5) :
  print("Odlican!")
elif (prosjek>=3.5 and prosjek<4.5):
  print("Vrlodobar!")
elif (prosjek>=2.5 and prosjek<3.5):
  print("Dobar!")
elif (prosjek>=2 and prosjek<2.5):
  print("Dovoljan!")
else:
  print("Nedovoljan!")
  
  
#zad9################################################################
xLGzavjese=int(input("Unesi x koordinatu - lijeva gornja zavjese: "))
yLGzavjese=int(input("Unesi y koordinatu - lijeva gornja zavjese: "))
xDDzavjese=int(input("Unesi x koordinatu cilja - desna donja zavjese: "))
yDDzavjese=int(input("Unesi y koordinatu cilja - desna donja zavjese: "))
xLGprozora=int(input("Unesi x koordinatu - lijeva gornja prozora: "))
yLGprozora=int(input("Unesi y koordinatu - lijeva gornja prozora: "))
xDDprozora=int(input("Unesi x koordinatu cilja - desna donja prozora: "))
yDDprozora=int(input("Unesi y koordinatu cilja - desna donja prozora: "))

if xLGzavjese<=xLGprozora and xDDprozora<=xDDzavjese and yDDzavjese<=yDDprozora and yLGprozora<=yLGzavjese:
  print("Zavjesa odgovara prozoru.")
else:
  print("Zavjesa ne odgovara prozoru.")

#zad10#############################################
x0=int(input("Unesi x0 koordinatu:"))
y0=int(input("Unesi y0 koordinatu:"))
r=int(input("Unesi poluprecnik:"))
x=int(input("Unesi x koordinatu cilja:"))
y=int(input("Unesi y koordinatu cilja:"))
if ((x-x0)**2+(y-y0)**2 <= r**2) :
  print("Cilj je u krugu")
else:
  print( "Cilj nije u krugu")

#zad11######################################################
xLD=int(input("Unesi x koordinatu - lijeva donja ivica: "))
yLD=int(input("Unesi y koordinatu - lijeva donja ivica: "))
xDG=int(input("Unesi x koordinatu cilja - desna gornja ivica: "))
yDG=int(input("Unesi y koordinatu cilja - desna gornja ivica: "))
xMrava=int(input("Unesi x koordinatu cilja - mrav: "))
yMrava=int(input("Unesi y koordinatu cilja - mrav: "))

if (xLD<=xMrava<=xDG and yLD==yMrava) or (xLD<=xMrava<=xDG and yDG==yMrava) or (yLD<=yMrava<=yDG and xLD==xMrava) or (yLD<=yMrava<=yDG and xDG==xMrava):
  print("Mrav se krece po ivici stola.")
else:
  print("Mrav se ne krece po ivici stola.")



#zad12##################################################
broj=int(input("Unesi dvocifreni broj: "))
cif1=broj//10
cif2=broj%10

if cif1 > cif2:
  print(f"Razlika cifara je {cif1-cif2}")
elif cif2 > cif1 : 
  print(f"Zbir je {cif1+cif2}") 
else:
  print(f"Proizvod je {cif1*cif2}")


#zad13######################################
import math
r1=int(input("Unesi poluprecnik 1: "))
r2=int(input("Unesi poluprecnik 2: "))
P1=r1**2*math.pi
P2=r2**2*math.pi
O1=2*r1*math.pi
O2=2*r2*math.pi
if P1 > P2:
  print(f"Obim stola sa vecom P1 je {round(O1,2)}")
elif P2 > P1 : 
  print(f"Obim stola sa vecom P2 je {round(O2,2)}") 
else:
  print("Imaju istu povrsinu")

#zad14###############################################
proiz1=float(input("Unesi cijenu proizvoda 1: "))
proiz2=float(input("Unesi cijenu proizvoda 2: "))
proiz3=float(input("Unesi cijenu proizvoda 3: "))
sum12=proiz1+proiz2
sum13=proiz1+proiz3
sum23=proiz2+proiz3

if sum12 < sum13 and sum12 < sum23 :
  print("Prvi i drugi proizvod imaju najmanju vrijednost!")
elif sum23 < sum13 and sum23 < sum12 :
  print("Drugi i treci proizvod imaju najmanju vrijednost!")
else : 
  print("Prvi i treci proizvod imaju najmanju vrijednost!") 



#zad15##################################################
godina=int(input("Unesi godinu: "))
if godina % 4 == 0 and godina % 100 != 0 or godina % 400 == 0 :
  print("Godina je prestupna!")
else:
  print("Godina nije prestupna!")

#zad16#####################################################
xLG=int(input("Unesi x koordinatu - lijeva gornja: "))
yLG=int(input("Unesi y koordinatu - lijeva gornja: "))
xDD=int(input("Unesi x koordinatu cilja - desna donja ivica: "))
yDD=int(input("Unesi y koordinatu cilja - desna donja ivica: "))
tackaX=int(input("Unesi x koordinatu tacke: "))
tackaY=int(input("Unesi y koordinatu tacke: "))

if xLG<=tackaX<=xDD and yDD<=tackaY<=yLG:
  print("Tacka pripada pravougaoniku.")
else:
  print("Tacka ne pripada pravougaoniku.")
  
#zad17##########################################
duzina=float(input("Unesi duzinu: "))
sirina=float(input("Unesi sirinu: "))

if sirina >= 2*duzina:
  print("Mogu se napraviti dva kvadrata")
else : 
  print("Ne mogu se napraviti dva kvadrata") 
  
  
  
#zad18###########################################3
temperatura=int(input("Unesi temperaturu: "))
if temperatura>0 and temperatura < 100 :
  print("Tecno agregatno stanje!")
elif temperatura <= 0 :
  print("Cvrsto agregatno stanje!")
else :
  print("Gasovito agregatno stanje!")
  

#zad20########################################3
n=int(input("Unesi cetvorocifren broj: "))
sumP=0
proN=1
n=abs(n)
print(n)
if n%2 == 0 :
  n1=n
  while n1 > 0:
    cif = n1 % 10
    if cif % 2 == 0 :
      sumP = sumP + cif
    n1 = n1//10
  print("Suma parnih cifara je: ", sumP)
else :
  n1=n
  while n1 > 0:
    cif = n1 % 10
    if cif % 2 != 0 :
      proN = proN * cif
    n1 = n1//10
  print("Suma parnih cifara je: ", proN)


#zad21###############################################3
import math
x=int(input("Unesi x: "))
y=0
if x <= -7 :
  y = -2*x + 7/2
elif x > -7 and x < 1 :
  y = (x**2 - 3*x + 5) / (x**2 + 2)
elif x >= 1 and x <= 8 :
  y = math.sqrt(x**2 + 2*x + 2) + math.sqrt(abs(3/2*x - 4/7))
else:
  y = abs(3/x**2 - 11*x)
  
print("Dobijena vrednost je: ", round(y,2))
  
#zad22#######################################
x=int(input("Unesi x koordinatu:"))
y=int(input("Unesi y koordinatu:"))

if x>0 and y>0:
  print("Tacka pripada prvom kvadrantu")
elif x>0 and y<0:
  print("Tacka pripada cetvrtom kvadrantu")
elif x<0 and y<0:
  print("Tacka pripada trecem kvadrantu")
elif x<0 and y>0:
  print("Tacka pripada drugom kvadrantu")
elif x==0 and y==0:
  print("Tacka je centar koordinatnog sistema")
elif x==0 and (y>0 or y<0):
  print("Tacka se nalazi na x osi")
elif y==0 and (x>0 or x<0):
  print("Tacka se nalazi na y osi")

  




  
#zad24###################################
tekst=input("Unesi tekst: ")
if len(tekst) > 30:
  tekst1=tekst[0:30] + "..."
  print(f"Skraceni string je: {tekst1}")
else:
  print(f"String ima manje od 30 karaktera: {tekst}")
  
#zad25##################################
tekst=input("Unesi tekst: ")
print("Novi tekst je: ",tekst[1:-1])

#zad26################################3
broj=input("Unesi broj: ")
if broj[0:2] == "0b" :
    print("Broj je binarni!")
elif broj[0:2] == '0o' :
  print("Broj je oktalni!")
elif broj[0:2] == '0x' :
  print("Broj je heksadecimalni!")
else :
  print("Broj je dekadni!")


#zad27###################################
tekst=input("Unesi tekst: ")
n = len(tekst)
br=0
for i in range(n):
  if tekst[i] == "a" or tekst[i] == "e" or tekst[i] == "i" or tekst[i] == "o" or tekst[i] == "u" :
    print("Tekst sadrzi samoglasnike!")
    br+=1
    break
if br == 0 :
    print("Tekst ne sadrzi samoglasnike!")


#zad28#####################################
string = input("Unesi string: ")
target = input("Unesi target: ")
n=len(string)
if string[-2:n] == target :
  print("Da.")
else :
  print("Ne.")



#zad29##########################################
broj=input("Unesi broj: ")
n=len(broj)
br=0
for i in range(n):
  if broj[i] == "1" or broj[i] == "0" :
    br+=1
  else :
    print("Broj nije binarni!")
    break
if br==n:
  print("Uneseni broj je binarni!")

#zad30################################################
n=int(input("Unesi n: "))
brP=0
brN=0
sumP=0
proN=1
for i in range(1,n+1) :
  if  i%2==0 :
    brP=brP+1
    sumP=sumP+i
  else:
    brN=brN+1
    proN=proN*i
print("Zbir parnih brojeva je: ",sumP)
print("Proizvod neparnih brojeva je: ",proN)
print("Parnih brojeva je: ",brP)
print("Neparnih brojeva je: ",brN)


#zad32########################################
brojA = int(input("Unesite broj A: "))	
brojB = int(input("Unesite broj B: "))
djelilac = int(input("Unesite djelilac: "))
sum = 0
br = 0
for i in range(brojA+1, brojB):
  if i % djelilac == 0:
    sum += i
    br += 1
print("Suma je {0}, a broj elemenata djeljivih je {1}".format(sum, br))


#zad33######################################
n=int(input("Unesi n: "))
n1=n
sum=0
while n1 > 0:
  sum=sum+n1%10
  n1=n1//10
print("Suma cifara unijetog broja je: ",sum)


#zad34####################################
tekst=input("Unesi tekst: ")
n = len(tekst)
proiz=1
for i in range(n):
  if tekst[i] >= "0" and tekst[i] <= "9" :
    proiz = proiz * int(tekst[i])
print("Proizvod je: {}".format(proiz))


#zad35######################################
import string
string = input("Unesi string: ")
n = len(string)
novi_string = 0
for i in range(n) :
  if  string[i].isdigit() :
    novi_string = novi_string*10 + int(string[i])
print(f"Dobijeni broj je: {novi_string}")



#zad36#########################################
string = input("Unesi string sa malim slovima: ")
n = len(string)
novi_string = ""
for i in range(n) :
  if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" :
    novi_string += "1"
  elif string[i] > "a" and string[i] <= "z" :
    novi_string += "0"
  else :
    print("Greska!")
    novi_string = ""
    break
print(novi_string)


#zad37#########################################
string = input("Unesi string: ")
n = len(string)
sum = 0
for i in range(n) :
  if  string[i] == "*" :
    sum -= 1
  elif string[i] == "1" :
    sum += 1
  elif string[i] == "0" :
    sum += 0
  else :
    print("Greska!")
    sum = 0
    break
if sum > 0 :
  print("Igrac je u plusu: {}".format(sum))
  
  

#zad38####################################################
import string
string = input("Unesi string: ")
n = len(string)
br_str = ""
novi_string = ""
for i in range(n) :
  if string[i].isdigit() :
    if int(string[i]) % 2 == 0 :
      novi_string += "0"
      br_str += string[i]
    elif int(string[i]) % 2 != 0 :
      novi_string += "1"
      br_str += string[i]
print("Prvobitni niz brojeva je: {0}, a novi niz je: {1}".format(br_str, novi_string))


#zad39##################################
broj = input("Unesi broj: ")
n = len(broj)
sum = 0
for i in range(n) :
    sum += int(broj[i])**n
if sum == int(broj) :
  print("Da")
else :
  print("Ne")
  
#zad40#############################################3
niz = [1,4,6,7,-1,-2,-5]
n=len(niz)
sum = 0
for i in range(n) :
  if niz[i] < 0 :
    sum = sum + abs((niz[i]))
print(sum)


#zad41#############################################
n = int(input("Unesi duzinu liste: "))
list = []
for i in range(n) :
  el = int(input("Unesi element liste: "))
  list.append(el)
print(list)
max = int(input("Unesi max vrijednost: "))
br = 0
for i in range(n):
  if list[i] < max :
    br += 1
print("Takvih brojeva je:", str(br))

#zad42#####################################
n = int(input("Unesi duzinu liste: "))
list = []
sum = 0
for i in range(n):
  el = int(input("Element liste: "))
  list.append(el)
  sum += el
print(list)
popust = int(input("Unesi popust u: "))
sum_sa_p = 0
for i in range(n):
  list[i] = list[i] * (100-popust) / 100
  sum_sa_p += list[i]
print(list)
print("Zarada marketa je manja za {}".format(round(sum - sum_sa_p),2) + " eura.")


#zad43##############################################
n = int(input("Unesi duzinu liste: "))
list = []
for i in range(n):
  el = int(input("Element liste: "))
  list.append(el)
print(list)
br_3 = 0
br_4 = 0
br_5 = 0
for i in range(n):
  if list[i] == 5 :
    br_5 += 1
  elif list[i] == 4 :
    br_4 += 1
  elif list[i] == 3 :
    br_3 += 1
  else :
    print("Greska!")
print(f"Broj petica je {br_5}, broj cetvorki je {br_4} i broj trojki je {br_3}")

#zad44############################################
list = []
for i in range(10):
  el = int(input("Element liste: "))
  list.append(el)
print(list)
maxbr = max(list)
print(f"Najvise je bilo {maxbr} posjeta")



#zad45#########################################
n = int(input("Unesi duzinu liste: "))
list = []
sum = 0
for i in range(n):
  el = int(input("Element liste: "))
  list.append(el)
  sum += el
print(list)
pr_zarada = sum / n
br = 0
for i in range(n):
  if list[i] > pr_zarada :
    br += 1
print(f"Broj zaposlenih sa vecom platom od prosjecne je {br}")

#zad46##############################################
n = int(input("Unesi duzinu liste: "))
if n<2:
  print("Lista mora imati najmanje 2 elemenata")
  n = int(input("Unesi duzinu liste: "))
list = []
for i in range(n):
  el = int(input("Element liste: "))
  list.append(el)
print(list)
list.sort(reverse=True)
print(f"Drugi zaposleni sa najvecom platom je {list[1]}")



#zad47###################################################
broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))
broj3 = int(input("Unesite treci broj: "))
max = broj1
if broj2 > max :
  max = broj2
  if broj3 > max :
    max = broj3
    print("Najveci broj je broj3: ", max)
  else :
    print("Najveci broj je broj2: ", max)
else :
  print("Najveci broj je broj1: ", max)
  
#zad48###################################
x = int(input("Unesite X: "))
n = int(input("Unesite stepen n: "))
rez = 1
i=1
while i<=n :
  rez *= x
  i=i+1
print("Dobijeni rezultat je: {}".format(rez))

#zad49########################################
string = input("Unesite string: ")
n = int(input("Unesite duzinu n: "))
duz = len(string)
if duz < n :
  novi_str = string + '...'
elif duz > n :
  novi_str = string[0:n] + '...'
print(f"Novi string je {novi_str}")

#zad50#####################################
string = input("Unesite string: ")
n = len(string)
novi_str = ""
for i in range(n) :
  if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" :
    novi_str += string[i]
print(f"Novi string je: {novi_str}")

#zad51#####################################
import string
passwd = input("Unesite lozinku: ")
n = len(passwd)
br_9 = 0
br_A = 0
br_a = 0
if n >= 8 :
  for i in range(n) :
    if passwd[i].isdigit() :
      br_9 += 1
    elif passwd[i].isalpha() :
      if passwd[i].isupper() :
        br_A += 1
      elif passwd[i].islower() :
        br_a += 1
if br_9 >= 1 and br_A >= 1 and br_a >= 1 :
  print("Lozinka je dobra")
  #print(br_9,br_A,br_a)
else :
  print("Lozinka nije dobra")
  

#zad52##########################################
a = input("Unesite string: ")
pre = input("Unesite prefiks: ")
suf = input("Unesite sufiks: ")
num = int(input("Unesite broj ponavljanja sufiksa i prefiksa: "))
novi_str = ""
i = 0
pre1 = ""
suf1 = ""
while i < num :
  pre1 += pre
  suf1 += suf
  i += 1
novi_str = pre1 + a + suf1
print(f"Prosireni string je: {novi_str}")
  
#zad53################################################
zbir = int(input("Unesite Petrov zbir: "))
zbir= zbir
i=0
while zbir > 0 and i < zbir :
  i += 1
  zbir -= i
print("Broj golova na utakmici je {}".format(i))


#zad54###############################################
a = input("Unesite string: ")
n = len(a)
poz = int(input("Unesite poziciju: "))
if poz == 0 :
  print("slobodno") if a[2] == "0" else print("zauzeto") 
elif poz == n-1 :
  print("slobodno") if a[-2] == "0" else print("zauzeto") 
else :
  for i in range(1,n-1) :
    if i == poz:
      print("slobodno") if (a[i-1] == "0" and a[i+1]) else print("zauzeto") 

#zad55#########################################
h = int(input("Unesite prirodan broj h: "))
o = int(input("Unesite prirodan broj o: "))
br_h = h//2
if br_h > 0 and o > 0 :
  if o >= br_h :
    print(f"Broj molekula vode je: {br_h}")
  else :
    print(f"Broj molekula vode je: {o}")
else :
  print("Ne moze se dobiti nijedan molekul.")
  
  
#zad56#############################################
import string
str = input("Unesi string: ")
n = len(str)
br=0
for i in range(0,n-3) :
  if str[i] == "-" and str[i+1].isdigit() and not str[i+2].isdigit() :
    br += 1
if str[-2] == "-" and str[-1].isdigit() :
  br += 1
print("Jednocifrenih neg brojeva je: ", br)
  


#zad57###################################
broj = input("Unesi broj: ")
n = len(broj)
sum = 0
for i in range(n) :
    sum += int(broj[i])**n
if sum == int(broj) :
  print("Da")
else :
  print("Ne")
  
#zad58##################################
import string
str = input("Unesi string: ")
n = len(str)
novi_str = ""
for i in range(0,n) :
  if not str[i].isdigit() :
    novi_str += str[i]
print("Novi string je: ", novi_str)

#zad59###########################################
str = input("Unesi string u vidu brojeva: ")
n = len(str)
novi_str = ""
for i in range(0,n) :
  if int(str[i]) % 2 == 0 :
    novi_str += "0"
  else:
    novi_str += "1"
print("Novi string je: ", novi_str)


#zad61########################################
import string
str = input("Unesi string: ")
n = len(str)
novi_str = ""
for i in range(0,n) :
  if str[i].isupper() :
    novi_str += str[i]
print("Novi string je: ", novi_str)



#zad64######################################
broj = input("Unesi broj: ")
n = len(broj)
min = int(broj[0])
max = int(broj[0])
for i in range(1,n) :
  if int(broj[i]) > max :
    max = int(broj[i])
  elif int(broj[i]) < min :
    min = int(broj[i])
print(f"Najmanje cifra je {min}, a najveca {max}")

#zad65########################################################
d = float(input("Unesite duzinu terase u metrima: "))
n = int(input("Unesite broj stubica: "))
s = float(input("Unesite sirinu stubica u centimetrima: "))
s = round(s,2)
d = d * 100 #prebacivanje u cm
r = (d - n * s)/(n+1)
print(f"Rastojanje izmedju stubica je {r} cm"	)


#zad66##############################################
n = int(input("Unesi duzinu liste: "))
list = []
for i in range(n) :
  el = int(input("Unesi element liste: "))
  list.append(el)
print(list)
br_2 = 0
br_3 = 0
for i in range(n) : 
  if list[i] > 9 and list[i] < 100 :
    br_2 += 1
  elif list[i] > 99 and list[i] < 1000 :
    br_3 += 1
if br_2 > br_3 :
  print("Vise je dvocifrenih brojeva.")
elif br_3 > br_2 :
  print("Vise je trocifrenih brojeva.")
else :
  print("Ima ih isto.")


#zad67########################################
list = [1,3,5,7,3,3,6,9,3,5,55,9,1,2,7,4]
broj = int(input("Unesite broj: "))
br = list.count(broj)
print("Broj se ponavlja: " + str(br) + " puta")

  
#zad68######################################
n = int(input("Unesi duzinu liste: "))
list = []
sum = 0
for i in range(n) :
  el = int(input("Unesi element liste: "))
  list.append(el)
  sum += el
print(list)
pr_zarada = sum / n
uvecanje = int(input("Unesi uvecanje u eurima: "))
for i in range(n) :
  if list[i] > pr_zarada :
    list[i] += uvecanje
print(list)

#zad69#######################################
n = int(input("Unesi duzinu liste: "))
list = []
sum = 0
for i in range(n) :
  el = int(input("Unesi element liste: "))
  list.append(el)
  sum += el
print(list)
pr_zarada = sum / n

for i in range(n):
  if list[i] < pr_zarada:
    list[i] = round(1.1*list[i])
  elif list[i] > pr_zarada:
    list[i] = round(0.9*list[i],2)
br = 0

for i in range(n):
  if list[i] > pr_zarada: 
    br += 1
print("Iznad prodjeka je: " + str(br) + " zarada.")
print(list)


#zad70#######################################
n = int(input("Unesi duzinu liste: "))
list = []
for i in range(n) :
  el = int(input("Unesi element liste: "))
  list.append(el)
print(list)
sum = 0
for i in range(n):
  if list[i] % 3 == 0:
    sum += pow(list[i],2)
print("Suma kvadrata brojeva deljivih sa 3 je: ", str(sum))


#zad71#####################################
import math
n = int(input("Unesi duzinu liste: "))
list = []
for i in range(n) :
  el = int(input("Unesi element liste: "))
  list.append(el)
print(list)
br = 0
for i in range(n):
  if pow(list[i],0.5).is_integer() :
    br += 1
print("Takvih brojeva je:", str(br))

#zad74##########################
a = []
na=int(input("Unesi broj zaposlenih: "))
print("Unesi plate zaposlenih: ")
for i in range(na):
  el=int(input())
  a.append(el)

sum=0
for i in range(na):
  sum += a[i]
prosjek = round(1.1*sum/na,2)
print("prosjek plata u dolarima je: {}".format(prosjek))



#zad75#######################################
a = []
na=int(input("broj klijenata: "))
print("Unesi iznos stednje klijenta: ")
for i in range(na):
  el=int(input())
  a.append(el)

kamata=float(input("Unesi kamatu: "))
sum_a=0
sum_kam=0
for i in range(na):
  sum_a += a[i]
  sum_kam += (a[i]*kamata/100+a[i])

print(f"Banka je izgubila na kamatama {sum_kam-sum_a} eura")




#zad76#############################################


#zad77############################################
a = []
na=int(input("unesi br elemenata liste: "))
print("Unesi element liste: ")
for i in range(na):
  el=int(input())
  a.append(el)
br=0
for i in range(na-1):
  if a[i] <= a[i+1]:
    br += 1
if br == na-1:
  print("True")
else:
  print("False")


#zad78############################################
na=int(input("unesi br elemenata liste: "))
print("Unesi element liste: ")
for i in range(na):
  el=int(input())
  a.append(el)
a.sort(reverse=True)
print(a)
print(f"Drugi najskuplji aritkal u prodavnici je {a[1]} eura")


#zad80########################################################
na=int(input("unesi br elemenata liste: "))
print("Unesi element liste: ")
for i in range(na):
  el=float(input())
  a.append(el)
a.sort(reverse=True)
print(a)
print(f"Razlika izmedju skokova je {round(a[0]-a[-1],2)}")

#zad85#################################################
lista = []
N=int(input("Unesi br elemenata liste: "))
np=int(input("Unesi broj posjetilaca: "))
for i in range(N):
  el=int(input("Unesi element liste "))
  lista.append(el)
print(lista)
if max(lista) >= np:
  print("Potrebno je rezervisati 1 red.")
elif max(lista) < np :
  sum=0
  br = 0
  for i in range(N):
    if sum<np:
      sum += lista[i]
      br += 1
    else:
      print("Potrebno je rezervisati", br, "reda.")
      break
  
	  




#zad86################################################
a = [] #lista
na=int(input("Unesi duzinu liste a: "))
print("Unesi elemente liste: ")
for i in range(na):
  el=int(input())
  a.append(el)
def absolute_of_even_number(a):
  sum=0
  for i in range(na):
    if a[i] < 0 and a[i] % 2 == 0:
      sum += abs(a[i])
  return sum
print("Apsolutna suma negativnih parnih brojeva je: ", absolute_of_even_number(a))

#zad87##########################################
a = [] #lista
na=int(input("Unesi duzinu liste a: "))
print("Unesi elemente liste: ")
for i in range(na):
  el=(input())
  a.append(el)
b = [] #lista
nb=int(input("Unesi duzinu liste b: "))
print("Unesi elemente liste b: ")
for i in range(nb):
  el=(input())
  b.append(el)
def presjek(a,b):
  lista=[]
  for i in range(na):
    for j in range(nb):
      if a[i]==b[j]:
        lista.append(a[i])
  return lista
print("Presjek listi su elementi: {}".format(presjek(a,b)))


#zad88########################################
a = []
n=int(input("Unesi duzinu liste: "))
print("Unesi elemente liste: ")
for i in range(n):
  el=int(input())
  a.append(el)
max_br=int(input("Unesi max vrijednost: "))
def br_elemenata(a,max_br):
  br=0
  for i in range(n):
    if a[i]<max_br:
      br+=1
  return br
print("Broj elemenata manjih od max je: {}".format(br_elemenata(a,max_br)))



#zad89###################################
a = []
n=int(input("Unesi duzinu liste: "))
print("Unesi elemente liste: ")
for i in range(n):
  el=int(input())
  a.append(el)
def br_elemenata(a):
  br=0
  for i in range(n):
    for j in range(i,n):
      if a[i] == -a[j]:
        br=br+1
  return br
print("Broj elemenata sa suprotnim brojem je: {}".format(br_elemenata(a)))


#zad90#############################################3
a = []
n=int(input("Unesi duzinu liste: "))
print("Unesi elemente liste: ")
for i in range(n):
  el=int(input())
  a.append(el)
x=int(input("Unesi prirodan broj x: "))
def update_list(a,x):
  for i in range(n):
    if a[i]%2 == 0:
      a[i] += x
  return a
print("Nova lista je: {}".format(update_list(a,x)))


#zad91##############################################
a = []
n=int(input("Unesi duzinu liste: "))
if n<2:
  print("Lista mora imati najmanje 2 elementa")
  n=int(input("Unesi duzinu liste: "))
for i in range(n):
  el=int(input())
  a.append(el)
#print(a)
def second_max(a):
  a.sort(reverse=True)
  return a[1]
print(second_max(a))
#print(a)



