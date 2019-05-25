import urllib.request
import plotly.plotly as py
import plotly.graph_objs as go
import string

class News:
    def __init__(self, file):

        self.file = file
        self.list = getPureAlphabet(file)
        self.word = {}
        self.stopword = {}
    
    def getWord(self):
        for w in self.list:
            if not rabin_karp(w, "stop_word.txt"):
                if w in self.word:
                    self.word[w] += 1
                else:
                    self.word[w] = 1

        return self.word

    def getStopword(self):
        for w in self.list:
            if rabin_karp(w, "stop_word.txt") and len(w) > 1:
                if w in self.stopword:
                    self.stopword[w] += 1
                else:
                    self.stopword[w] = 1
        return self.stopword

def rabin_karp(pattern, file_name):
    pureAlphabet = str.maketrans(string.punctuation + string.ascii_uppercase,
                                " " * len(string.punctuation) + string.ascii_lowercase)
    words = open(file_name).read().translate(pureAlphabet)
    length = len(pattern)
    hpattern = hash(pattern)

    is_matched = False
    for i in range(0, len(words) - length):
        hword = hash(words[i:length + i])
        if hword == hpattern:
            if pattern == words[i:length + i]:
                is_matched = True
                break

    return is_matched

def getPureAlphabet(text):
    pureAlphabet = str.maketrans(string.punctuation + string.ascii_uppercase,
                                " " * len(string.punctuation) + string.ascii_lowercase)
    text = text.translate(pureAlphabet)
    return text.split()


def plotStopword(word, stop):
    cityName=[]
    wordCount=[]
    stopwordCount=[]

    
    for w in word:
        cityName.append(w)

    for w in word.values():
        wordCount.append(w)

    for w in stop.values():
        stopwordCount.append(w)


    trace1 = go.Bar(
     x=cityName,
     y=wordCount,
     name='Word Count'
     )
     
    trace2 = go.Bar(
    x=cityName,
    y=stopwordCount,
    name='Stop Word Count'
    )

    data=[trace1,trace2]
    layout=go.Layout(barmode='group')

    fig=go.Figure(data=data,layout=layout)
    py.plot(fig,filename='grouped-bar')


def countWord(word):
    return sum(word.values())
    

wordCount={}
stopCount={}
city = {'Osaka', 'Incheon', 'Melbourne', 'Moscow', 'Beijing', 'Jakarta', 'Singapore', 'NewYork', 'Madrid', 'Manchester'}
for c in city:
    file = c + ".txt"
    f = open(file)
    newClass = News(f.read())
    wordCount[c] = countWord(newClass.getWord())
    stopCount[c] = countWord(newClass.getStopword())

print(wordCount)
print(stopCount)

plotStopword(wordCount,stopCount)