def count_character_frequencies(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

string= "data structures and algorithms"
print(count_character_frequencies(string))