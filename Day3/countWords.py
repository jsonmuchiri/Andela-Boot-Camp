def words(A):
    word_split = A.split()
    word_list = []
    for word in word_split:
        word_list.append(word)

    is_list = {i: word_list.count(i) for i in word_list if not i.isdigit()}
    count_words = {int(k): word_list.count(k) for k in word_list if k.isdigit()}
    count_words.update(is_list)
    print(count_words)
    

words("test print")
