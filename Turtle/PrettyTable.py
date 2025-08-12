from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["pickachu","skitty","charmander"])
table.add_column("type",["Electric","water","fire"])
table.align = "l"
print(table)