##Python file: watch_next.py

# Import Spacy module.
import spacy

# Load the language model
nlp = spacy.load("en_core_web_md")

# Read in the movie descriptions from the movies.txt file
with open("movies.txt", "r", encoding='utf-8-sig') as f:
    movies = f.readlines()


# Define a function to find the most similar movie and recommend the next movie based on the description of the already
# watched movie
def most_similar_movie(description):
    # Parse the description using the language model
    query = nlp(description)

    # Calculate the similarity of the query to each movie; the word vectors for each movie
    similarities = [query.similarity(nlp(movie)) for movie in movies]

    # Find the index of the most similar movie
    most_similar_index = similarities.index(max(similarities))
    similarity_max = max(similarities)
    print(f"\nRating of similarity: {100 * similarity_max:.2f}%\n")

    # Return the title of the most similar movie correspondent to the above index
    return movies[most_similar_index]


# Test the function with the given description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the " \
              "Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in " \
              "peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a " \
              "gladiator."

# call the most_similar_movie function with the description of as a parameter
similar_movie = most_similar_movie(description)
print("You should watch next: \n", similar_movie)
