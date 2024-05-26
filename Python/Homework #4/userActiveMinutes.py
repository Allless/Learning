def getUserActiveMinutes(logs, k):
    userDict = {}
    for log in set([tuple(i) for i in logs]):
        if(log[0] in userDict):
            userDict[log[0]] += 1
        else:
            userDict[log[0]] = 1
    return [list(userDict.values()).count(t) for t in range(1,k+1)]
