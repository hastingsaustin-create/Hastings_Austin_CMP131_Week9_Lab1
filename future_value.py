#Austin Hastings
#CMP 131 86520
#Week 9
#Lab 1
#future value
#12 NOV 2026
print("future value")
print("------------")

def future_value(p, i, m):
    f = p * (1 + i)**m
    
def display(f):
    print("The future value is: ", f)

def main():
    p = float(input("Enter the present value: "))
    interest = float(input("Enter the the monthly interest rate percentage: "))
    i = float(interest / 100 )
    m = int(input("Enter the number of months: "))
    f = future_value(p, i, m)
    display(f)
main()