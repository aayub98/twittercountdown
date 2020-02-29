import yaml
import twitter
from datetime import datetime
import sys
sys.path.append(".")
new_status = "testing testing"

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

twitter = Twitter(auth = OAuth(cfg['twitterkeys']['consumer_key'],
                  ['twitterkeys']['consumer_secret'],
                  ['twitterkeys']['access_token_key'],
                  ['twitterkeys']['access_token_secret']))


results = twitter.statuses.update(status = new_status)
print("updated status: %s" % new_status)