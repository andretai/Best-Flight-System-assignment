#city = ["ITM", "ICN", "MEL", "SVO", "PEK", "CGK", "SIN", "JFK", "MAD", "MAN"]
city = ["Osaka", "Incheon", "Melbourne", "Moscow", "Beijing", "Jakarta", "Singapore", "NewYork", "Madrid", "Manchester"]
bestRouteDist = [4965, 4103, 6329, 8200, 3200, 1125, 297, 16161, 11098, 10785]
newBayList: [[378, 147], [423, 161], [1009, 370], [515, 189], [361, 149], [351, 114], [567, 233], [400, 201], [1027, 433], [610, 260]]
pnNewsProb = [[0.720, 0.280], [0.724, 0.276], [0.732, 0.268], [0.732, 0.268], [0.708, 0.292], [0.755, 0.245], [0.709, 0.291], [0.666, 0.334], [0.703, 0.297], [0.701, 0.299]]
totalPosProb = 0
totalNegProb = 0
totalRouteDist = 0
invTotalDist = 0
invSumPosBay = 0

#Create a list to store the probability of using a route
routeProb = [[None for _ in range(1)] for _ in range(10)]
#Create a list to store the probability of going that country based on positive news (Bayes' Theorem)
bayProb = [[None for _ in range(1)] for _ in range(10)]
#Create a list to store prob distribution
proDistList = [[None for _ in range(1)] for _ in range(10)]

#Probability take 0.5 from the Bayes Theorem, 0.5 from the route distance probability
for cName in city:
    totalPosProb += pnNewsProb[city.index(cName)][0]
    totalNegProb += pnNewsProb[city.index(cName)][1]
    totalRouteDist += bestRouteDist[city.index(cName)]

    #Total distance of all route (1/A + 1/B + ....)
    invTotalDist += 1/bestRouteDist[city.index(cName)]

    # Total positive probability choosing a route (inverse)
    invSumPosBay += 1/pnNewsProb[city.index(cName)][0]


for cName in city:
    routeProb[city.index(cName)] = (1 / bestRouteDist[city.index(cName)]) / (invTotalDist)

for cName in city:
    bayProb[city.index(cName)] = (1 / pnNewsProb[city.index(cName)][0]) / invSumPosBay


# print(totalPosProb)
# print(totalNegProb)
# print(totalRouteDist)
# print(invTotalDist)
# print(invSumPosBay)


#Printing route prob list
print(routeProb)

#Printing country selection list
print(bayProb)



#Probability of a user using a particular route
#Based on 0.50 routeProb and bayProb
#People normally prefer short distance country with positive politics sentiment

for cName in city:
    print(cName)
    proDis = (0.5 * routeProb[city.index(cName)]) + (0.5 * bayProb[city.index(cName)])
    proDistList[city.index(cName)] = proDis
    print("Probability Distribution: " + "{0:.3f}".format(proDis))
    print()

cityIndex =proDistList.index(max(proDistList))
#print(cityIndex)
print("Highest possible that end user will visit to " + city[cityIndex])
print("Probability Distribution: ")
print(round(max(proDistList),3))









#Backup
# bestRouteDist(from KL to) = ["ICN", "ITM", "MEL", "SVO", "PEK", "CGK", "SIN", "JFK", "MAN", "MAD"]