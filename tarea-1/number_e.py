# Calculate the value of e to the nth digit

import math
import decimal



def main():
    # Get the number of digits to calculate
    n = int(input("Enter the number of digits to calculate: "))

    file_to_write = 'e.txt'
    
    # Set the precision of the decimal module
    decimal.getcontext().prec = n + 1

    # Calculate the value of e with n decimal places
    # and store all the decimal in file to write
    
    with open(file_to_write, 'w') as file:
        e = decimal.Decimal(0)
        for i in range(n):
            e += decimal.Decimal(1) / math.factorial(i)
        file.write(str(e) + '\n')
    
if __name__ == "__main__":
    main()