city = ["Osaka", "Incheon", "Melbourne", "Moscow", "Beijing", "Jakarta", "Singapore", "NewYork", "Madrid", "Manchester"]

#list with [{posNum, negNum, neuNum}]
posNegNeu = [[455, 70, 1157], [510, 74, 1347], [1222, 157, 2785],
             [624, 80, 1864], [433, 77, 1331], [430, 35, 995], [679, 121, 1733],
             [466, 135, 1385], [1225, 235, 3742], [728, 142, 2024]]

#***************************Approach 1****************************************
#Keep result from approach 1
app1List = [[None for _ in range(1)] for _ in range(10)]
print("Approach 1: Positive or Negative Sentiment")
print("Positive when Positive words > Negative words and vice versa")

#Sentiment based on positive & negative word Count
for cName in city:
    print(cName)
    posWordCount = posNegNeu[city.index(cName)][0]
    negWordCount = posNegNeu[city.index(cName)][1]
    if posWordCount > negWordCount:
        print("Number of Positive Number: %d" % posWordCount)
        print("Number of Negative Number: %d" % negWordCount)
        print("Word Count: Positive Sentiment")
        app1List[city.index(cName)] = 1
    elif posWordCount < negWordCount:
        print("Number of Positive Number: %d" % posWordCount)
        print("Number of Negative Number: %d" % negWordCount)
        print("Word Count: Negative Sentiment")
        app1List[city.index(cName)] = -1
    else:
        print("Number of Positive Number: %d" % posWordCount)
        print("Number of Negative Number: %d" % negWordCount)
        print("Word Count: Neither Positive or Negative")
        app1List[city.index(cName)] = 0



#*******************************Approach 2************************************
#Alternative way of calculating Sentiment
#Using Bayers Theorem
"""
Sometime Positive word can be a negative news for certain country
Give an example here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
Let A = Positive Word
Let B = Positive News
Assuming that P(A and B) = 0.8 and P(A' and B') = 0.8
"""
#bayerList = [[]*(n-1)]*n -> n*n list
bayerList = [[None for _ in range(4)] for _ in range(10)]

#Keep result from approach 2
app2List = [[None for _ in range(1)] for _ in range(10)]

#Creating a Bayer List
#bayerList = [[(A and B), (A and B'), (A' and B), (A' and B')], [(A and B), (A and B'), (A' and B), (A' and B')], ...] following country sequence
for cName in city:
    bayerList[city.index(cName)][0] = int(round(posNegNeu[city.index(cName)][0] * 0.8))
    bayerList[city.index(cName)][1] = posNegNeu[city.index(cName)][0] - bayerList[city.index(cName)][0]
    bayerList[city.index(cName)][2] = int(round(posNegNeu[city.index(cName)][1] * 0.8))
    bayerList[city.index(cName)][3] = posNegNeu[city.index(cName)][1] - bayerList[city.index(cName)][2]
#print(bayerList)

#new BayerList = [[+ve news, -ve news], [+ve news, -ve news], ......]
newBayList = [[None for _ in range(2)] for _ in range(10)]
for cName in city:
    newBayList[city.index(cName)][0] = bayerList[city.index(cName)][0] + bayerList[city.index(cName)][3]
    newBayList[city.index(cName)][1] = bayerList[city.index(cName)][1] + bayerList[city.index(cName)][2]

#print(newBayList)

#bayTotalRow = [total[0], total[1], ....]
bayRowTotal = [[None for _ in range(1)] for _ in range(10)]

for cName in city:
    bayRowTotal[city.index(cName)] = newBayList[city.index(cName)][0] + newBayList[city.index(cName)][1]

#print(bayRowTotal)

print()
print("Approach 2: Positive or Negative Sentiment")
print("Using Bayes' Theorem")
for cName in city:
    print(cName)
    posSen = (newBayList[city.index(cName)][0]/bayRowTotal[city.index(cName)])
    negSen = (newBayList[city.index(cName)][1]/bayRowTotal[city.index(cName)])
    if  posSen > negSen:
        print("Probability of positive sentiment: %.3f" % posSen)
        print("Probability of negative sentiment: %.3f" % negSen)
        print ("Bayes' Theorem: Positive sentiment")
        app2List[city.index(cName)] = 1
    elif posSen < negSen:
        print("Probability of positive sentiment: %.3f" % posSen)
        print("Probability of negative sentiment: %.3f" % negSen)
        print("Bayes' Theorem: Negative sentiment")
        app2List[city.index(cName)] = -1
    else:
        print("Probability of positive sentiment: %.3f" % posSen)
        print("Probability of negative sentiment: %.3f" % negSen)
        print("Bayes' Theorem: Neither Positive or Negative sentiment")
        app2List[city.index(cName)] = 0

    # print(newBayList[city.index(cName)][0]/bayRowTotal[city.index(cName)])
    # print(newBayList[city.index(cName)][1]/bayRowTotal[city.index(cName)])

#Conclusion
print()
for cName in city:
    if app1List[city.index(cName)] == 1 and app2List[city.index(cName)] == 1:
        print("Conclusion: Positive Sentiment in " + str(cName))
    elif app1List[city.index(cName)] == -1 and app2List[city.index(cName)] == -1:
        print("Conclusion: Negative Sentiment in " + str(cName))
    else:
        print("Conclusion: No Result in " + str(cName))
