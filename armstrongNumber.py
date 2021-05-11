number1=int(input("Enter a number:"))
number2=number1

length_of_number = len(str(number1))

sum1=0

while number1 > 0:

    digit = number1 % 10
    number1 = number1 // 10
    sum1 = sum1 + pow(digit, length_of_number) #pow() function
# print(sum1)

if sum1 == number2:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")