import os
import platform
import snscrape.modules.twitter
import requests
import random
from getch import getch

# determining to use cls or clear depending on os
sys = platform.system()
if sys == 'Windows':
    clear = 'cls'
elif sys == 'Linux' or 'Darwin':
    clear = 'clear'

def tweet_scraper():
    os.system(clear)
    user = input("Enter the users tweets you want to scrape:\nChoice: ")

    os.system(clear)
    jsonchoice=int(input("Do you want the program to output the tweets in json form?\n(1) Yes\n(2) No\nChoice: "))
    if jsonchoice==1:
        json1='--jsonl '
        json2='-tweets.json'
    elif jsonchoice==2:
        json1=''
        json2='-tweets.txt'

    os.system(clear)
    replychoice=int(input("Do you want to include replies?\n(1) Yes\n(2) No\nChoice: "))
    if replychoice==1:
        reply1=''
    elif replychoice==2:
        reply1=' exclude:replies '
    
    os.system(clear)
    retweetschoice=int(input("Do you want to include retweets?\n(1) Yes\n(2) No\nChoice: "))
    if retweetschoice == 1:
        retweets1 = ''
    elif retweetschoice == 2:
        retweets1 = 'exclude:retweets'
    
    os.system(clear)
    limitchoice1=int(input("Do you want a limit on the amount of tweets to scrape?\n(1) Yes\n(2) No\nChoice: "))
    if limitchoice1 == 1:
        os.system(clear)
        limitchoice2 = str(input("What is the limit you wish to have?\nChoice: "))
        limit1 = '--max-results ' + limitchoice2 + ' '
    elif limitchoice1 == 2:
        print("")
        limit1 = ''
    
    os.system(clear)
    progresschoice=int(input("Do you want the program to output progress?\n(1) Yes\n(2) No\nChoice: "))
    if progresschoice == 1:
        progress1 = '--progress '
    elif replychoice == 2:
        progress1 = ''

    # checks if directory exists, if not then it makes it
    if os.path.isdir('tweets') == True:
        print("")
    elif os.path.isdir('tweets') == False:
        os.system('mkdir tweets')
    
    os.system(clear)
    # command for scraping the tweets, utilizes the inputs from above
    os.system('''snscrape ''' + limit1 + progress1 + json1 + '''twitter-search "from:''' + user + reply1 + retweets1 + '''" > tweets/''' + user + json2)
    os.system(clear)

    # printing the amount of tweets scraped & what user it was from
    num_lines = sum(1 for _ in open('tweets/' + user + json2))
    print("Scraped " + str(num_lines) + " tweets from @" + user + '.\n')
    print("Press any key to continue.")
    getch()

def image_downloader():
    while True:
        os.system(clear)
        user = input("Enter the user you wish to download media from:\nChoice: ")

        if os.path.isdir('images/' + user) == True:
            os.system(clear)
            print("You seem to have already scraped images from this user.\nDelete the directory and try again.\n\nPress any key to continue.")
            getch()
            break
        elif os.path.isdir('images/' + user) == False:
            os.system('mkdir -p images/' + user)
        
        os.system(clear)
        print("Scraping images, this may take a while.")

        for tweet in snscrape.modules.twitter.TwitterUserScraper(user, False).get_items():
            if not tweet.media:
                continue
            for medium in tweet.media:
                if isinstance(medium, snscrape.modules.twitter.Photo):
                    r = requests.get(medium.fullUrl)
                    with open('images/' + user + '/' + str(random.randint(0000000000, 9999999999)) + '.jpg', 'wb') as fp:
                        fp.write(r.content)
        print("Finished scraping images from " + user + '.\nPress any key to continue')
        getch()
        break


def main():
    while True:
        os.system(clear)
        try:
            choice=int(input("Choose an option:\n(1) Tweet Scraper\n(2) Image Downloader\n(3) Quit\nChoice: "))
            if choice==1:
                tweet_scraper()
            elif choice==2:
                image_downloader()
            elif choice==3:
                break
            else:
                print("That was an incorrect answer. Press any key to continue")
                getch()
                continue
        except:
            print("That was an incorrect answer. Press any key to continue")
            getch()
            continue

if __name__ == '__main__':
    main()