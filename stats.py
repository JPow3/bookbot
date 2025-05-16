def get_num_words(input):
    word_count = input.split()
    return len(word_count)

def get_num_letters(input):
    final_dict = {}
    word_count = input.split()
    for word in word_count:
        word.lower()
        final_dict[word] += 1
    return final_dict

