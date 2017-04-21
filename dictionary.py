import csv
from collections import OrderedDict     # for sorting of dictionary keys

while True:

    my_dict = {}
    with open('data.csv', 'r') as f:
        my_dict = dict(csv.reader(f))
    print(my_dict)

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
                print("Sadly there is no such definition :( But you can add that to dictioary! ( ͡° ͜ʖ ͡°)")

        elif menu == 2:
            new_element = {}
            new_definition = input("Enter name of definition(key): ")
            new_explanation = input("Enter explanation: ")
            new_source = input("Enter source: ")
            new_element[new_definition] = (new_explanation, new_source)
            print(new_element)
            with open('data.csv', 'w') as f:
                csv.writer(f).writerows(new_element.items())
"''ZAPISUJE Z CUDZYSLOWAMI NAOKOLO TUPLA i nadpisuje ciagle te same dane zamiast przejsc do kolejnej linii"''

        elif menu == 3:
            my_dict = OrderedDict(sorted(my_dict.items()))  # sorting of elements in dictionary
            for key in my_dict:     # printing only the keys
                print(key)

        elif menu == 4:
            my_dict = OrderedDict(sorted(my_dict.items()))
            for key in my_dict:
                print(key[0])   # printing only first letter of the keys

        elif menu == 0:
            break
        else:   # dupa test
            print('Choose proper menu number!')

    except ValueError:  # if you put non-int
        print('Is that a number?')

print("See you next time! ( ͡° ͜ʖ ͡°)")
