def reversed_words():
    sentence='Python is exciting!'
    words=sentence.split(' ');

    reverse_sentence=' '.join(reversed(words))
    print(reverse_sentence)

reversed_words()