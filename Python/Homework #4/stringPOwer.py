def getStringPower(str, pow):
    if(pow >= 0):
        return str * pow
    pow *= -1
    subStrLen = int(len(str)/pow)
    if(subStrLen == len(str)/pow and str.count(str[:subStrLen]) == pow):
        return str[:subStrLen]
    return 'undefinded'

