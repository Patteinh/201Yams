from src.utils import help

def check_args(ac, av):
    valid_dice = "123456"
    valid_cmb = ["pair", "three", "four", "full", "straight", "yams"]
    error = 0
    error_c = 0

    if ac == 2 and av[1] == "-h":
        help()
        exit(0)
    if ac != 7:
        raise Exception("ERROR: The number of arguments must be 7.")
    combination = av[6]
    for i in range(1, 6):
        if len(av[i]) != 1 or not av[i].isdigit() or int(av[i]) not in range(7):
            raise Exception("ERROR: The numbers passed are not correct.")
    for s in valid_cmb:
        if s in combination:
            break
        else:
            error_c += 1
    if (error_c == len(valid_cmb)):
            raise Exception("ERROR: Invalid combination")
    for i, c in enumerate(valid_cmb):
        if (error == 6):
            raise Exception("ERROR: Invalid combination")
        if not av[6].startswith(c):
            error += 1
            continue
        if i == 3:
            if combination[combination.find('_') + 1] in valid_dice and combination[combination.rfind('_') + 1] in valid_dice and combination[combination.rfind('_') + 1] != combination[combination.find('_') + 1]:
                continue
            else:
                raise Exception("ERROR: Invalid full combination")
        if i == 4:
            if int(combination[combination.find('_') + 1]) < 5:
                raise Exception("ERROR: Invalid straight combination")
        if combination[-1] == '_':
            raise Exception("ERROR: Invalid combination")
        if combination[combination.find('_') + 1] in valid_dice:
            continue
        raise Exception("ERROR: Invalid combination")
