alphadict_q = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'o', 10: 'p',
               11: 'a', 12: 's', 13: 'd', 14: 'f', 15: 'g', 16: 'h', 17: 'j', 18: 'k', 19: 'l', 20: 'z',
               21: 'x', 22: 'c', 23: 'v', 24: 'b', 25: 'n', 26: 'm', 27: '1', 28: '2', 29: '3', 30: '4',
               31: '5', 32: '6', 33: '7', 34: '8', 35: '9', 36: '0', 37: 'Q', 38: 'W', 39: 'E', 40: 'R',
               41: 'T', 42: 'Y', 43: 'U', 44: 'I', 45: 'O', 46: 'P', 47: 'A', 48: 'S', 49: 'D', 50: 'F',
               51: 'G', 52: 'H', 53: 'J', 54: 'K', 55: 'L', 56: 'Z', 57: 'X', 58: 'C', 59: 'V', 60: 'B',
               61: 'N', 62: 'M', 63: '!', 64: '@', 65: '#', 66: '$', 67: '%', 68: '^', 69: '&', 70: '*',
               71: '(', 72: ')', 73: '`', 74: '~', 75: '-', 76: '_', 77: '=', 78: '+', 79: ',', 80: '<',
               81: '.', 82: '>', 83: '/', 84: '?', 85: ';', 86: "'", 87: '"', 88: '[', 89: '{', 90: ']',
               91: '}', 92: ' ', 93: '|', 94: ':'}
numadict_q = {v: k for k, v in alphadict_q.items()}

alphadict_a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
               11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
               21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: '+', 28: "'", 29: '"', 30: '`',
               31: '~', 32: '[', 33: ']', 34: '{', 35: '}', 36: ';', 37: '|', 38: 'B', 39: 'C', 40: 'D',
               41: 'E', 42: 'F', 43: 'G', 44: 'H', 45: 'I', 46: 'J', 47: 'K', 48: 'L', 49: 'M', 50: 'N',
               51: 'O', 52: 'P', 53: 'Q', 54: 'R', 55: 'S', 56: 'T', 57: 'U', 58: 'V', 59: 'W', 60: 'X',
               61: 'Y', 62: 'Z', 63: '!', 64: '@', 65: '#', 66: '$', 67: '%', 68: '^', 69: '&', 70: '*',
               71: '(', 72: ')', 73: ' ', 74: ',', 75: '<', 76: '.', 77: '>', 78: '/', 79: '?', 80: '-',
               81: '_', 82: '=', 83: '1', 84: '2', 85: '3', 86: '4', 87: '5', 88: '6', 89: '7', 90: '8',
               91: '9', 92: '0', 93: ':', 94: 'A'}
numadict_a = {v: k for k, v in alphadict_a.items()}

alphadict_z = {1: 'Z', 2: 'z', 3: 'Y', 4: 'y', 5: 'X', 6: 'x', 7: 'W', 8: 'w', 9: 'V', 10: 'v',
              11: 'U', 12: 'u', 13: 'T', 14: 't', 15: 'S', 16: 's', 17: 'R', 18: 'r', 19: 'Q', 20: 'q',
              21: 'P', 22: 'p', 23: 'O', 24: 'o', 25: 'N', 26: 'n', 27: 'M', 28: 'm', 29: 'L', 30: 'l',
              31: 'K', 32: 'k', 33: 'J', 34: 'j', 35: 'I', 36: 'i', 37: 'H', 38: 'h', 39: 'G', 40: 'g',
              41: 'F', 42: 'f', 43: 'E', 44: 'e', 45: 'D', 46: 'd', 47: 'C', 48: 'c', 49: 'B', 50: 'b',
              51: 'A', 52: 'a', 53: '0', 54: '9', 55: '8', 56: '7', 57: '6', 58: '5', 59: '4', 60: '3',
              61: '2', 62: '1', 63: ')', 64: '(', 65: '*', 66: '&', 67: '^', 68: '%', 69: '$', 70: '#',
              71: '@', 72: '!', 73: '~', 74: '`', 75: '+', 76: '=', 77: '_', 78: '-', 79: ':', 80: ';',
              81: '"', 82: "'", 83: '<', 84: ',', 85: '>', 86: '.', 87: '?', 88: '/', 89: ' ', 90: '{',
              91: '}', 92: '[', 93: ']', 94: '|'}
