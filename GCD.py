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
    print(Euclid(250, 111))


if __name__ == "__main__":
    main()