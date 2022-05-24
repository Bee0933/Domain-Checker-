import os
import pickle
import config
import warnings
import pandas as pd
import joblib as jl
import tldextract as xt  
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

warnings.filterwarnings(action='ignore')

# helper function
def join_char(s):
    str1 = ''
    return(str1.join(s))

# function to perform n_grams on input string 
def n_gram_extraction(n, token):
    lst = []
    n_grams = ngrams(list(str(token)), n)
    for items in n_grams:
        res = join_char(list(items))
        
        lst.append(res)
    return lst

# function to tokenize input url and extract values to form unigrams, bigrams & trigrams 
def tokenizer(url):
    # break url to domain, subdomain & suffix 

    # full url token - domain + subdomain + suffix
    url_token = f'{url}-{xt.extract(url).subdomain}-{xt.extract(url).domain}-{xt.extract(url).suffix}'
    
    # url to unigram level
    domain_unigram = n_gram_extraction(1,xt.extract(url).domain)
    subdomain_unigram = n_gram_extraction(1,xt.extract(url).subdomain)

    # url to bigram level
    domain_bigram = n_gram_extraction(2,xt.extract(url).domain)
    subdomain_bigram = n_gram_extraction(2,xt.extract(url).subdomain)

    # url to trigram level
    domain_trigram = n_gram_extraction(3,xt.extract(url).domain)
    subdomain_trigram = n_gram_extraction(3,xt.extract(url).subdomain)
    token = url_token.split('-')
    if '' in token:
        token.remove('') # remove empty element in list
    
    # append final exteacted tokens to list to form extracted features
    for item in domain_unigram:
        token.append(item)
    for item in subdomain_unigram:
        token.append(item)

    for item in domain_bigram:
        token.append(item)
    for item in domain_trigram:
        token.append(item)

    for item in subdomain_bigram:
        token.append(item)
    for item in subdomain_trigram:
        token.append(item)

    # print(token)

    return token

# predict model function
def predict(url):
    url = str(url).lower()

    # load train data to fit vectorizer
    with open(config.X_TRAIN_SAVED, 'rb') as f:
            Xtrain = pickle.load(f)

            # preprocess & vectorize train set 
            tVec = TfidfVectorizer(tokenizer=tokenizer)
            tf = tVec.fit_transform(Xtrain)

            # preprocess and vectorize input url
            input = [url]
            tf = tVec.transform(input)

            # load trained model 
            model = jl.load(config.TRAINED_MODEL, 'r')

            # prediction
            result = model.predict(tf)
            res = {'0': 'maleware domain', '1': 'legit'}
            # print(res[str(result[0])])

            return res[str(result[0])]


if __name__ == '__main__':
    # print(predict('GorddsogjowdhvoudhsidhsklE.Com'))
    pass

