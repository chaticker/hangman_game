from random import *
lists = ["apple", "banana", "orange"]
c_list = choice(lists)  #랜덤으로 넣기
print(c_list)

letters = ""  #사용자로부터 지금까지 입력받음 모든 알파벳 보관

while True:
    succeed = True
    print()
    for w in c_list:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success")

    letter = input("input letter > ")  #사용자 입력 받기
    if letter not in letters:
        letters += letter

    if letter in c_list:
        print("Correct")
    else:
        print("wrong")
