#zad1##############################
from functools import reduce
l = ["flowers","flow","flight"]
def najduzi_string(lista):
  return reduce(lambda x,y: x if len(x) > len(y) else y, lista)

print(najduzi_string(l))



#zad2#############################
l1=["Milica","Ana","Sanja","Marko","Janko","Luka"]
l2 = [9.2, 8.5, 9.1, 7.5, 6.2, 8.9]

def search_students(l1,l2):
  l3=[]
  for i in range(len(l1)):
    if l2[i] > 8.5:
      l3.append((l1[i],l2[i]))
  return l3

print(search_students(l1,l2))


#zad3##########################
lista=[{ 'ime': 'Ana', 'godine': 22, 'prosjek': 9.1 }, { 'ime': 'Marija', 'godine': 20, 'prosjek': 8.1 },{ 'ime': 'Marko', 'godine': 25, 'prosjek': 7.1 },{ 'ime': 'Luka', 'godine': 23, 'prosjek': 8.91 },{ 'ime': 'Janko', 'godine': 21, 'prosjek': 8.7 }]

def sort_studenti(lista):
  lista=filter(lambda x: x['godine']>21,lista)
  lista=sorted(lista,key=lambda x: x['prosjek'], reverse=True)
  return lista

print(sort_studenti(lista))


#zad4#######################
from functools import reduce

li = ["Hello, World!", "Python is cool", "Functional programming rocks"]
def count_words(lista):
  str=reduce(lambda x,y: x+y, map(lambda x: x.split(), lista))
  print(str)
  return len(str)

print(count_words(li))


#zad5##########################
from functools import reduce
li=[("Milica", 5, "Fizika"), ("Luka", 5, "Programiranje"), ("Maja", 3, "Fizika"), ("Petar", 3, "Programiranje"),("Marko", 5, "Engleski"), ("Marko", 5, "Matematika"), ("Ana", 4, "Fizika")]

def prosjek(lista):
  sum=reduce(lambda x,y: x+y,list(map(lambda x: x[1], lista)))
  print(len(lista))
  return(sum/len(lista))

print(prosjek(li))


#zad6#######################
niz=[2,3,4,1,2,3,4,5,6,7,8,9,10,11,12,13]
def promjena(niz):
  return list(map(lambda x,y: y-x , niz[:-1], niz[1:]))

print(promjena(niz))

#zad7############################
from functools import reduce

lista = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

def calculate_frequency(lst):
  skup = list(map(lambda x: (x, lst.count(x)), lst))
  print(skup)
  l=[]
  for i in range(0,len(skup)-1):
   for j in range(1,len(skup)):
     if skup[i]==skup[j] and skup[i] not in l:
        l.append(skup[i])
     else:
      pass
  
  return l

print(calculate_frequency(lista))


#zad8#########################
def max_proizvod():
 
  rectangles = []
  with open("rectangles.txt", "r") as file:
      for line in file:
        a, b = map(int, line.strip().split(","))
        rectangles.append((a, b))
        #print(rectangles)
      #return rectangles
  sqr=[]
  for i in rectangles:
    if i[0] == i[1]:
      sqr.append(i)
  #print(sqr)
  p=0
  max_p=0
  for i in sqr:
    p=i[0]*i[1]
    if p>max_p:
      max_p=p
      
  return max_p

pp = max_proizvod()
print(f"Najveci proiyvod je: {pp}")


#zad9##########################
def main():
  trazeni_grad = input("Unesite naziv grada: ")

  try:
      with open("cities.txt", "r") as file:
          lines = file.readlines()
  except FileNotFoundError:
      print("Fajl 'cities.txt' nije pronadjen.")
      return
  max_broj_stanovnika = 0
  naziv_naselja = ""
  for line in lines:
    grad, naselje, broj_stanovnika = line.strip().split(",")
    print(line.strip().split(","))
    broj_stanovnika = int(broj_stanovnika)
    if grad == trazeni_grad and broj_stanovnika > max_broj_stanovnika:
        max_broj_stanovnika = broj_stanovnika
        naziv_naselja = naselje

  if naziv_naselja:
      print(f"Naselje sa najvecim br stanovnika u gradu {trazeni_grad} je: {naziv_naselja}")
  else:
      print(f"Nije pronadjeno naselje za grad {trazeni_grad}.")

if __name__ == "__main__":
  main()
  
  
#zad10##############################
def main():
  
  drz=input("Unesi drzavu: ")
  
  try:
    with open("population.txt", "r") as file:
      lines=file.readlines()
  except FileNotFoundError:
    print("Fajl nije pronadjen.")
    return

  min_br_stanovnika = float('inf')
  print(min_br_stanovnika)
  naziv_grada=""
  for line in lines:
    drzava,grad,br_stanovnika=line.strip().split(",")
    print(line.strip().split(","))
    br_stanovnika=int(br_stanovnika)
    if drzava==drz and br_stanovnika<min_br_stanovnika:
      min_br_stanovnika=br_stanovnika
      naziv_grada=grad

  if naziv_grada=="":
    print("Nema grada za trazenu drzavu!")
  else:
    print(f"Grad sa najmanje stanovnika u {drz} je {naziv_grada} sa {min_br_stanovnika} stanovnika.")
    
if __name__ == "__main__":
  main()



