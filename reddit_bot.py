import praw
import config
import time
import os
import random
import datetime
def randomLink():
     textlink = random.choice(list(open('yorumlar.txt', encoding='utf-8')))
     return textlink

def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Reddit new bot b0lshweit")


    return r


def run_bot(r, comments_replied_to):
    print ("Searching last 1,000 comments")
    x = datetime.datetime.now()
    x = int(x.strftime("%H"))
    for submission in subreddit1.new(limit=1):
        if submission.id not in comments_replied_to :
            print(randomLink())
            Yorum=randomLink()
            print(submission.permalink+"\n")
            try:
                submission.reply(body=Yorum)
                time.sleep(5)
            except:
                time.sleep(25)
                pass
            print ("Replied to comment " + submission.id)

            comments_replied_to.append(submission.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(submission.id + "\n")

    print ("Search Completed.")


    print ("Sleeping for 10 seconds...")
    #Sleep for 10 seconds...		
    time.sleep(150)

def get_saved_comments():

	if not os.path.isfile("comments_replied_to.txt"):
		GonderilenPostIdleri = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			GonderilenPostIdleri = f.read()
			GonderilenPostIdleri = GonderilenPostIdleri.split("\n")
			GonderilenPostIdleri = list(filter(None, GonderilenPostIdleri))

	return GonderilenPostIdleri
Satirsublar=""
with open("subs.txt") as file1:
    for line in file1:        
        Satirsublar = Satirsublar+line.strip()+"+"         
#time.sleep(1000)
r = bot_login()
subreddit1 = r.subreddit(Satirsublar)
comments_replied_to = get_saved_comments()


while True:
	run_bot(r, comments_replied_to)


