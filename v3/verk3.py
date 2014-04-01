
def test(filename):
    dict = {}
    file = open(filename).readlines()
    for line in file:
        split = line.split(" ")
        if len(split) > 1:
            if not split[0] in dict:
                 dict[split[0]] = [(split[1],split[2][:-1])]
            else:
                dict[split[0]].append((split[1],split[2][:-1]))
    return dict

