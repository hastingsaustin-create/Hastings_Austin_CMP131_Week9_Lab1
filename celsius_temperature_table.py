#Austin Hastings
#CMP 131 86520
#Week 9
#Lab 1
#Kinetic Energy
#12 NOV 2026
print("Celcius")
print("-------")

def celsius (f):
    c = 0.55556 * (f-32)
    print(f," ",c)
def main():
    for f in range (21):
        celsius(f)
main()