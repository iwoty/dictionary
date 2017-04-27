import csv
from collections import OrderedDict     # for sorting of dictionary keys

while True:
    try:
        my_dict = {}
        with open('data.csv', mode='r') as open_data:  # Opening a file in read mode
            reader = csv.reader(open_data, delimiter=',')   # delimiter tells us about separator
            for row in reader:
                my_dict[row[0]] = (row[1], row[2])
    except FileNotFoundError:
        print("Data.csv file not found :(")
        exit()
    try:
        print('/----------------------------------------------------------------------\ ')
        print(' Dictionary for a little programmer:\n\
        1) search explanation by appellation\n\
        2) add new definition\n\
        3) show all appellations alphabetically\n\
        4) show available definitions by first letter of appellation\n\
        0) exit')
        print('\----------------------------------------------------------------------/ ')
        menu = int(input("Choose option from menu: "))

        if menu == 1:
            search = input("What definition are you looking for? ")
            if search in my_dict:   # dictionary membership test
                print("Explanation:", my_dict.get(search)[0])   # we are taking  first element
                print("Source:", my_dict.get(search)[1])
            else:
                print("Sadly there is no such definition :( But you can add one to dictionary! ( ͡° ͜ʖ ͡°)")

        elif menu == 2:
            new_definition = input("Enter name of definition(key): ")
            new_explanation = input("Enter explanation: ")
            new_source = input("Enter source: ")

            with open('data.csv', mode='a') as add_data:  # Opening a file in append mode
                append_csv = csv.writer(add_data, delimiter=',')
                append_csv.writerow([new_definition, new_explanation, new_source])

        elif menu == 3:
            my_dict = OrderedDict(sorted(my_dict.items()))  # sorting of elements in dictionary
            for key in my_dict:     # printing only the keys
                print(key)

        elif menu == 4:
            my_dict = OrderedDict(sorted(my_dict.items()))
            letter_choice = input("Enter first letter of definition: ")
            for key in my_dict:
                if key[0].upper() == letter_choice.upper():
                    print(key)

        elif menu == 0:
            break
        else:   # dupa test
            print('Choose proper menu number!')

    except ValueError:  # if you put non-int
        print('Is that a number?')

print("See you next time! ( ͡° ͜ʖ ͡°)")
