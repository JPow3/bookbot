def get_num_words(input):
    word_count = input.split()
    return len(word_count)

def get_num_letters(input):
    final_dict = {}
    for i in input:
        letter = i.lower()
        if letter in final_dict:
            final_dict[letter] += 1
        else:
            final_dict[letter] = 1
    return final_dict

