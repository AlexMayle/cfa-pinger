import requests

URL = "https://www.chick-fil-a.com"
RESULTS_FILE = "results.log"

if __name__ == '__main__':
    response = requests.get(URL)
    log_object = dict()
    log_object['headers'] = str(response.headers)
    log_object['content'] = response.text
    with open(RESULTS_FILE, 'a+') as f: 
        f.write(str(log_object))
        f.write('\n\n')
