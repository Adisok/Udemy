# FileNotFound

try:
    f = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    f = open("a_file.txt", "w")
    f.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist ")
else:
    print(f.read())
    print("It worked so hard but in the end it dosen't even matter")
finally:
    f.close()
    print("file was closed")
    # raise KeyError("This is an my error")

height = float(input("Height: "))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError("Type human height!")

bmi = weight/height**2
print(bmi)
