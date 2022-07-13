import os

while True:
    try:
        user = input("\nEnter the users tweets you want to scrape:\n")
        print("\nDo you want the program to output the tweets in json form?\n(1) Yes\n(2) No")
        jsonchoice=int(input("Choice:\n> "))
        if jsonchoice==1:
            print("")
            os.system('''snscrape --progress --jsonl twitter-search "from:''' + user + ''' exclude:replies exclude:retweets" > ''' + user + '''-tweets.json''')
        elif jsonchoice==2:
            print("")
            os.system('''snscrape --progress twitter-search "from:''' + user + ''' exclude:replies exclude:retweets" > ''' + user + '''-tweets.txt''')
        else:
            print("\nThat was an incorrect answer. Press any key to continue")
    except:
        print("\nThat was an incorrect answer. Press any key to continue")
        continue
    