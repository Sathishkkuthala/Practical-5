fh = open("prac 5.txt",'w')
year = int(input("Enter a year to check if it's a leap year: "))
if (year % 4 == 0 ):
    fh.write(f"{year} is a leap year!")
else: 
    fh.write(f"{year} is not a leap year.") 
fh.close()