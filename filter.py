file = open('spanish_len_5.txt', 'r')
abc = 'abcdefghijklmnñopqrstuvwxyz'
tilde = 'áéíóúü'

def write_list_to_file(txt, py_file):
    with open(py_file, 'w') as f:
        f.write(f"WORDS = [\n")
        for line in txt:
            if all(x in abc for x in line.strip()):
                f.write(f"  '{line.strip()}', \n")

        f.write(f"]\n")

write_list_to_file(file, 'word_list.py')
            