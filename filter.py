file = open('spanish_len_5.txt', 'r')

def write_list_to_file(txt, py_file):
    with open(py_file, 'w') as f:
        f.write(f"words = [\n")
        for line in txt:
            f.write(f"  '{line.strip()}', \n")

        f.write(f"]\n")

write_list_to_file(file, 'words.py')
            