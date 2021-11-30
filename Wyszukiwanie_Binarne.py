from random import randint

range_of_list = int(input("Input a range of list"))

randomint = randint(0, range_of_list)
print(randomint)

list_of_numbers = [x for x in range(301)]

print(list_of_numbers)


while True:
    userinput = int(input("Guess the number: "))

    if userinput < randomint:
        print(f"Your number {userinput} is less than Random Int")
        del list_of_numbers[0: userinput + 1]

    if userinput > randomint:
        print(f"Your number {userinput} is greater than Random Int")
        del list_of_numbers[userinput: len(list_of_numbers) + 1]

    if userinput == randomint:
        print("YOU WON")
        break

    print(list_of_numbers)