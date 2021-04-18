
with open("./Input/Letters/starting_letter.txt","r") as letter:
    blank = letter.read()

with open("./Input/Names/invited_names.txt", "r") as file_names:
    names_list = file_names.readlines()
    for i in range(len(names_list)):
        names_list[i] = names_list[i].replace("\n", "")
        with open(f"./Output/ReadyToSend/letter_for_{names_list[i]}", "w") as send_letter:
            send_letter.write(blank.replace("[name]", f"{names_list[i]}"))