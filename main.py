import yaml
from twitter import *
from datetime import datetime
import sys
sys.path.append(".")
new_status = "testing testing"

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

twitter = Twitter(auth = OAuth(cfg['twitterkeys']['access_token_key'],
                  cfg['twitterkeys']['access_token_secret'],
                  cfg['twitterkeys']['consumer_key'],
                  cfg['twitterkeys']['consumer_secret']))


results = twitter.statuses.update(status = new_status)
print("updated status: %s" % new_status)