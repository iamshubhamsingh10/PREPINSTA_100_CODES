#palindrome
num = 1234
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
if num == reverse:
    print("It is a plaindorme")
else:
    print("It is not a plaindorme")

