#  write your code here 
from sklearn.feature_extraction.text import TfidfVectorizer
f = '''
Old MacDonald Had A Farm
E-I-E-I-O
And on his farm he had a cow
E-I-E-I-O
With a moo moo here
And a moo moo there
Here a moo, there a moo
Everywhere a moo moo
Old MacDonald had a farm
E-I-E-I-O

Old MacDonald had a farm
E-I-E-I-O
And on his farm he had a pig
E-I-E-I-O
With a oink oink here
And a oink oink there
Here a oink, there a oink
Everywhere a oink oink
Old MacDonald had a farm
E-I-E-I-O

Old MacDonald had a farm
E-I-E-I-O
And on his farm he had a duck
E-I-E-I-O
With a quack quack here
And a quack quack there
Here a quack, there a quack
Everywhere a quack quack
Old MacDonald had a farm
E-I-E-I-O

Old MacDonald had a farm
E-I-E-I-O
And on his farm he had a horse
E-I-E-I-O
With a neigh neigh here
And a neigh neigh there
Here a neigh, there a neigh
Everywhere a neigh neigh
Old MacDonald had a farm
E-I-E-I-O

Old MacDonald had a farm
E-I-E-I-O
And on his farm he had a lamb
E-I-E-I-O
With a baa baa here
And a baa baa there
Here a baa, there a baa
Everywhere a baa baa
Old MacDonald had a farm
E-I-E-I-O

Old MacDonald had a farm
E-I-E-I-O
And on his farm he had some chickens
E-I-E-I-O
With a cluck cluck here
And a cluck cluck there
Here a cluck, there a cluck
Everywhere a cluck cluck
With a baa baa here
And a baa baa there
Here a baa, there a baa
Everywhere a baa baa
With a neigh neigh here
And a neigh neigh there
Here a neigh, there a neigh
Everywhere a neigh neigh
With a quack quack here
And a quack quack there
Here a quack, there a quack
Everywhere a quack quack
With a oink oink here
And a oink oink there
Here a oink, there a oink
Everywhere a oink oink
With a moo moo here
And a moo moo there
Here a moo, there a moo
Everywhere a moo moo

Old MacDonald had a farm
E-I-E-I-OOOOOOO...
'''


# with open('hyperskill-dataset-62183909.txt', 'r') as file:
#     vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True,
#                                  analyzer='word', ngram_range=(1, 1),
#                                  stop_words=None)
#     tfidf_matrix = vectorizer.fit_transform([file])
# print(tfidf_matrix[(0, 10)])

dataset = ["Yesterday",
           "All my troubles seemed so far away",
           "Now it looks as though they're here to stay",
           "Oh, I believe in yesterday"]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names_out()
print(terms)