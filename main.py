
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

# --- 1 uzduotis ---
