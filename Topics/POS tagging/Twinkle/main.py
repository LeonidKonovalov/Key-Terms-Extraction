import nltk


poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']


n = nltk.pos_tag(poem)
for i in n:
        # print(i)
        if i[1] == 'NN':
                print(i[0])