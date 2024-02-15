import re

with open("sampletcpdump.txt", 'r') as f:
    data = f.read()

packetLog = ".+ IP .+\n    .+ ecr .+"
icmpPattern = ".+ICMP.+\n.+ICMP.+\n.+\n.+"
messageList = list(re.findall(packetLog, data))
icmpList = list(re.findall(icmpPattern, data))

idPattern = 'id [0-9]+'
routerIp = '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
ttlPattern = 'ttl [0-9]+'
ipPatternCalc = '[0-9]+\.[0-9]+'

beforeTTL = ""
beforeRouter = ""

for m in messageList:
    resultTTL = re.findall(ttlPattern, m)
    resultID = re.findall(idPattern, m)
    lessCalcIP = re.findall(ipPatternCalc,m)

    if (beforeTTL != resultTTL[0]):      
        print(resultTTL[0].upper())
        beforeTTL = resultTTL[0]

    for icmp in icmpList:
       resultFindID = re.findall(idPattern, icmp)
       if (resultFindID[1] == resultID[0]) :
            resultRouter = re.findall(routerIp, icmp)
            if (beforeRouter != resultRouter[0]):
                print(resultRouter[0])
                beforeRouter = resultRouter[0]

            moreCalcIP = re.findall(ipPatternCalc, icmp)
            seconds = (float(moreCalcIP[0])-float(lessCalcIP[0]))*1000
            print("%.2f ms" % seconds)



