"""
Llacki B.P.
CSC 592
"""
import math, time, random

#Euclid Algorithm to find GCD of two Inputs
def Euclid(x,y):
    print('i',"\t",'q',"\t", 'm',"\t", 'n',"\t", 'r')
    print('----------------')
    if x < y:
        x,y = y,x

    i = 0
    while y != 0:
        r = x % y

        print(i,"\t", (x // y),"\t", x,"\t", y,"\t", r)

        x = y
        y = r
        i+=1

    print('STOP')
    return x

def main():
    da_list = []

    while True:
        try:
            num = int(input("Enter an integer: "))
        except ValueError:
            print("Please enter a valid integer pls!")
            continue
        da_list.append(num)

        try:
            num = int(input("Enter Second Integer: "))
        except ValueError:
            print("Please enter a valid integer pls!")
            continue
        da_list.append(num)

        break

    print(Euclid(da_list[0], da_list[1]))


if __name__ == "__main__":
    main()