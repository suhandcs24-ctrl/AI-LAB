roomA = input("Enter Room A status (clean/dirty): ")
roomB = input("Enter Room B status (clean/dirty): ")

location = input("Enter vacuum location (A/B): ")

while roomA == "dirty" or roomB == "dirty":

    if location == "A":
        if roomA == "dirty":
            print("A is dirty -> Cleaning A")
            roomA = "clean"
        else:
            print("A is clean -> Move to B")
            location = "B"

    else:
        if roomB == "dirty":
            print("B is dirty -> Cleaning B")
            roomB = "clean"
        else:
            print("B is clean -> Move to A")
            location = "A"

print("Both rooms are clean!")
