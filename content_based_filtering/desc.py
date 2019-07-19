def print_description(index):
    example = df[df.index == index][['description', 'name', 'address']].values[0]
    if len(example) > 0:
        print(example[0])
        print('Nama:', example[1])
        print('Alamat:', example[2])        