import yaml
from twitter import *
from datetime import datetime
import sys
import time
sys.path.append(".")

#the part where you figure out how many days are left
def calculate_dates():
    now = datetime.now()
    gradDay = datetime(2020, 5, 15)
    return (gradDay - now.today()).days + 1

new_status = 'happy ' + str(calculate_dates()) + ' days until grad'

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

while True:
    if (datetime.now().hour is 9 and datetime.now().minute is 0 and datetime.now().second is 0):
        twitter = Twitter(auth = OAuth(cfg['twitterkeys']['access_token_key'],
                  cfg['twitterkeys']['access_token_secret'],
                  cfg['twitterkeys']['consumer_key'],
                  cfg['twitterkeys']['consumer_secret']))
        results = twitter.statuses.update(status = new_status)
        time.sleep(5)
# print("updated status: %s" % new_status)

