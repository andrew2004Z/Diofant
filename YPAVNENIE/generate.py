f = open('chisla.txt', 'w')
for a in range(1, 100000):
    for b in range(1, 100000):
        for c in range(1, 100000):
            f.write(f'{a} {b} {c}\n')