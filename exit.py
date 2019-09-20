#! usr/bin/env python3
'''exit.py by Ahmet Bolat,
This script will calculate your potential exit points.
'''

def main():
    position = input('Enter L for Long or S for Short = ').lower()
    shares = float(input('Enter position size = '))
    avg_cost = float(input('Enter average cost of shares = '))
    
    if position == 'l':
        print('$25 = ' + str(round(25 / shares + avg_cost, 2)) + '\n') 
        print('$50 = ' + str(round(50 / shares + avg_cost, 2)) + '\n')
        print('$75 = ' + str(round(75 / shares + avg_cost, 2)) + '\n')
        print('$100 = ' + str(round(100 / shares + avg_cost, 2)) + '\n')
        print('$125 = ' + str(round(125 / shares + avg_cost, 2)) + '\n')
        print('$150 = ' + str(round(150 / shares + avg_cost, 2)) + '\n')
        print('$175 = ' + str(round(175 / shares + avg_cost, 2)) + '\n')
        print('$200 = ' + str(round(200 / shares + avg_cost, 2)) + '\n')
    
    elif position == 's':
        print('$25 = ' + str(round(avg_cost - 25 / shares, 2)) + '\n')
        print('$50 = ' + str(round(avg_cost - 50 / shares, 2)) + '\n')
        print('$75 = ' + str(round(avg_cost - 75 / shares, 2)) + '\n')
        print('$100 = ' + str(round(avg_cost - 100 / shares, 2)) + '\n')
        print('$125 = ' + str(round(avg_cost - 125 / shares, 2)) + '\n')
        print('$150 = ' + str(round(avg_cost - 150 / shares, 2)) + '\n')
        print('$175 = ' + str(round(avg_cost - 175 / shares, 2)) + '\n')
        print('$200 = ' + str(round(avg_cost - 200 / shares, 2)) + '\n')
    
    else:
        print('Something went wrong!')
#    print('See you soon!')


if __name__ == '__main__':
    main()
