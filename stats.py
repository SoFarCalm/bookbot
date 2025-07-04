def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def get_num_words(string):

    list_of_words = string.split()
    number_of_words = len(list_of_words)
    
    return number_of_words

def get_num_chars(string):

    num_chars_dict = {}

    for letter in string:
        lowercase_letter = letter.lower()

        if lowercase_letter not in num_chars_dict:
            num_chars_dict[lowercase_letter] = 1
        
        elif lowercase_letter in num_chars_dict:
            num_chars_dict[lowercase_letter] += 1
    
    return num_chars_dict

def sort_dictionary(dictionary):

    list_of_dictionaries = []

    for k, v in dictionary.items():
        
        if k.isalpha():

            temp_dict = {}
            key_1 = 'char'
            key_2 = 'num'

            temp_dict[key_1] = k
            temp_dict[key_2] = v

            list_of_dictionaries.append(temp_dict)
    
    sorted_list = sorted(list_of_dictionaries, key=lambda d: d['num'], reverse = True)

    for d in sorted_list:
        print(f"{d[key_1]}: {d[key_2]}")
