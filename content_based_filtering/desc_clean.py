# Deskripsi kedua (Setelah preprocessing)
def print_description_clean(index):
    example = df[df.index == index][['desc_clean', 'name', 'address']].values[0]
    if len(example) > 0:
        print(example[0])
        print('Nama:', example[1])
        print('Alamat:', example[2])