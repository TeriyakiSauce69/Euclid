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

#Recursive Algorithm to find GCD of two Inputs
def Recursive(x,y):
    if y == 0:
        return x
    else:
        return Recursive(y ,x % y)



def main():
    #for x in range(5, 500, 9):
        #start =time.perf_counter()

        #y =random.randint(1,10)
        #answer = Euclid(x,2 * y)
        #answer2 = Recursive(x, 2 * y)

        #end = time.perf_counter()


        #start2 = time.perf_counter()
        #answer2 = Recursive(x, 2 * x)
        #end2 = time.perf_counter()


        #start3 = time.perf_counter()
        #answer3 = ConIntCheck(x, 2 * x)
        #end3 = time.perf_counter()

        #print(x, "\t",end - start, "\t", end2 - start2, "\t",end3 - start3 )
        #print(answer,answer2,  "\t", x, y)

    print(Euclid(250, 111))
    # print(Euclid(111,250))

if __name__ == "__main__":
    main()