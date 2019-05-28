


# posNum = [455, 510, 1222, 624, 433, 430, 679, 466, 1225, 728]
# negNum = [70, 74, 157, 80, 77, 35, 121, 135, 235, 142]
# neuNum = [1157, 1347, 2785, 1864, 1331, 995, 1733, 1385, 3742, 2024]

city = ["Osaka", "Incheon", "Melbourne", "Moscow", "Beijing", "Jakarta", "Singapore", "NewYork", "Madrid", "Manchester"]
#list with [{posNum, negNum, neuNum}]
posNegNeu = [[455, 70, 1157], [510, 74, 1347], [1222, 157, 2785],
             [624, 80, 1864], [433, 77, 1331], [430, 35, 995], [679, 121, 1733],
             [466, 135, 1385], [1225, 235, 3742], [728, 142, 2024]]
print("Approach 1: Positive or Negative Sentiment")
print("Positive when Positive words > Negative words and vice versa")
#Sentiment based on positive & negative word Count
for cName in city:
    if posNegNeu[city.index(cName)][0] > posNegNeu[city.index(cName)][1]:
        print(str(cName) + " having Positive Sentiment")
    elif posNegNeu[city.index(cName)][0] < posNegNeu[city.index(cName)][1]:
        print(str(cName) + " having Negative Sentiment")
    else:
        print(str(cName) + " Neither Positive or Negative")

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

#Creating a Bayer List
#format: [[(A and B), (A and B'), (A' and B), (A' and B')], [(A and B), (A and B'), (A' and B), (A' and B')], ...] following country sequence
for cName in city:
    bayerList[city.index(cName)][0] = int(round(posNegNeu[city.index(cName)][0] * 0.8))
    bayerList[city.index(cName)][1] = posNegNeu[city.index(cName)][0] - bayerList[city.index(cName)][0]
    bayerList[city.index(cName)][2] = int(round(posNegNeu[city.index(cName)][1] * 0.8))
    bayerList[city.index(cName)][3] = posNegNeu[city.index(cName)][1] - bayerList[city.index(cName)][2]
#print(bayerList)

#new BayerList = [[+ve words|+ve news, +ve words|-ve news], [+ve words|+ve news, +ve words|-ve news], ......]
newBayList = [[None for _ in range(2)] for _ in range(10)]
for cName in city:
    newBayList[city.index(cName)][0] = bayerList[city.index(cName)][0] + bayerList[city.index(cName)][3]
    newBayList[city.index(cName)][1] = bayerList[city.index(cName)][1] + bayerList[city.index(cName)][2]

#print(newBayList)

#bayTotalRow = [+ve news, +ve news, ....]
bayRowTotal = [[None for _ in range(1)] for _ in range(10)]

for cName in city:
    bayRowTotal[city.index(cName)] = newBayList[city.index(cName)][0] + newBayList[city.index(cName)][1]

#print(bayRowTotal)

print()
print("Approach 2: Positive or Negative Sentiment")
print("Using Bayes' Theorem")
for cName in city:
    if (newBayList[city.index(cName)][0]/bayRowTotal[city.index(cName)]) > (newBayList[city.index(cName)][1]/bayRowTotal[city.index(cName)]):
        print (cName + "->Bayes' Theorem: Positive sentiment")
    elif (newBayList[city.index(cName)][0]/bayRowTotal[city.index(cName)]) < (newBayList[city.index(cName)][1]/bayRowTotal[city.index(cName)]):
        print(cName + "-> Bayes' Theorem: Negative sentiment")
    else:
        print(cName + "-> Bayes' Theorem: Neither Positive or Negative sentiment")

    # print(newBayList[city.index(cName)][0]/bayRowTotal[city.index(cName)])
    # print(newBayList[city.index(cName)][1]/bayRowTotal[city.index(cName)])




#Backup
# for cName in city:
#     for i in range(len(posNegNeu)):
#         if posNegNeu[int(i)][0] > posNegNeu[int(i)][1]:
#             print(str(cName) + "Positive Sentiment")
#         elif posNegNeu[int(i)][0] < posNegNeu[int(i)][1]:
#             print(str(cName) + "Negative Sentiment")
#         else:
#             print(str(cName) + "Neither Positive or Negative")


# bayerList[0].append(city.index(cName))


# for cName in city:
#     bayerList[city.index(cName)][0] = (posNegNeu[city.index(cName)][0] * 0.8)
#     bayerList[city.index(cName)][1] = (posNegNeu[city.index(cName)][0] * 0.2)
#     bayerList[city.index(cName)][2] = (posNegNeu[city.index(cName)][1] * 0.8)
#     bayerList[city.index(cName)][3] = (posNegNeu[city.index(cName)][1] * 0.2)
# print(bayerList)