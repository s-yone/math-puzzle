#coding: UTF-8
from collections import deque

#bin_num = 0b10
#ct_num = 0o10
#hex_num = 0x10

def check(int_num):
    list1 = []
    list2 = list(str(int_num))
    while len(list2) != 2:
        list1.append(list2.pop())
    return list1

def num_check(int_num):
    list1 = []
    list2 = list(str(int_num))
    while len(list2) != 0:
        list1.append(list2.pop())
    return list1

num = 10
while True:
    if list(str(num)) != num_check(num):
        num +=1
        continue
    bin_num = bin(num)
    if list(bin_num[2:]) != check(bin_num):
        num +=1
        continue
    oct_num = oct(num)
    if list(oct_num[2:]) == check(oct_num):
        print(num)
        print(bin_num)
        break
    num +=1


#char1 = split(bin_num)
    

