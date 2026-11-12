#Austin Hastings
#CMP 131 86520
#Week 9
#Lab 1
#Kinetic Energy
#12 NOV 2026
print("Kinetic Energy")
print("--------------")

def sum(m, v):
    ke = .5 * m * (v * v)
    return ke

def display(ke):
    print("The kinetic energy is: ", ke)

def main():
    m = float(input("Enter the object's mass in kilograms: "))
    v = float(input("Enter the objects velocity: "))
    ke = sum (m, v)
    display(ke)
main()