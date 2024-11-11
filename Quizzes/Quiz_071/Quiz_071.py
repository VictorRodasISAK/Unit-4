import random


def macGenerator(N: int):
    output = []
    letter_dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    for i in range(N):
        mac = ""
        for j in range(6):
            mac += random.choice([str(random.randint(0, 9)), letter_dict[random.randint(10, 15)]])
            if j % 2 == 1 and j != 5:
                mac += ":"
        output.append(mac)
    return output





