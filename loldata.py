import json , requests, time ,datetime
key = "RGAPI-3ebe2d5e-360c-4ad5-beaa-6642af128ec2"
summonerName = "대운사"  #후에 input 으로 바꿔서 입력받자.
url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName+"?api_key="+key
res = requests.get(url)
dataJson = res.text
dataDic = json.loads(dataJson)
enAccID= dataDic['accountId']

urlMats = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/'+enAccID+'?api_key='+key

r = requests.get(urlMats)
dataMatsJ = r.text
dataMatsD = json.loads(dataMatsJ)
n = 0
a = 0
timeFirst = 0
timeEnd = 0
for h in dataMatsD['matches'] :
    im = str(h['gameId'])
    urlim = 'https://kr.api.riotgames.com/lol/match/v4/matches/'+im+'?api_key='+key
    res = requests.get(urlim)
    dataJson = res.text
    dataDic = json.loads(dataJson)
    times = dataDic['gameDuration']
    a = a + times
    realmin = times//60 
    realsec = times%60
    print(str(realmin)+'분',str(realsec)+'초')
    n = n + 1
    print(n)

    if(n==98):
        timeEnd = h['timestamp']
        break
    if(n==1):
        timeFirst = h['timestamp']

datetimeFir = datetime.datetime.fromtimestamp(timeFirst/1000)
print(datetimeFir)
datetimeEnd = datetime.datetime.fromtimestamp(timeEnd/1000)
print(datetimeEnd)
print((datetimeFir-datetimeEnd).days, '일')


print(n)
print(a)
amin = a//60 
asec = a%60
print(str(amin)+'분',str(asec)+'초')