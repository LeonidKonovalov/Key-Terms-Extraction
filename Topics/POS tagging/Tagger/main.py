import nltk


# the line below reads a sentence from the input and converts it into a list
sent = input().split()

# your code here

n = nltk.pos_tag(sent)
print(n)
# for i in n:
#         print(i)
        # if i[1] == 'NN':
        #         print(i[0])
# nltk.help.upenn_tagset('WRB')