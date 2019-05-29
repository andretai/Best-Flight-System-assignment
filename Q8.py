import plotly
plotly.tools.set_credentials_file(username='kahseng97',api_key='VKuPm0qbKKoUsRMzdh1c')
import plotly.plotly as py
import plotly.graph_objs as go
news = {}
positivenum = []
negativenum = []
neutralnum = []

def readwords( filename ):
    f = open(filename)
    text = f.read()
    word = text.split()
    return word

pos_word = readwords('pos.txt')
neg_word = readwords('neg.txt')


def pos_neg_num_pct(news):
    pos = 0
    neg = 0
    neu = 0

    for key in news:
        key = key.rstrip('.,?!\n') # removing possible punctuation signs
        if key in pos_word:
            pos += 1
        elif key in neg_word:
            neg += 1
        else:
            neu += 1

    total = pos + neg + neu
    pos_Pct = round((pos / total) * 100, 2)
    neg_Pct = round((neg / total) * 100, 2)
    neu_Pct = round((neu / total) * 100, 2)

    positivenum.append(pos)
    negativenum.append(neg)
    neutralnum.append(neu)



    print ("Positive Number: ", pos)
    print ("Nagative Number: ", neg)
    print ("Neutral Number: ", neu)
    print ("Positive Percentage: ", pos_Pct, "%")
    print ("Negative Percentage: ", neg_Pct, "%")
    print ("Neutral Percentage: ", neu_Pct, "%")



def plotsentiment():
    cityname=["Osaka", "Incheon", "Melbourne", "Moscow", "Beijing", "Jakarta", "Singapore", "NewYork", "Madrid", "Manchester"]
    trace1 = go.Bar(x=cityname,y=positivenum, name='Positive Number')
    trace2 = go.Bar(x=cityname,y=negativenum, name='Negative Number')
    data=[trace1,trace2]
    layout = go.Layout(barmode='group')

    fig=go.Figure(data=data,layout=layout)
    py.plot(fig,filename='grouped-bar')


city = {'Osaka', 'Incheon', 'Melbourne', 'Moscow', 'Beijing', 'Jakarta', 'Singapore', 'NewYork', 'Madrid', 'Manchester'}

for c in city:
    file = c + ".txt"
    f = open(file)
    news = f.read().split()
    print(c)
    pos_neg_num_pct(news)
    print()

print(positivenum)
print(negativenum)
print(neutralnum)

#plotsentiment()