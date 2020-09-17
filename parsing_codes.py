
import requests

r = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

with open('jsr.log','w') as ru:
    ru.write(r.text)

dictionary = {}

with open("jsr.log", "r") as logFile:

    for line in logFile:

        statusCode = line.split(" ")[8]

        if statusCode in dictionary:
            dictionary[statusCode] = dictionary[statusCode] + 1
        else:
            dictionary[statusCode] = 1
    for item in sorted((key,value) for (key,value) in dictionary.items()):
            print(item)
