
def parser_yams(av):
    data = {'d':[int(arg) for arg in av[1:6]],'combination':None,'nbr':[0, 0], 'v':None, 's':None}
    cmp = ["pair", "three", "four", "full", "straight", "yams"]
    for c in cmp:
        if av[6].startswith(c):
            data['combination'] = c
            if c == "pair":
                data['v'] = 2
                data['s'] = "pair"
            if c == "three":
                data['v'] = 3
                data['s'] = "three-of-a-kind"
            if c == "four":
                data['v'] = 4
                data['s'] = "four-of-a-kind"
            if c == "yams":
                data['v'] = 5
                data['s'] = "yams"
            if c == "straight":
                data['s'] = "straight"
            data['nbr'][0] = int(av[6][-1])
            if c == "full":
                data['nbr'][1] = int(av[6][-1])
                data['nbr'][0] = int(av[6][5])
                data['s'] = "full_of"
            return (data)
    return (data)
