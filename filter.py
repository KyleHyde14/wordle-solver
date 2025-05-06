file = open('spanish_len_5.txt', 'r')
abc = 'abcdefghijklmnñopqrstuvwxyz'
tilde = 'áéíóúü'
substitution = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ü': 'u'
}

def write_list_to_file(txt, py_file):
    with open(py_file, 'w') as f:
        f.write(f"WORDS = [\n")
        for line in txt:
            line = line.strip()
            if all(x in abc for x in line):
                f.write(f"  '{line}', \n")
            elif any(x in tilde for x in line):
                for i in line.strip():
                    if i in substitution:
                        line = line.replace(i, substitution[i])
                f.write(f"  '{line}', \n")

        f.write(f"]\n")

write_list_to_file(file, 'word_list.py')
            