import csv
from collections import OrderedDict     # for sorting of dictionary
'''
dict = {'definition':'name of def','expl_source':('expl','source')}

with open('dictionary.csv', newline='') as csvfile:
    for row in range(sum(1 for line in open('dictionary.csv'))):
        dict_tuples.append(readline())
print(dict_tuples)
'''


my_dict = {'definition': ('eplx', 'source'),
           'adefinition': ('eplxA', 'sourceA'),
           'cdefinition': ('eplxC', 'sourceC')
           }

while True:
            # wczytanie pliku od nowa
    try:
        print('/----------------------------------------------------------------------\ ')
        print(' Dictionary for a little programmer:\n\
        1) search explanation by appellation\n\
        2) add new definition\n\
        3) show all appellations alphabetically\n\
        4) ***show available definitions by first letter of appellation\n\
        0) exit')
        print('\----------------------------------------------------------------------/ ')
        menu = int(input("Choose option from menu: "))

        if menu == 1:
            search = input("What definition are you looking for? ")
            if search in my_dict:   # dictionary membership test
                print("Explanation:", my_dict.get(search)[0])
                print("Source:", my_dict.get(search)[1])
            else:
                print("There is no such definition :( You can add that to dictioary! ;)")

        elif menu == 2:
            my_dict['definition'] = input("Enter name of definition(key): ")
            my_dict['expl_n_source'] = input("Enter explanation")
            print(my_dict)

        elif menu == 3:
            my_dict = OrderedDict(sorted(my_dict.items()))
            print(my_dict)
            for key in my_dict:
                print(key)

        elif menu == 4:
            my_dict = OrderedDict(sorted(my_dict.items()))
            print(my_dict)
            for key in my_dict:
                print(key[0])

        elif menu == 0:
            break
        else:
            print('Choose proper menu number!')

    except ValueError:
        print('Is that a number?')

print("See you next time! ( ͡° ͜ʖ ͡°)")
