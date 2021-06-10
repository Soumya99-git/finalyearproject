import pickle

def emotion_from_text(s):
    file = "model.sav"
    model = pickle.load(open(file,"rb"))

    return model.predict([s])[0]


