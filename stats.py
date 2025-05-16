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

def final_sort(input):
    def sort_on(dict):
        return dict["num"]
    list = []
    for char in input:
        count = input[char]
        char_dict = {
            "char" : char,
            "num" : count
        }
        list.append(char_dict)
    list.sort(reverse=True, key=sort_on)
    return list