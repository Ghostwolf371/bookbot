def get_num_words(text):
    return len(text.split())


def get_num_each_char(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def sort_on(dict):
    return dict["count"]


def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
