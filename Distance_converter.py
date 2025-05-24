print("Distance program km -> mi")
print("")
def distance_km():
    while True:
     distance = float(input("Please enter distance in km: "))
     if distance > 0: 
        mi = distance * 0.621
        print(f"Distance: {distance}km, Miles: {mi:.1f} miles")
        break
     else:
        print("Invalid input. Distance must be greater than zero.")
     
     
        
while True:
    strt = input("Would you like to perform distance calculation? y/n: ").lower()
    if strt == "y":
          distance_km()
    elif strt != "y":
        print("Program has now ended. Please restart program to begin. Enter y to start.")
        break