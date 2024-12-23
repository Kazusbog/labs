try:
    with open('example.txt') as file:
        content = file.read()
        print(content)
    with open ('example.txt') as file:
        lines = [line for line in file]
    with open('hamster combat.txt') as file:
        content = file.read()
except FileNotFoundError:
    print('ОШибка')
