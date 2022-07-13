fileNum=""
hashtagList=[]
hashtagCounter=[]
try:
    
    while(1):
        f = open('messages'+str(fileNum)+".html", 'r', encoding='utf-8')
        for line in f:
            for i in range(line.count("ShowHashtag")):
                line=line[line.find("ShowHashtag")+len("ShowHashtag(&quot;"):]
                a = line[:line.find("&")]
                j=0
                while j<len(hashtagList) and a!=hashtagList[j]:
                    j += 1
                if(j==len(hashtagList)):
                    hashtagList.append(a)
                    hashtagCounter.append(1)
                else:
                    hashtagCounter[j] += 1
        f.close()
        if(fileNum):
            fileNum+=1;
        else:
            fileNum=2;
except FileNotFoundError:
    if(fileNum):
        print("Scanning done. Scanned files: "+str(fileNum-1));
    else:
        print("Files not found1")
            
f = open('hashtags.txt', 'w', encoding='utf-8')

if(fileNum):
    # Output for list
    f.write("Powered by TelegramHashtagFinder 0.1. Helps find hashtags in exported Telegram history.\nCredit: Konstantin Mazein (@stels_rus)")
    f.write("\n\nFiles scanned: "+str(fileNum-1))
    f.write("\nDifferent hashtags detected: "+str(len(hashtagList)))
    hashtagNumber=0
    for i in hashtagCounter:
        hashtagNumber += i
    f.write("\nNumber of detected hashtags: "+str(hashtagNumber))    
    f.write("\n\nList of different hashtags:\n")
    for i in hashtagList:
        f.write("#"+i+"\n")
    
    # Sorting for making Top-list
    for i in range(len(hashtagCounter)):
        max = i
        for j in range(i+1, len(hashtagCounter)):
            if(hashtagCounter[j]>hashtagCounter[max]):
                max=j
        hashtagList[i], hashtagList[max] = hashtagList[max], hashtagList[i]
        hashtagCounter[i], hashtagCounter[max] = hashtagCounter[max], hashtagCounter[i]
        
    # Output for Top-list
    f.write("\n\nTop hashtags:\n")

    for i in range(len(hashtagList)):
        f.write("#"+str(hashtagList[i])+" "+str(hashtagCounter[i])+"\n")

f.close()
