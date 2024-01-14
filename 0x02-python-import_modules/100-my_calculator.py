#!/usr/bin/python3

#this is a  program that imports all functions from the file calculator_1.py and handles basic operations
#operators for my calculator are addition, subtrction, multiplacation and subtraction
#argc is an integer representing the number of arguments of the program
#len is a function that returns the number of items in an object

if __name__ == '__main__':

    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv)
    result = 0
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*' and\
       sys.argv[2] != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
    print('{:d} {} {:d} = {:d}'.format(int(sys.argv[1]), sys.argv[2],
                                       int(sys.argv[3]), result))
