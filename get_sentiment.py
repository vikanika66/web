from sklearn.externals import joblib
PATH_TO_MODEL = "models/clf.pkl"


def load_model():
    return joblib.load(PATH_TO_MODEL)

def get_sentiment(data):
    clf = load_model()
    if clf.predict([data]) == 1:
        return 'positive'
    else:
        return 'negative'
