import argparse
from fib_lib import *

def main(method):
    print(method)
    if method == 'recursion':
        for i in range(36):
            print('fib(' + str(i) + ') =', fib(i))
    elif method == 'fast':
        for i in range(40):
            print('fib(' + str(i) + ') =', fast_fib(i))
    else:
        print('Method not implemented.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fib main functions')
    parser.add_argument('--method', help='method')
    args = parser.parse_args()

    main(args.method)