numadict_z = {v: k for k, v in alphadict_z.items()}


dictdict = {"a":  (alphadict_a, numadict_a), "q":  (alphadict_q, numadict_q), "z":  (alphadict_z, numadict_z)}



def new_autodict(name):
    i = 1
    alphadict_name = {}
    while i <= 94:
        alphadict_name.update({i: input(i)})
        i += 1
    numadict_name = {v: k for k, v in alphadict_name.items()}
    print(alphadict_name)
    print(numadict_name)
    x = ""
    while x != "y" and x != "n":
        x = input("add to dictdict?(y/n)")
    if x == "y":
        dictdict.update({name: (alphadict_name, numadict_name)})
        print("added")
        with open('EFdictdict.txt', 'a') as textionaries:
            textionaries.write(", \n\"" + str(name) + "\":  " + str((alphadict_name, numadict_name)))
    elif x == "n":
        print("not added")

def encrypt(input, cypher, key):
    coded_list = []
    encrypted_list = []
    i = 1

    for character in input:
        if character in cypher:
            coded_list.append(cypher[character])

    for number in coded_list:
        number += int(key) + i*i
        number = number % len(cypher)
        if number == 0:
            number = len(cypher)
        encrypted_list.append(number)
        i += 1
    return encrypted_list


def active(en_dict, de_dict):
    option = ""


    while option != "encode" and option != "decode" and option != "autodict" \
            and option != "dictionaries" and option != "quit":

        option = str.lower(input("\n \n \nWhat Would you like to do?\n(Commands: encode, decode, autodict, dictionaries, quit):"))


    if option =="encode":

        d = input('Dictionary:')
        k = input("Key:")
        y = encrypt(input("Message:\n\n"), dictdict.get(d)[1], k)
        new_letters = []
        new_string = ""
        for number in y:
            if number in alphadict_a:
                new_letters.append(alphadict_a[number])
        for letter in new_letters:
            new_string += letter

        print("\nEncoded Message:\n")
        print(new_string)
        option = ""
        active(en_dict, de_dict)


    elif option == "decode":

        num_list = []
        new_num_list = []
        char_list = []
        new_string = ""
        i = 1
        d = input("Dictionary:")
        k = input("Key:")
        m = input("Encoded Message:\n\n")

        for character in m:
            if character in numadict_a:
                num_list.append(numadict_a[character])

        for number in num_list:
            number -= (int(k) + i * i)
            number = number % len(numadict_a)
            if number == 0:
                number = len(numadict_a)
            new_num_list.append(number)
            i += 1

        for number in new_num_list:
            if number in dictdict.get(d)[0]:
                char_list.append(dictdict.get(d)[0][number])

        for letter in char_list:
            new_string += letter

        print("\nDecoded Message:\n")
        print(new_string)
        option = ""
        active(en_dict, de_dict)

        return new_string

    elif option == "autodict":
        new_autodict(input("Dictionary Name:"))

        option = ""
        active(en_dict, de_dict)

    elif option == "dictionaries":
        x = str(dictdict.keys())
        x = x.split("[")[1]
        x = x.split("]")[0]
        x = x.replace("'", "")
        x = x.replace('"', "")
        print(x)

        option = ""
        active(en_dict, de_dict)

    elif option == "quit":
        print("\n \nGoodbye!")
        quit()

        option = ""
        active(en_dict, de_dict)

print("Welcome to EncoFun!")
active(numadict_q, alphadict_q)