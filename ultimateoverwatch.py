import time

print("Hello Ultimate Overwatch User")
time.sleep(.5)
print("Would You Like To Look For:")
print("1. Team Comp")
print("2. Counters")
owCategory = input("Enter The Numerical Value: ")
if owCategory == "1":
    print("This Feature Isn't Availible Yet.")
elif owCategory == "2":
    print("Select A Character")
    print("Zarya")
    print("Mercy")
    print("Pharah")
    owCountersChar = input("Who would you like to counter? ")
    if owCountersChar == "Zarya":
        print("Reccomended Counters Are:")
        print("Pharah - DPS")
        print("Sombra DPS")
        print("Zenyatta - Support")
        print("Bastion - DPS")