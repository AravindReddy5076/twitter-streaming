import re
tempTxt=""
# Open if file exists/Create a file to append data
txt = open('cricket_twitter.txt', 'a+')

with open('cricket_twitter.csv',newline='') as csvfile:
    for line in csvfile:
        cricketdata = ""
        url_hash_datacollected = re.findall(r'[#@][^\s#@]+', line)
        url_hash_datacollected += re.findall("(?P<url>https?://[^\s]+)",line)
        print("url's and hashtags extraction in progress")
        for data in url_hash_datacollected:
            cricketdata += " "+data
            txt.write(cricketdata)

print("Extraction Completed Successfully")
#close file
txt.close()