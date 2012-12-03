import cPickle as pickle

def initialize():
    fhandle = open('classificador.pkl', 'rb')
    classifier = pickle.load(fhandle)
    return classifier

clf = initialize()
