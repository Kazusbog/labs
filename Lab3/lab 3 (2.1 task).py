with open('user_input.txt','w') as file:
    file.write('hello world')
f=open('user_input.txt','r')
print(f.readline())

