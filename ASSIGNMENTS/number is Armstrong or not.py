num = int(input("Enter a number: "))
original = num
sum_of_powers = 0
n = len(str(num))

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** n
    num //= 10

if sum_of_powers == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
