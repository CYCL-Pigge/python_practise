i = 1
while i <= 9:
    q = 1
    while q <= i:
        print(f'{q} * {i} = {q * i}', end='\t')
        q = q +1
    print()
    i = i + 1