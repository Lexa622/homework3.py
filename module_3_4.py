def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        for j in range(len(i) - len(root_word)):
            if root_word.lower() == i[j: len(root_word) + j].lower():
                same_words.append(i)
        for j in range(len(root_word) - len(i)):
            if i.lower() == root_word[j: len(i) + j].lower():
                same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
