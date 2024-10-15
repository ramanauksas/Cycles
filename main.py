import random

# for ciklo uzduotys

# 1 uzduotis
for i in range(5):
    print("Tomas")

# 2 uzduotis
for i in range(11):
    print(i)

# 3 uzduotis
for i in range(0,16,2):
    print(i)

# 4 uzduotis
for i in range(0,21,2):
    print(f"[{i}]")

# 5 uzduotis
for i in range(1,21):
    if i % 4 == 0:
        print(i)

# 6 uzduotis
for i in range(1,16):
    if i % 2 == 0:
        print(f"{i} - lyginis")
        continue
    print(f"{i} - nelyginis")

# 7 uzduotis
r1 = 10
r2 = 15
if r1<r2:
    for i in range(r1, r2+1):
        print(f"{i} {i**2}")

# 8 uzduotis
r1 = 10
r2 = 20
if r1<r2:
    for i in range(r1,r2+1):
        if i % 2 !=0 or i % 8 == 0:
            print(i)


# # 9 uzduotis
# name = input("Iveskite varda")
# for l in name:
#     print(f"Labas, {name}!")


# 10 uzduotis
for elementas in [88, 65, 21, 26, 47]:
    if elementas % 2 == 0:
        print(elementas)


# # 11 uzduotis
# r1 = int(input("Iveskite zemutini rezi"))
# r2 = int(input("Iveskite virsutini rezi"))
# step = int(input("Iveskite zingsni"))
# even = input('Iveskite: "Lyginis" ar "Nelyginis"')
#
# if r2>r1:
#     for i in range(r1, r2, step):
#         if i%2==0 and even=="Lyginis":
#             print(i)
#         if i%2!=0 and even=="Nelyginis":
#             print(i)
# else:
#     print("Reziai blogi!")


# # 12 uzduotis
# height = int(input("Iveskite eglutes auksti"))
# my_string = "*"
# for i in range(height):
#     print(my_string)
#     my_string += "*"

# # 13 uzduotis
# word = input("Iveskite zodi: ")
# repeat = int(input("Kiek kartu kartosim kiekviena raide? "))
# for letter in word:
#     print(letter*repeat)

# 14 uzduotis
print("--- 14 uzduotis ---")
num1 = 2
num2 = 5
result = 0
for i in range(2):
    result += num2
print(result)

print("--- 15 uzduotis ---")
result=0
for i in range(1, 101):
    result += i
print(f"Sveiku skaiciu nuo 1 iki 100 suma: {result}")

print("--- 16 uzduotis ---")
result = 0
for i in range(20,51):
    if i%2==0:
        result += i
print(f"Sveiku lyginiu skaiciu nuo 20 iki 50 suma: {result}")

print("--- 17 uzduotis ---")
result = 0
for i in range(30,61):
    if i%2!=0:
        result += i
print(f"Sveiku nelyginiu skaiciu nuo 30 iki 60 suma: {result}")

print("--- 18 uzduotis ---")
result=0
for i in range(1000):
    if i%3==0 or i%5==0:
        result+=i
print(result)

print("--- 19 uzduotis ---")
for i in range(1, 101):
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

print("--- 20 uzduotis ---")
length = 10
int1 = 2
int2 = 1
print(int1)
print(int2)
for i in range(2, length+1):
    int3 = int1 + int2
    print(int3)
    int1 = int2
    int2 = int3


# While ciklai

print("--- 1 uzduotis ---")
i=0
while i<20:
    i += 1
    print(i)

print("--- 2 uzduotis ---")
i=0
while i<50:
    i+=1
    if i%2==0:
        print(f"{i} - lyginis")
    else:
        print(f"{i} - nelyginis")

print("--- 3 uzduotis ---")
i=24
while i<50:
    i +=1
    if i%3==0:
        print("dalinasi is 3")
    else:
        print(i)

print("--- 4 uzduotis ---")
i=0
while True:
    i += 1
    if i%7==0:
        break
    print(i)

print("--- 5 uzduotis ---")
i=0
while True:
    i += 1
    if i%15==0:
        break
    print(i)

