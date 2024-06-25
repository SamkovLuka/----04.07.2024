import random


#1)
list1 = []
for i in range(5):
    list1.append(random.randint(-100,100))
list2 = []
for i in range(5):
    list2.append(random.randint(-100,100))
print(f"перший список = {list1}")
print(f"другий список = {list2}")
num1 = list1[3]
num2 = list2[1]
num3 = list1[4]
num4 = list2[0]
num5 = list1[2]
list3 = []
list3.append(num1)
list3.append(num2)
list3.append(num3)
list3.append(num4)
list3.append(num5)
print(f"третій список = {list3}")



#2)
list1 = []
for i in range(5):
    list1.append(random.randint(-100,100))
list2 = []
for i in range(5):
    list2.append(random.randint(-100,100))
print(f"перший список = {list1}")
print(f"другий список = {list2}")
list3_1 = []
num1 = list1[3]
num2 = list2[1]
num3 = list1[4]
num4 = list2[0]
num5 = list1[2]
if num1 == num2 == num3 == num4 == num5:
    list3_1.remove(num1, num2)
    print(f"третій список = {list3_1}")
else:
    list3_1.append(num1)
    list3_1.append(num2)
    list3_1.append(num3)
    list3_1.append(num4)
    list3_1.append(num5)
    print(list3_1)
    print(f"третій список = {list3_1}")



#3)
list1 = []
for i in range(5):
    list1.append(random.randint(-100,100))
list2 = []
for i in range(5):
    list2.append(random.randint(-100,100))
print(f"перший список = {list1}")
print(f"другий список = {list2}")
list3_2 = []
num1 = list1[3]
num2 = list2[1]
num3 = list1[4]
num4 = list2[0]
num5 = list1[2]
if num1 == num2 == num3 == num4 == num5:
    list3_2.append(num1)
    list3_2.append(num2)
    list3_2.append(num3)
    list3_2.append(num4)
    list3_2.append(num5)
    print(f"третій список = {list3_2}")
else:
    list3_2.remove(num1, num2)
    print(list3_2)
    print(f"третій список = {list3_2}")


#4)
list1 = []
for i in range(5):
    list1.append(random.randint(-100,100))
list2 = []
for i in range(5):
    list2.append(random.randint(-100,100))
print(f"перший список = {list1}")
print(f"другий список = {list2}")
list3_3 = []
num1 = list1[3]
num2 = list2[1]
num3 = list1[4]
num4 = list2[0]
num5 = list1[2]
if num1 != num2 != num3 != num4 != num5:
    list3_3.append(num1)
    list3_3.append(num2)
    list3_3.append(num3)
    list3_3.append(num4)
    list3_3.append(num5)
    print(f"третій список = {list3_3}")
else:
    list3_3.remove(num1, num2)
    print(list3_3)
    print(f"третій список = {list3_3}")


#5)
list1 = []
for i in range(5):
    list1.append(random.randint(-100,100))
list2 = []
for i in range(5):
    list2.append(random.randint(-100,100))
print(f"перший список = {list1}")
print(f"другий список = {list2}")
list3_4 = []
num1 = list1[3]
num2 = list2[1]
num3 = list1[4]
num4 = list2[0]
num5 = list1[2]
if num1 == min(list1):
    list3_4.append(num1)
elif num1 == max(list1):
    list3_4.append(num1)
if num2 == min(list2):
    list3_4.append(num2)
elif num2 == max(list2):
    list3_4.append(num2)
if num3 == min(list1):
    list3_4.append(num3)
elif num3 == max(list1):
    list3_4.append(num3)
if num4 == min(list2):
    list3_4.append(num4)
elif num4 == max(list2):
    list3_4.append(num4)
if num5 == min(list1):
    list3_4.append(num5)
elif num5 == max(list1):
    list3_4.append(num5)
print(f"третій список = {list3_4}")


