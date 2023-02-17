##Python file: semantic.py

# Import Spacy module.
import spacy
# load two different language models, en_core_web_md and en_core_web_sm for later comparison
nlp = spacy.load('en_core_web_md')
nlp_sm = spacy.load('en_core_web_sm')

#### First Example ####
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
# Using the advanced language model en_core_web_md, the similarity() method is used to compare the similarity between
# the pairs of words, and the results are printed.
print("─" * 77)
print(f"│ {'First Example : Usage of advanced language model en_core_web_md:':^{74}}│")
print("─" * 77)
print(f"│ {'Similarity Between:':^{43}}│ {'Rate:':^{29}}│")
print("─" * 77)
print(f"│ \t\t\t\t{word1} & {word2}\t\t\t\t │\t\t\t {word1.similarity(word2):.5f} \t\t\t│")
print(f"│ \t\t\t\t{word3} & {word2}\t\t\t\t │\t\t\t {word3.similarity(word2):.5f} \t\t\t│")
print(f"│ \t\t\t\t{word2} & {word1}\t\t\t\t │\t\t\t {word3.similarity(word1):.5f} \t\t\t│")
print("─" * 77)
print(f'''
The advanced language model 'en_core_web_md' can identify similarities between different types of entities, such as 
"monkey" and "banana," despite their dissimilarity in meaning or usage (animal/ fruit). This indicates the model's 
ability to recognize underlying patterns in language.. For loops can calculate similarity but may not align with 
human intuition due to basic word embeddings.
''')
print(f"\n")

#### Second Example ####
# Similar to the above module, but this time the nlp() method is run on the same three words using the single
# language model en_core_web_sm.
word1_sm = nlp_sm("cat")
word2_sm = nlp_sm("monkey")
word3_sm = nlp_sm("banana")
print("─" * 77)
print(f"│ {'Second Example : Usage of single language model en_core_web_sd:':^{74}}│")
print("─" * 77)
print(f"│ {'Similarity Between:':^{43}}│ {'Rate:':^{29}}│")
print("─" * 77)
print(f"│ \t\t\t\t{word1_sm} & {word2_sm}\t\t\t\t │\t\t\t {word1_sm.similarity(word2_sm):.5f} \t\t\t│")
print(f"│ \t\t\t\t{word3_sm} & {word2_sm}\t\t\t\t │\t\t\t {word3_sm.similarity(word2_sm):.5f} \t\t\t│")
print(f"│ \t\t\t\t{word2_sm} & {word1_sm}\t\t\t\t │\t\t\t {word3_sm.similarity(word1_sm):.5f} \t\t\t│")
print("─" * 77)
print(f'''
'En_core_web_md' is larger and more advanced than 'en_core_web_sm', with more features such as pre-trained word vectors 
for computing word similarity. 'En_core_web_sm' lacks these word vectors, so similarity judgments based only on the 
tagger, parser, and NER may not be useful.
''')
print(f"\n")

#### Third Example ####
tokens = nlp('cat apple monkey banana ')
print("─" * 77)
print(f"│ {'Third Example : Usage of for loops to undertake comparison of the words:':^{74}}│")
print("─" * 77)
print(f"│ {'Similarity Between:':^{43}}│ {'Rate:':^{29}}│")
print("─" * 77)
# for loop to iterate through all possible pairs of words in the sentence "cat apple monkey banana" and calculate the
# similarity between them using the similarity() method.
for token1 in tokens:
  for token2 in tokens:
    print(f"│ \t\t\t\t{token1.text:^{6}} & {token2.text:^{6}}\t\t\t\t │\t\t\t {token1.similarity(token2):.5f} \t\t\t│")
print("─" * 77)
print(f'''
'For loops to compare words' lack the granularity and context of spaCy models, as it only provides a matrix of 
similarity scores between individual words, without considering their relationships within the sentence or broader 
context.

The trend of higher similarity scores between related words is similar between 'en_core_web_md' and 'for loops'. 
However, spaCy provides more contextual information, accounting for meanings and sentence relationships, which 
'for loops' do not.

Comparing "happy," "joyful," and "ecstatic" using the 'en_core_web_md' and 'for loops' NLP models could demonstrate the 
potential for nuanced similarity scores with the larger model, which may not be captured by the 'for loops' model.
''')
print(f"\n")


#### Fourth Example ####
# Using similarity scores between "car", "bike", "book" and "bike"
word1 = nlp("car")
word2 = nlp("bike")
word3 = nlp("book")
word4 = nlp("chair")
# Using the advanced language model en_core_web_md, the similarity() method is used to compare the similarity between
# the pairs of words, and the results are printed.
print("─" * 77)
print(f"│ {'Fourth Example : advanced language model en_core_web_md vs for loops:':^{74}}│")
print(f"│ {'(Between Own words: car, bike, book and chair)':^{74}}│")
print("─" * 77)
print(f"│ {'Similarity Between:':^{43}}│ {'Rate:':^{29}}│")
print("─" * 77)
print(f"│ {'Example : advanced language model en_core_web_md:':^{74}}│")
print("─" * 77)
print(f"│  \t\t\t\t{word1} & {word2}\t\t\t\t\t │\t\t\t {word1.similarity(word2):.5f} \t\t\t│")
print(f"│  \t\t\t\t{word3} & {word2}\t\t\t\t\t │\t\t\t {word3.similarity(word2):.5f} \t\t\t│")
print(f"│  \t\t\t\t{word3} & {word1}\t\t\t\t\t │\t\t\t {word3.similarity(word1):.5f} \t\t\t│")
print(f"│  \t\t\t\t{word4} & {word1}\t\t\t\t\t │\t\t\t {word4.similarity(word1):.5f} \t\t\t│")
print("─" * 77)
print(f"│ {'Example : for loops to undertake a comparison of the words:':^{74}}│")
print("─" * 77)

# for loop to iterate through all possible pairs of words and calculate the similarity between them using the similarity() method.
tokens = nlp('car bike book chair')
for token1 in tokens:
  for token2 in tokens:
    print(f"│ \t\t\t\t{token1.text:^{6}} & {token2.text:^{6}}\t\t\t\t │\t\t\t {token1.similarity(token2):.5f} \t\t\t│")
print("─" * 77)
print(f'''
"Car" and "bike" have higher similarity scores than "car" and "book" or "chair" and "car" due to shared semantic 
similarities. However, the score between "book" and "bike" may not be intuitive to humans. Human evaluation and 
validation are essential for NLP results.
''')
print(f"\n\n")

#### Fifth Example ####
# Compare a single sentence, with a list of other sentences using the similarity() method
print("─" * 77)
print(f"│ {'Fifth Example : Working with sentences:':^{74}}│")
print("─" * 77)
print(f"│ {'Sentence:':^{43}}│ {'Rate:':^{29}}│")
print("─" * 77)
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
  similarity = nlp(sentence).similarity(model_sentence)
  print(f"│ {sentence:^{42}} │ {similarity:^{28},.5f} │")
print("─" * 77)
print(f"\n\n")