# print("--- 6 uzduotis ---")
# while True:
#     r1 = int(input("Iveskite zemutini rezi: "))
#     r2 = int(input("Iveskite virsutini rezi: "))
#     if r2>r1:
#         break
#     print("Blogi reziai!")
# for i in range(r1,r2):
#     print(f'{i} - {"lyginis" if i%2==0 else "nelyginis"}, {i**2}')

print("--- 7 uzduotis ---")
i = 0
while True:
    i+=1
    print(i)
    if i>20:
        pirminis = True
        for x in range(2, i):
            if i % x == 0:
                pirminis = False
                break
        if pirminis == True:
            break

# print("--- 8 uzduotis ---")
# result = 0
# while True:
#     my_num = int(input("Iveskite skaiciu (Ivedus nuli skaiciuosim suma): "))
#     result += my_num
#     if my_num == 0:
#         break
# print(f"Ivestu skaiciu suma: {result}")


# print("--- 9 uzduotis ---")
# while True:
#     num1 = int(input("Iveskite pirma skaiciu: "))
#     num2 = int(input("Iveskite antra skaiciu: "))
#     print(f"{num1}+{num2}={num1+num2}\n{num1}-{num2}={num1-num2}\n{num1}*{num2}={num1*num2}\n{num1}/{num2}={num1/num2}")
#     more = input("Vedam dar? (T/N): ")
#     if more!="T":
#         break

# print("--- 10 uzduotis ---")
# while True:
#     num1 = int(input("Iveskite skaiciu nuo 1 iki 9: "))
#     for i in range(1,10):
#         print(f"{num1} * {i} = {num1*i}")
#     more = input("Kartojam? (T/N): ")
#     if more!="T":
#         break


# print("--- 11 uzduotis ---")
# my_sum = 0
# count = 0
# my_avg = 0
# while True:
#     my_num = int(input("Iveskite skaiciu (0, -1 - sustabdys cikla): "))
#     if my_num in [0, -1]:
#         break
#     my_sum += my_num
#     count += 1
#     my_avg = my_sum/count
# print(f"suma: {my_sum}; vidurkis: {my_avg}")


# print("--- 12 uzduotis ---")
# while True:
#     name = input("Iveskite studento varda: ")
#     my_sum = 0
#     count = 0
#     my_avg = 0
#     while True:
#         my_num = int(input("Iveskite pazymi (0, -1 - sustabdys cikla): "))
#         if my_num in [0, -1]:
#             break
#         my_sum += my_num
#         count += 1
#         my_avg = my_sum/count
#     print(f"Studento ({name}) pazymiu vidurkis: {my_avg}")
#     more = input("Skaiciuojam kitam studentui? (T/N): ")
#     if more!="T":
#         break

# print("--- 13 uzduotis ---")
# while True:
#     r1 = int(input("Pasirinkite zemutini rezi"))
#     r2 = int(input("Pasirinkite virsutini rezi"))
#     if r2>r1:
#         break
#     print("Blogi reziai!")
# while True:
#     allow_help = input("Ar reikes pagalbos spejant? (T/N)")
#     if allow_help.lower() in ["t", "n"]:
#         break
#     print("Nesupratau atsakymo!")
# while True:
#     max_guesses = input("Kiek leidziama spejimu? (-1 reikš neribotai)")
#     try:
#         max_guesses = int(max_guesses)
#         break
#     except:
#         print("Iveskite skaiciu!")
#
# secret_num = random.randint(r1, r2)
# current_try = 0
# while True:
#     current_try += 1
#     guess = int(input(f"Spekite skaiciu nuo {r1} iki {r2}"))
#     if allow_help:
#         if guess > secret_num:
#             print("Bandykite mazesni!")
#         elif guess < secret_num:
#             print("Bandykite didesni!")
#         else:
#             print("Atspejote!")
#             break
#     else:
#         if guess == secret_num:
#             print("Atspejote!")
#             break
#     if current_try == max_guesses:
#         print("Isnaudojote visus bandymus. Neatspejote!")
#         break

