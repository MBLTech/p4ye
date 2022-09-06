def hint_username(username):
    if len(username) <= 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        return username


name_prompt = input("Choose Your username: ")

if True:
    validity_username = hint_username(name_prompt)
    if validity_username != None:
        print("Welcome " + str(validity_username) + " to the Department")
