"""
Llacki B.P.
CSC 592
"""
import math, time, random

#Euclid Algorithm to find GCD of two Inputs
def Euclid(x,y):
    print('i',"\t",'q',"\t", 'm',"\t", 'n',"\t", 'r',"\t", 't')
    print('-------------------------------------------------------------')

    t, lastt = 0, 1
    #print("t, lastt" , t, lastt)

    p = 0

    if x < y:
        x,y = y,x

    still_x = x

    i = 0


    list = []
    while y != 0:
        r = x % y

        print(i,"\t", (x // y),"\t", x,"\t", y,"\t", r,"\t", t)
        list.append((x // y))

        i += 1

        if i > 2:
            #print(t,"should be 0,", lastt,"Should be 1", list[i - 3])
            #print("Should be -1",(t - (lastt * list[i - 3])))
            #print("Should be 26", still_x)
            p = (t - (lastt * list[i - 3])) % still_x

            #print(list[i - 3])

            print("Here", p)

            t, lastt = lastt, p
            #print("t, lastt", t, lastt)


        x = y
        y = r
    #print(t, lastt, list[i-3],still_x)

    print("This is the multplicative inverse, ti , we care about! ", (t - (lastt * list[i - 2])) % still_x)


    #print(0-3)
    #print("This should be 25",-1 % 26)

    # for z in list:
    #     print(z)
    # print("DIS", list[5 - 3])







    print('STOP')
    return x

def main():
    da_list = []

    # while True:
    #     try:
    #         num = int(input("Enter an integer: "))
    #     except ValueError:
    #         print("Please enter a valid integer pls!")
    #         continue
    #     da_list.append(num)
    #
    #     try:
    #         num = int(input("Enter Second Integer: "))
    #     except ValueError:
    #         print("Please enter a valid integer pls!")
    #         continue
    #     da_list.append(num)
    #
    #     break

    #print(Euclid(da_list[0], da_list[1]))
    print(Euclid(28,75))


if __name__ == "__main__":
    main()