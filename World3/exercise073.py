# Exercise 073: Tuples with football teams
# Make a tuple filled with the top 20 soccer teams of Brazilian Football Championship.
# Show the top 5
# The lasts 4 teams
# The teams in alphabetic order
# The position of Corinthians

teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Altético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')

print('-=' * 15)
print(f'Full list: {teams}')
print('-=' * 15)
print(f'The top five teams: {teams[0:5]}')
print('-=' * 15)
print(f'The last 4 teams: {teams[-4:]}')
print('-=' * 15)
print(f'Teams in alphabetic order: {sorted(teams)}')
print('-=' * 15)
print(f'The Corinthians is in {teams.index("Corinthians")+1}ª position')
