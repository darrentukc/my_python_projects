# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ['Pokemon Name', 'Type']
# table.add_row(['Pikachu', 'Electric'])
# table.add_row(['Squirtle', 'Water'])
# table.add_row(['Charmander', 'Fire'])
table.add_column('Pokemon', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align['Pokemon'] = 'l'
print(table.align)
print(table)

