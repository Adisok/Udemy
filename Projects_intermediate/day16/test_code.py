from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Bulbasaur", "Charmander"])
table.add_column("Type", ["Electric", "Grass", "Fire"])

table.align = "l"


print(table)