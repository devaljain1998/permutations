import sys

def remove_redundant_strings(strings: list):
    """Generating a list from keys (values of list)
    If any redudant value (key) is found then it will not be 
    inserted in the dict, and then recreating the list from the 
    dictionary
    """
    return list(dict.fromkeys(strings))

def generate_permutations(index: int, matrix_of_characters: list):
    
    #Setting up breakpoint of recursion:
    if (index == len(matrix_of_characters) - 1):
        return matrix_of_characters[index]
    
    list_from_prev_func = generate_permutations(index + 1, matrix_of_characters)
    characters = matrix_of_characters[index]
    bare_list = []
    for character in characters:
        for c in list_from_prev_func:
            bare_list.append(character + c)
            
    #removing redundant strings (if any)
    bare_list = remove_redundant_strings(bare_list)
    return bare_list

def get_permutations(matrix_of_characters):
    return generate_permutations(0, matrix_of_characters)


def read_input_csv_file(filename):
    matrix = []
    with open(filename) as file:
        #Reading file line by line
        while True:
            line = file.readline()
            if not line:
                break
            array = line.strip().split(',')
            matrix.append(array)
    return matrix

def main(*args):
    #Reading the csv file to get the 2D Array
    #of characters (characters with line):
    filename = args[0][0]
    matrix_of_characters = read_input_csv_file(filename)
    
    #Generating the permutations
    permutations = get_permutations(matrix_of_characters)
    permutations_space_seperated = ' '.join(permutations)
    print(permutations_space_seperated)

if __name__ == "__main__":
    main(sys.argv[1:])