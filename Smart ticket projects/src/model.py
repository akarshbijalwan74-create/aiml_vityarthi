from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd

# Dummy dataset to 'train' our AI instantly
data = {
    'text': [
        'my internet is down', 'wifi not working', 'connection lost',
        'billing error', 'wrong charge', 'invoice incorrect',
        'password reset', 'cannot login', 'account locked'
    ],
    'category': [
        'Technical', 'Technical', 'Technical',
        'Billing', 'Billing', 'Billing',
        'Account', 'Account', 'Account'
    ]
}

def get_trained_model():
    df = pd.DataFrame(data)
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(df['text'], df['category'])
    return model

def predict_category(model, text):
    return model.predict([text])[0]
