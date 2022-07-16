import os
import platform
import pandas as pd
from getch import getch

sys = platform.system()
if sys == 'Windows':
    clear = 'cls'
elif sys == 'Linux' or 'Darwin':
    clear = 'clear'

def tweet_scraper():
    os.system(clear)
    user = input("Enter the users tweets you want to scrape:\n")

    os.system(clear)
    print("Do you want the program to output the tweets in json form?\n(1) Yes\n(2) No")
    jsonchoice=int(input("Choice: "))
    if jsonchoice==1:
        json1='--jsonl '
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
    os.system('''snscrape ''' + limit1 + progress1 + json1 + '''twitter-search "from:''' + user + reply1 + retweets1 + '''" > tweets/''' + user + json2)
    os.system(clear)
    num_lines = sum(1 for _ in open('tweets/' + user + json2))
    print("Scraped " + str(num_lines) + " tweets from @" + user + '.\n')
    print("Press any key to continue.")
    getch()

def media_downloader():
    print()

def main():
    while True:
        os.system(clear)
        print("Choose an option:\n(1) Tweet Scraper\n(2) Media Downloader\n(3) Quit")
        try:
            choice=int(input("Choice: "))
            if choice==1:
                tweet_scraper()
            elif choice==2:
                media_downloader()
            elif choice==3:
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                os.system(clear)
                continue
            os.system(clear)
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            os.system(clear)
            continue


if __name__ == '__main__':
    main()