#  Is python 11 - sarasai
print("--- 16 uzduotis ---")
word_list = ["mano", "sarasas", "su", "pasirinktais", "zodziais"]
word_string_comma = ", ".join(word_list)
word_string_vertical = "|".join(word_list)
word_string_space = " ".join(word_list)
print(word_string_comma)
print(word_string_vertical)
print(word_string_space)

print("--- 17 uzduotis ---")
language, environment, *files = ["python", "web", "myfile1", "myfile2", "myfile3"]
print(language)
print(environment)
print(files)

print("--- 18 uzduotis ---")
coworkers = ["Jonas Jonaitis", "Petras Petraitis", "Jonas Kazlauskas"]
print("Prie projekto dirba sie komandos nariai:")
for worker in coworkers:
    print(worker)

print("-- 19 uzduotis ---")
themes = ["variables", "strings", "conditional sentences", "for loops", "while loops"]
print("Mes jau mokemes:")

for theme in themes:
    print(theme)

while True:
    try:
        theme = themes.pop(0)
        print(theme)
    except:
        break

print("--- 20 uzduotis ---")
courses = ["web development", "data analytics", "data science", "machine learning"]
for course in courses:
    print(course)


print("--- 21 uzduotis ---")
countries = ["Lithuania", "Latvia", "Estonia", "Poland"]
for country in countries:
    print(f"Šalis: {country}")

print("--- 22 uzduotis ---")
cart = ["Duona", "Batonas", "Sviestas", "Ledai"]
for i, product in enumerate(cart):
    print(f"Pirkinys Nr. {i}: {product}")

print("-- 23 uzduotis ---")
grades = [8, 9, 10, 8, 9, 7, 6, 9, 10]
grades.sort()
for grade in grades:
    if grade == 10:
        comment = "puikiai"
    if grade == 9:
        comment = "labai gerai"
    if grade == 8:
        comment = "gerai"
    if grade == 7:
        comment = "pakankamai"
    if grade == 6:
        comment = "patenkinamai"
    if grade == 5:
        comment = "silpnai"
    if grade == 4:
        comment = "nepatenkinamai"
    if grade == 3:
        comment = "prastai"
    if grade == 2:
        comment = "labai prastai"
    if grade == 1:
        comment = "kosmaras"
    if grade == 0:
        comment = "nepaduota"
    print(f"{grade} - {comment}")

# print(" --- 24 uzduotis ---")
# num_of_numbers = int(input("Kiek generuosim skaiciu? "))
# num_list = []
# for i in range(num_of_numbers):
#     num_list.append(random.randint(0,100))
# print(num_list)
# for num in num_list:
#     print(f"{num}; {num**2}")

print("--- 25 uzduotis ---")
initial_list = ["list", "with", "initial", "information"]
print("initial list: ", initial_list)
initial_list[0] = "sarasas"
initial_list[2] = "pradine"
initial_list[3] = "informacija"
print("changed list: ", initial_list)

print("--- 26 uzduotis ---")
numbers = [1, 2, 5, 7, 9, 10, 15, 10, 14, 16, 21, 22]
print("Lyginiai skaiciai:")
for num in numbers:
    if num %2 ==0:
        print(num)
print("Visi nelyginiai skaiciai: ")
for num in numbers:
    if num%2!=0:
        print(num)
print("Visi skaiciai, kurie dalijasi is 3: ")
for num in numbers:
    if num%3==0:
        print(num)

print("--- 28 uzduotis ---")
numbers = [2, 5, 7, 9, 10, 15, 10, 14, 16, 21, 22]
for number in numbers:
    multipliers = []
    for i in range(0, number+1):
        if i!=0 and i!=1 and number%i==0:
            multipliers.append(str(i))
    multipliers_list = ", ".join(multipliers)
    print(f"Skaicius {number} dalinasi is {multipliers_list}")

# print("--- 29 uzduotis ---")
# num_words = int(input("Kiek norite ivesti zodziu? "))
# word_list = []
# for i in range(num_words):
#     word = input("Iveskite zodi: ")
#     word_list.append(word)
# print("Zodziu sarasas: ", word_list)

print("--- 30 uzduotis ---")
my_list=["my", "random", "word", "list"]
for word in my_list:
    print(f"word: {word}; number of letterS: {len(word)}")















