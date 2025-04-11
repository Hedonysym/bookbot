def count_words(text):
    # counts the words in a string

    words = text.split()
    return len(words)

def count_char(text):
    counts = {}
    for c in text.lower():
        counts[c] = counts.get(c, 0) + 1
    return counts

def sort_dict(dict):
    list = []
    for k in dict:
        new_dict = {}
        new_dict["char"] = k
        new_dict["num"] = dict[k]
        list.append(new_dict)
    # makes a list of dictionaries with number and character values for each entry

    def sort_on(d):
        return d["num"]
    # a function to sort the number values with

    list.sort(reverse=True, key=sort_on)
    return list