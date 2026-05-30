#this program was found as a practice function on pynative.com
#program should create a function that can accept variable number of arguments and print them all
def func1(*args):
    print("Printing Values:")
    for i in args:
        print(i)

#calling with 5 arguments
func1(10, 20, 30, 40, 50)

#calling with 10 arguments
func1(61, 62, 63, 64, 65, 66, 67, 68, 69, 70)

