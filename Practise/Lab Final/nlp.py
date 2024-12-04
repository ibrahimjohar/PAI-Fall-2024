from nltk.tokenize import word_tokenize, sent_tokenize

paragraph = """hello man whats up, Ibrahim has opened up his new digital store. head onto wix's website. to see more."""
            
print(paragraph)

##tokenization
# paragraph --> sentences
# sentence --> words
sentences = sent_tokenize(paragraph) #converts to sentences
print(sentences)

words = word_tokenize(paragraph) #converts to words
print(words)


#stemming --> converts a word to its root/base word
## Comments of product is a positive review or negative review
## Reviews ----> eating, eat, eaten or going, go, gone

words = ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]

##PorterStemmer

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

for word in words:
    print(word+"---->"+stemmer.stem(word))

## Major disadvantage of stemming is that stemmed words don't always give a proper meaning
## eaten --> eaten, history --> histori (sometimes they are either unchanged or don't produce valid words)

print(stemmer.stem("congratulations")) #invalid case
print(stemmer.stem("sitting")) #valid case

##lemmatization
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("going", pos='n')) #pos = 'a' (adjective), 'v' (verb), 'n' (noun)

for word in words:
    print(word+"---->"+lemmatizer.lemmatize(word, pos = 'v'))
    
print(lemmatizer.lemmatize("beautiful", pos = 'a'))


#stopwords
from nltk.corpus import stopwords
import nltk

#nltk.download('stopwords')
#stopwords.words('english')

paragraph = """The lion is a wild terrestrial animal called the king of the forest. The lion is a strong animal with a strong body, a big head, 
a majestic mane, and two fierce eyes. Lions are predatory animals and eat only after hunting. 
They have strong claws and sharp teeth, which help them hunt their prey and eat the flesh. 
Lions have yellowish-grey skin colour with smooth hair and an imperious roar which makes a lion unique. 
The footprints of lions are called pug marks. Lions are found chiefly in grasslands, open woodlands, or enclosed in zoos. 
Since they kill their own prey and hunt for food, they have the capacity to run fast."""

words = word_tokenize(paragraph)
#make list that has all stemmed words that are not present in the stopwords set
words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]

print(words)

stemmed_paragraph = ' '.join(words) #same sentence w/o the stopwords
print("stemmed paragraph:\n",stemmed_paragraph)

#now with lemmatization
words = word_tokenize(paragraph)
words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
lemmatized_paragraph = ' '.join(words)
print("lemmatized paragraph:\n",lemmatized_paragraph)
