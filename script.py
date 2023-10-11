hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

def checkin():
    check = False
    while check == False:
        floor = input("Enter the floor number: ")
        if floor == "1" or floor == "2" or floor == "3":
            check = True
        else:
            print("Not a valid floor number. Enter a number 1-3")
    room = input("Enter the room number: ")
    if room in hotel[floor]:
        print("This room is already occupied. Try again")
        return
    occ = int(input("How many occupants will be in the room? "))
    count = 0
    people = []
    while count < occ:
        person = input(f"Enter name of occupant number {count + 1}: ")
        people.append(person)
        count += 1
    hotel[floor][room] = people
    print("You are checked in.")
    display()

def checkout():
    check = False
    while check == False:
        floor = input("Enter the floor number: ")
        if floor == "1" or floor == "2" or floor == "3":
            check = True
        else:
            print("Not a valid floor number. Enter a number 1-3")
    room = input("Enter the room number: ")
    if room not in hotel[floor]:
        print("This room is not occupied. Try again")
        return
    del hotel[floor][room]
    print("You are checked out.")
    display()

def display():
    for floor in hotel:
        print(f"\n\nFloor {floor}")
        for room in hotel[floor]:
            print(room, end=": ")
            people = len(hotel[floor][room])
            counter = 1
            for person in hotel[floor][room]:
                if counter < people:
                    print(person, end=", ")
                    counter += 1
                else:
                    print(person)

status = False

while (status == False):
    action = input("\nDo you want to check in or check out? Type in or out.\nYou can also type quit to exit the app\nEnter your text here: ")
    if action == "quit":
        status = True
        continue
    if action == 'in':
        checkin()
    elif action == 'out':
        checkout()
    else:
        print("Not a valid response, try again")