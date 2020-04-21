
import spacy

nlp = spacy.load('fr_core_news_sm')
doc = nlp("Le pastis et l'eau vont très bien ensemble, n'est-ce pas ?")

""" Tokenization """
for token in doc:
    print(token)

""" Text Preprocessing | Lemmatization """
print("\n" + f"Token \t\tLemma \t\tStopword".format('Token', 'Lemma', 'Stopword'))
print("-"*40)
for token in doc:
    print(f"{str(token)}\t\t{token.lemma_}\t\t{token.is_stop}")

