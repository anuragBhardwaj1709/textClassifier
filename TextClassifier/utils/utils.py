import pickle
import re
import string


def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.strip()
    text = ' '.join([i for i in text.split() if len(i) > 2])
    return text


def classifier():
    clf = pickle.load(open('TextClassifier/utils/classifier_V4.pkl', 'rb'))
    return clf


def vector():
    vec = pickle.load(open('TextClassifier/utils/vector_V4.pkl', 'rb'))
    return vec


def binarizer():
    multilabel = pickle.load(open('TextClassifier/utils/binarizer_V4.pkl', 'rb'))
    return multilabel
