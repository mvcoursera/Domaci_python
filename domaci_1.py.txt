#zad1
a=int(input("unesi duzinu stranice a: "))
b=int(input("unesi sirinu stranice b: "))
p=a*b
print("povrsina pravougaonika je: ",p)
o=2*a+2*b
print("obim pravougaonika je: ",o)

#########################
#zad2
import math

a=int(input("Vrijednost a: "))
b=int(input("Vrijednost b: "))
c=int(input("Vrijednost c: "))
print("kvadratna jednacina je: {}*x^2+{}*x+{}=0".format(a,b,c))
x1=-b+math.sqrt(b*b-4*a*c)/(2*a)
x2=-b-math.sqrt(b*b-4*a*c)/(2*a)

print(x1)
print(x2)
#############################
#zad3
A=int(input("Vrijednost A: "))
B=int(input( "Vrijednost B: "))
raz_kvadr=(A-B)*(A+B)
print("Razlika kvadrata: {}".format(raz_kvadr))
##########################
#zad4
d=int(input("Duzina d: "))
s=int(input( "Sirina s: "))
met=2*(d+s)*4
print("Sportista obidje: {}".format(met))
#########################
#zad5
v=int(input("Visina v u mm: "))
s=int(input( "Sirina s u mm: "))
p=v*s
p_cm=p/100
print("Povrsina : {} u cm2.".format(p_cm))
########################
#zad6
a=int(input("parametar a: "))
b=int(input("parametar b: "))
c=int(input("parametar c: "))
print("Formula je: ({}+{}+{})^2 ".format(a,b,c))
rez=a**2+b**2+c**2+2*a*b+2*b*c+2*a*c
print("rezultat je: ",rez)
############################
#zad7
h=float(input("Unesi vrijeme u satima: "))
lit=h/2
print("Kolicina vode koju je Marko popio u lit: {}",int(lit))
########################
#zad8
import math

P=float(input("Unesi povrsinu kruga: "))
r=math.sqrt(P/3.14)
O=2*r*3.14
print("Duzina trake: {}",round(O,3))
########################
#zad9
d=int(input("duzina d: "))
s=int(input("sirina s: "))
r=int(input("rastojanje r: "))
O=2*(4*r+d+s)
print("Duzina ograde u metrima je:",O)
#########################
#zad10
x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
a=abs(x2-x1)
b=abs(y2-y1)
O=2*(a+b)
P=a*b
print("Povrsina je: {0} , a obim je: {1}".format(P,O))
#####################
#zad11
import math

x1=int(input("x1: "))
x2=int(input("x2: "))
y1=int(input("y1: "))
y2=int(input("y2: "))
print("Tacke su: A({0},{1}) i B({2},{3}) ".format(x1,x2,y1,y2))
e_dist=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Euklidsko rastojanje izmedju A i B je: ", round(e_dist,2))
###################
#zad12
N=input("Koliko godina ima Milos? ")
godiste=2024-int(N)
print(f'Milos je rodjen ' + str(godiste) + '. godine.')
print(f'Milos je rodjen {godiste}. godine.')
print('Milos je rodjen {}. godine.'.format(godiste))
#####################
#zad13
import math

x1, y1 = input("Unesi koordinate hrasta G: ")
print("G({0},{1}) ".format(x1,y1))
x2, y2 = input("Unesi koordinate kuce K: ")
print("K({0},{1}) ".format(x2,y2))
x3=int(x2)+2
y3=int(y2)-3
print("B({0},{1}) ".format(x3,y3))
vaz_rast=round(math.sqrt((int(y1)-y3)**2+((int(x1)-x3)**2)),2)
print('Vazdusno rastojanje od hrasta do blaga je: {} '.format(vaz_rast))

rast_G_B=round(math.sqrt((int(y1)-int(y2))**2+((int(x1)-int(x2))**2))+math.sqrt((int(y2)-y3)**2+((int(x2)-x3)**2)),2)
print('Rastojanje od hrasta do blaga je preko K je: {} '.format(rast_G_B))

#######################
#zad14
kvadrat=int(input("Koliko kvadrata ima stan? "))
parking=int(input("Ima li parking (1-da, 0-ne)? "))
zona=int(input("Koja je zona (zona1=3, zona2=2, zona3=1)? "))
cijena_kv=1200

if parking==1:
    cijena_stana=zona*kvadrat*cijena_kv*5*10+1000
    #print("cijena stana je {}".format(cijena_stana))
elif parking==0:
    cijena_stana=zona*kvadrat*5*cijena_kv+1000

print("cijena stana je {}".format(cijena_stana))

#########################
#zad15
a1, a2=input("tacka A ")
b1,b2=input("tacka B ")
c1,c2=input("tacka C ")
print("A({0},{1}), B({2},{3}), C({4},{5}) ".format(a1,a2,b1,b2,c1,c2))
rasAB=((int(a1)-int(b1))**2+(int(a2)-int(b2))**2)**0.5
rasAC=((int(a1)-int(c1))**2+(int(a2)-int(c2))**2)**0.5
rasBC=((int(b1)-int(c1))**2+(int(b2)-int(c2))**2)**0.5
S=(0.5*(rasAB+rasAC+rasBC))
print(S)
P=round((S*(S-rasAB)*(S-rasAC)*(S-rasBC))**0.5,2)
print("Povrsina trougla je {0}".format(P))
########################
#zad16
p=float(input("unesi predjene km: "))
cijena=(1+p/2)
print("cijena je: {}".format(cijena))
######################
#zad17
import random

