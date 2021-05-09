# Make a program that has a function named history(),
# that will receive two optionals parameters: the name of a soccer player and how many gols he did.
# The program will be capable to show this history, even that some data did not inputted.

# Programmer: Hugo Leça Ribeiro

def history(name_func='<unknow>', gols_func=0):
    print(f'The player {name_func} did {gols_func} gols in the championship')


name = str(input('Player name: '))
gols = str(input('Number of gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name.strip() == '':
    history(gols_func=gols)
else:
    history(name, gols)
