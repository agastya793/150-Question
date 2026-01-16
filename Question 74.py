#  Write a program to repeatedly sum the digits of a number until the result is zero.

def sum_digits_until_zero(num):
    while num != 0:
        total = 0

        # Sum the digits of the number
        while num > 0:
            digit = num % 10
            total += digit
            num = num // 10

        print("Sum of digits:", total)

        # Replace num with the sum
        num = total

    print("Result is zero. Process stopped.")
