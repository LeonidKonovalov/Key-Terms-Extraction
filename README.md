# Key-Terms-Extraction
Project from https://hyperskill.org/projects/134?track=2

Program that can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model. Used natural language processing and preprocessing with the NLTK library, string operations, and the application of statistics in your code.

There was 6 stages:

-First we open the given text corpus, break the text into separate words, and obtain some properties of the corpus.
-Then we use bigrams, sequences of two consecutive words from the dataset. Transform the preprocessed corpus into a list of bigrams. 
-Create a Markov chain model that shows the probability of certain words appearing after a given chain of words. 
-Use the Markov model to generate a text starting with a user-specified word and handle exceptions. 
-Modify the algorithm so that sentences always start with capital letters and end with punctuation marks. 
-Extend the program to create a Markov model based on trigrams in order to generate more sensible sentences. 