cijena=float(input("Unesi cijenu knjige: "))
posto_snizenja=random.randrange(100)
print(posto_snizenja)
snizena_cijena=cijena-cijena*posto_snizenja/100
print("Cijena knjige sa popustom je: {}".format(snizena_cijena))


#############################
#zad18
p=float(input("unesi cijenu konzole: "))
cijena1=1.1*p
cijena2=0.9*cijena1
print("nova cijena je: {}".format(cijena2))
###############################
#zad19
p=int(input("unesi trocifren broj: "))
zbir=p%10+p//100+p//10%10
print("zbir je: {}".format(zbir))

##############################
#zad20
p=int(input("unesi trocifren broj: "))
zbir=p%10+p//100+p//10%10
proiz=(p%10)*(p//100)*(p//10%10)
kod=int(proiz-zbir)
print("Kod je: {}".format(kod))

##########################
#zad21
broj=int(input("Unesi cetvorocifren broj: "))
kv_zbira=(broj%10+broj//1000)**2
raz_kv=(broj%100//10)**2-(broj//100%10)**2
sifra=kv_zbira-raz_kv
print("Sifra je: {}".format(sifra))

########################
#zad22
N=int(input("Unesi ukupan broj ucenika: "))
K=int(input("Unesi broj ucenika na drugoj strani: "))
p1=float(input("unesi prosjecan br poena p1: "))
p2=float(input("unesi prosjecan br poena p2: "))
pr_N=round(((N-K)*p1+K*p2)/N,2)
print("Prosjecan broj poena svih ucenika je: {}".format(pr_N))

##########################
#zad23
a =int(input("unesi parametar a: "))
b =int(input("unesi parametar b: "))
sr_vr=float((a+b)/2)
print("srednja vrednost je: {}".format(sr_vr))

########################
#zad24
Milica=int(input("Koliko puta je Ana obisla teren: "))
Ana=int(input("Koliko puta je Milica obisla teren: "))
print(Milica)
print(Ana)
niz=[Milica,Ana]
print(niz)
print("Milica je obisla {0}, a Ana {1}.".format(niz[1],niz[0]))

#######################
#zad25
rast =float(input("unesi rastojanje u cm: "))
rast_m=rast/100
print("rastojanje u m je: {}".format(rast_m))

########################
#zad26
broj=int(input("unesi cetvorocifren broj: "))
sprat=broj%100//10
print("Sprat je: {}".format(sprat))

########################
#zad27
broj=int(input("unesi cetvorocifren broj: "))
kv_zbir=(broj//1000)**2+(broj%100//10)**2+(broj%10)**2+((broj//100)%10)**2
print("Kvadrat zbira cifara je: {}".format(kv_zbir))

#########################
#zad28
broj=int(input("unesi trocifren broj: "))
zamjena=(broj//100)+(broj%100//10)*10+(broj%10)*100
print("Novi broj je: {}".format(zamjena))

###################
#zad29
x1=int(input("unesi kordinatu x1: "))
y1=int(input("unesi kordinatu y1: "))
x2=int(input("unesi kordinatu x2: "))
y2=int(input("unesi kordinatu y2: "))
x3=(x2-x1)/2
y3=(y2-y1)/2
rast13=round(((x1-x3)**2+(y1-y3)**2)**0.5,2)
rast23=round(((x2-x3)**2+(y2-y3)**2)**0.5,2)
print("Rastojanje pocetne pozicije A do tacke C je {0}, a od B do C je {1} ".format(rast13,rast23))


##########################
#zad30
a=543
b=130
st_kv=65
a1=a//st_kv
b1=b//st_kv
print(a1,b1)
br=a1*b1
print("Broj kvadrata je: {}".format(br))

#############################
#zad31
dijag=50
b=(dijag**2-((16/9)**2+1))**0.5
a=16/9*b
P=a*b
print("Povrsina ekrana je: {}".format(P))

#############################
#zad32
broj=int(input("Unesite sestocifreni broj: "))
a=broj//100000
b=broj//10000%10
c=broj//1000%10
d=broj%1000//100
e=broj%100//10
f=broj%10
#print(d)
print(b+d*e)
print(a*c+2+f)
print(bool(a*c+2+f==b+d*e))

################################
#zad33
a=int(input("unesi sirinu pravouganika "))
b=int(input("unesi duzinu pravougaonika "))
c=int(input("unesi stranicu kvadrata " ))
a1=a//c
b1=b//c
print(a1,b1)
br=a1*b1
print("Broj poligona je: {}".format(br))

##############################
#zad34
broj=int(input("unesi setocifreni broj: "))
sum=(broj%1000000//100000+broj%10000//1000%10+broj%1000//100+broj//10000%10+broj%100//10+broj%10)**2
pro=(broj%10000//1000)*(broj//100%10)
idb=sum-pro
print("ID je: {}".format(idb))

###########################
#zad35
#broj=(input("unesi petocifren broj: "))
#sprat=int(broj[2])+int(broj[4])
broj=int(input("unesi petocifren broj: "))
sprat=broj%10+broj%1000//100
print("Novi broj je: {}".format(sprat))