#zad11##################################
def main():
  
  drz=input("Unesi drzavu: ")
  
  try:
    with open("population.txt", "r") as file:
      lines=file.readlines()
  except FileNotFoundError:
    print("Fajl nije pronadjen.")
    return

  sum=0
  for line in lines:
    drzava,grad,br_stanovnika=line.strip().split(",")
    #print(line.strip().split(","))
    br_stanovnika=int(br_stanovnika)
    if drzava==drz:
      sum+=br_stanovnika
      
  if sum==0:
     print("Nema trazene drzave!")
  else:
     print(f"Drzava {drz} ima ukupno {sum} stanovnika.")
    
if __name__ == "__main__":
  main()
  
  
#zad12#############################
def main():
  
  try:
    with open("fajl.txt", "r") as file:
      lines=file.readlines()
  except FileNotFoundError:
    print("Fajl nije pronadjen.")
    return

  sum=0
  for line in lines:
    line=line.strip()
    if line.startswith("0x"):
      broj=int(line,16)
      if broj%10==3:
        sum+=broj
  print(f"Suma brojeva koji se zavrsavaju cifrom 3 je {sum}")

    
if __name__ == "__main__":
  main()
  
  
#zad13###########################
def append_to_file(list_of_product):
  
    with open("products.csv", "a") as file:
       file.write("Naziv, Opis, Godina, Kolicina, Cijena\n")
       for product in list_of_product:
         naziv = product["naziv"]
         opis = product["opis"]
         godina = product["godina"]
         kolicina = product["kolicina"]
         cijena = product["cijena"]

         line = f"{naziv}, {opis}, {godina}, {kolicina}, {cijena}\n"
         file.write(line)

    print("Zavrseno")

lista = [
    {"naziv": "majica", "opis": "kratkih rukava", "godina": 2022, "kolicina": 10, "cijena": 30},
    {"naziv": "cokolada", "opis": "sa ljesnicima", "godina": 2024, "kolicina": 15, "cijena": 5}
]
print(append_to_file(lista))


def get_products_older_than(year):
  products = []
  with open("products.csv", "r") as file:
      for line in file:
          name, description, prod_year, quantity, price = line.strip().split(", ")
          prod_year = int(prod_year)
          if int(prod_year) >= int(year):
            products.append({"naziv": name,"opis": description,"godina": prod_year,"kolicina": int(quantity),"cijena": float(price)})
  return products

result = get_products_older_than(2023)
for product in result:
  print(f"{product['naziv']}, {product['opis']}, {product['godina']}, {product['kolicina']},{product['cijena']}")




def max_possible_revenue(products):
  uk_prihod = 0
  for product in products:
      kolicina = product.get("kolicina", 0)
      cijena = product.get("cijena", 0)
      uk_prihod += kolicina * cijena
      
  print(f"Maksimalni prihod je: {maksimalni_prihod}")
  return uk_prihod
  
  maksimalni_prihod = max_possible_revenue(lista)




#zad14#########################
def append_to_file(list_of_students):
  
  with open("students.txt", "a") as file:
    for student in list_of_students:
        ime = student["ime"]
        prezime = student["prezime"]
        godina = student["godina"]
        prosjek = student["prosjek"]
        file.write(f"{ime},{prezime},{godina},{prosjek}\n")


students = [
  {"ime": "milica", "prezime": "vukcevic", "godina": 3, "prosjek": 8},
  {"ime": "marko", "prezime": "markovic", "godina": 2, "prosjek": 8.9},
  {"ime": "Ana", "prezime": "Jankovic", "godina": 4, "prosjek": 7.1},
]

append_to_file(students)




def get_students_with_greater_grade(year, grade):

  GRADES_PATTERN = {
    'A': [9.5, 10],
    'B': [8.5, 9.5],
    'C': [7.5, 8.5],
    'D': [6.5, 7.5],
    'E': [6, 6.5]
  }

  def check_grade(score, pattern):
    for g, score_range in pattern.items():
        if score_range[0] <= score < score_range[1]:
            return g
    raise ValueError("Invalid grade range")

  students = [
    {"ime": "Marko", "prezime": "Markovic", "godina": 2, "prosjek": 8.6},
    {"ime": "Boris", "prezime": "Boricic", "godina": 3, "prosjek": 7.9},
    {"ime": "Novak", "prezime": "Novovic", "godina": 3, "prosjek": 6.9}
  ]

  filtered_students = []
  for student in students:
    if student["godina"] == year and check_grade(student["prosjek"], GRADES_PATTERN) == grade :
      filtered_students.append(student)

  return filtered_students


result = get_students_with_greater_grade(3, "D")
print(result)


#zad15##################################
def validate_credit_card(card_number: str) -> bool:
  card_number = [int(num) for num in card_number]
  checkDigit = card_number.pop(-1)
  card_number.reverse()
  card_number = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]
  card_number = [num - 9 if idx % 2 == 0 and num > 9 else num for idx, num in enumerate(card_number)]
  card_number.append(checkDigit)
  checkSum = sum(card_number)
  return checkSum % 10 == 0

if __name__ == '__main__':
  print(validate_credit_card('378282246310005')) 
  print(validate_credit_card('371449635398431')) 
  print(validate_credit_card('7762888103111881')) 
  print(validate_credit_card('3533747323060364'))  
  
  







