#leap year
year=int(input('Enter the number'))
if year%400==0 or (year%4==0 and year%100!=0):
    print("The year is Leap year")
else:
    print('The year is not a leap year')
