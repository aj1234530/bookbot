def get_book_text(filepath):
    with open(filepath) as f:
        return len(f.read().split())
    
def freq_char(filepath):
    with open(filepath) as f:
        file_c = f.read()
    char_dict = {}
    for char in file_c:
        char = char.lower()
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char] = 1
    return char_dict

    # split the each chars here and count the no of chars
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
