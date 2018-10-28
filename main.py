import requests
from datetime import datetime
import json

URL = "https://www.chick-fil-a.com"
RESULTS_FILE = "/home/ec2-user/cfa-pinger/results.log"

if __name__ == '__main__':
    response = requests.get(URL)
    log_object = dict()
    log_object['timestamp'] = str(datetime.now())
    log_object['status'] = response.status_code
    log_object['headers'] = str(response.headers)
    log_object['content'] = response.text
    with open(RESULTS_FILE, 'a+') as f: 
        f.write(json.dumps(log_object))
