def distance_to_miles(dist):
  miles = dist / 1.609

  print(f"The distance in miles is {miles:.2f} miles")

km = int(input("Enter a distance in Km: "))

distance_to_miles(km)