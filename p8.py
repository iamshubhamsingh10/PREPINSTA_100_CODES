#prime number
prime=int(input('Enter the number'))
if prime%2==1 or (prime%prime==0 and prime%2==1):
    print("It is prime number")
else:
    print("it is not prime")