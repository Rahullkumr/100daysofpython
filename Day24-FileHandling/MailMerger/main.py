with open("Input/Names/invited_names.txt") as invited_names:
    invited = invited_names.readlines()


with open("Input/Letters/starting_letter.txt") as letter_bp:    #blueprint
    letter = letter_bp.readlines()

greeting_line = letter[0]
rest_of_letter = letter[1:]

for person in invited:
    name = person.strip('\n')
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "x") as ready:
        ready.write(greeting_line.replace("[name],", f"{name},\n"))
        for line in rest_of_letter:
            ready.write(f"{line}")

