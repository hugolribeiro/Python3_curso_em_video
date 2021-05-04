# Objective: Make a program that have a function called write(). This function will receive a text and will print this text within lines.
# Programmer: Hugo Leça Ribeiro

def write(text):
    line = "~"
    for letter in range(0, len(text)):
        line += "~"
    print(f'{line}\n{text}\n{line}')


write("Hugo Leça Ribeiro")
write("Python Student")
write("FATEC")
