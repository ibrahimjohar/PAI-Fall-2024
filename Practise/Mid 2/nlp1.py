import nltk
#nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

text = "this is a sample sentence. tokenize me, please."

#tokenize the text into words
words = word_tokenize(text)
print("word tokenization:")
print(words)

#tokenize the text into sentences
sentences = sent_tokenize(text)
print("sentence tokenization:")
print(sentences)

# stemming
# -> a process that stems(removes) last few characters from a word, often leading to incorrect meanings and spellings
# -> 'caring' to 'car'
# used in case of large dataset, where performance is an issue

# lemmatization
# -> considers context & converts the word to its meaningful base form (called Lemma)
# -> 'caring' to 'care'
# computationally expensive since it involves look up tables

from nltk.stem import PorterStemmer

#initialize the Porter Stemmer
stemmer = PorterStemmer()

#sample words for stemming
words = ["jumping", "jumps", "jumped", "running", "runner", "easily"]

#stem the words
stemmed_words = [stemmer.stem(word) for word in words]
print("\n")
print("original words: ", words)
print("stemmed words: ", stemmed_words)


from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

#list of words to lemmatize
words = ["jumping", "jumps", "jumped", "running", "runner", "easily"]

#apply lemmatization specifying the part of speech as verb (POS = 'v')
lemmatized_words_n = [lemmatizer.lemmatize(word) for word in words]

lemmatized_words_v = [lemmatizer.lemmatize(word, pos='v') for word in words]


print("\noriginal words: ", words)
print("lemmatized words as noun: ", lemmatized_words_n)
print("lemmatized words as verb: ", lemmatized_words_v)


print("\n")


# stop words
# "a", "the", "is", "are"
# commonly used in text mining and NLP to eliminate words that are so widely used that they
# carry very little useful information

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "this is a sample sentence with some stopwords that we want to remove."

#tokenize the text
words = word_tokenize(text)

#get a list of english stopwords
stop_words = set(stopwords.words('english'))

#remove stopwords from the list of words
filtered_words = [word for word in words if word.lower() not in stop_words]

print("original words: ", words)
print("words after removing stopwords: ", filtered_words)

print("\n")

#stemming a paragraph
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """
            Pakistan is the site of several ancient cultures, including the 8,500-year-old Neolithic site of 
            Mehrgarh in Balochistan, the Indus Valley civilisation of the Bronze Age, and the ancient Gandhara civilisation. 
            The regions that comprise the modern state of Pakistan were the realm of multiple empires and dynasties, 
            including the Achaemenid, the Maurya, the Kushan, the Gupta; the Umayyad Caliphate in its southern regions, 
            the Samma, the Hindu Shahis, the Shah Miris, the Ghaznavids, the Delhi Sultanate, the Mughals, and most recently, the British Raj from 1858 to 1947."
            """
            
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

#stemming 
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print("sentences after stemming: ", sentences)

#Produce intermediate representation of the word that may not have any meaning

print("\n")

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

paragraph = """
            Pakistan is the site of several ancient cultures, including the 8,500-year-old Neolithic site of 
            Mehrgarh in Balochistan, the Indus Valley civilisation of the Bronze Age, and the ancient Gandhara civilisation. 
            The regions that comprise the modern state of Pakistan were the realm of multiple empires and dynasties, 
            including the Achaemenid, the Maurya, the Kushan, the Gupta; the Umayyad Caliphate in its southern regions, 
            the Samma, the Hindu Shahis, the Shah Miris, the Ghaznavids, the Delhi Sultanate, the Mughals, and most recently, the British Raj from 1858 to 1947."
            """
            
sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

#lemmitization

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print("sentences after lemmatizing: ", sentences)



