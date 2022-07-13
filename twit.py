import os
import platform


while True:
    sys = platform.system()
    if sys == 'Linux' or 'Darwin':
        clear = 'clear'
    elif sys == 'Windows':
        clear = 'cls'
    
    os.system(clear)
    user = input("Enter the users tweets you want to scrape:\n")

    os.system(clear)
    print("Do you want the program to output the tweets in json form?\n(1) Yes\n(2) No")
    jsonchoice=int(input("Choice: "))
    if jsonchoice==1:
        json1='--jsonl'
        json2='-tweets.json'
    elif jsonchoice==2:
        json1=''
        json2='-tweets.txt'

    os.system(clear)
    print("Do you want to include replies?\n(1) Yes\n(2) No")
    replychoice=int(input("Choice: "))
    if replychoice==1:
        reply1=''
    elif replychoice==2:
        reply1=' exclude:replies '
    
    os.system(clear)
    print("Do you want to include retweets?\n(1) Yes\n(2) No")
    retweetschoice=int(input("Choice: "))
    if retweetschoice == 1:
        retweets1 = ''
    elif retweetschoice == 2:
        retweets1 = 'exclude:retweets'
    
    os.system(clear)
    print("Do you want the program to output progress?\n(1) Yes\n(2) No")
    progresschoice=int(input("Choice: "))
    if progresschoice == 1:
        progress1 = '--progress '
    elif replychoice == 2:
        progress1 = ''

    if os.path.isdir('tweets') == True:
        print("")
    elif os.path.isdir('tweets') == False:
        os.system('mkdir tweets')
    
    os.system(clear)
    print("Do you want a limit on the amount of tweets to scrape?\n(1) Yes\n(2) No")
    limitchoice1=int(input("Choice: "))
    if limitchoice1 == 1:
        os.system(clear)
        print("What is the limit you wish to have?")
        limitchoice2 = str(input("Choice: "))
        limit1 = '--max-results ' + limitchoice2 + ' '
    elif limitchoice1 == 2:
        print("")
        limit1 = ''

    os.system(clear)
    os.system('''snscrape ''' + limit1 + progress1 + json1 + '''twitter-search "from:''' + user + reply1 + retweets1 + '''" > tweets/''' + user + json2)
    break