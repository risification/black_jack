from random import randint

players = 10
names = ['urmatik', 'beksich', 'aziretich', 'businesswman', 'erjanchik', 'ataichik', 'rasulchik',
         'rusik', 'sanjarchik', 'saidchik']
w_names = []
dict1 = {}
list1 = []
i = 0


def twenty_one(names, players: int):
    i = 0
    while i < players:
        print(f'Играет {names[i]}')
        two_cards = randint(2, 11) + randint(2, 11)
        print(two_cards)
        check = input('One more? да/нет: ')
        while check == 'да':
            two_cards = two_cards + randint(2, 11)
            print(two_cards)
            if two_cards > 21:
                break
            check = input('One more? да/нет: ')
        if two_cards > 21:
            two_cards = 0

        if two_cards > 0:
            w_names.append(names[i])
            list1.append(two_cards)

        # Придумать алгоритм на удаление из names

        dict1[names[i]] = two_cards
        print(f'У игрока {names[i]} {two_cards} очков!')
        i += 1


twenty_one(names, 10)
print(w_names, list1)
w_names2 = []
w_list = []
list1_max = max(list1)

for i in range(len(list1)):
    if list1_max == list1[i]:
        w_names2.append(w_names[i])
        w_list.append(list1[i])
twenty_one(w_names2, len(w_names2))
