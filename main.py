
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


print("--- 11 uzduotis ---")
my_sum = 0
count = 0
my_avg = 0
while True:
    my_num = int(input("Iveskite skaiciu (0, -1 - sustabdys cikla): "))
    if my_num in [0, -1]:
        break
    my_sum += my_num
    count += 1
    my_avg = my_sum/count
print(f"suma: {my_sum}; vidurkis: {my_avg}")


print("--- 12 uzduotis ---")



