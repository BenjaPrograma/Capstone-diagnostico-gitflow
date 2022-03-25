import json
import time
from dateutil import parser
from collections import defaultdict

def read_dataset():
    all_data = []
    i = 0
    with open("farmers-protest-tweets-2021-03-5.json", "r", encoding="utf-8") as f:
        for line in f:
            line = line[:len(line)-1]
            all_data.append(json.loads(line))
    return all_data

def top10_dates(all_data):
    
    freq_dict = defaultdict(int)

    for tweet in all_data:
        date = tweet["date"]
        formatted_date = str(parser.parse(date)).split(' ')[0]
        freq_dict[formatted_date] +=1
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
    return list(sorted_dict.keys())[:10]

if __name__ == '__main__':
    a = time.time()
    all_data = read_dataset()
    print(len(all_data))
    b = time.time() - a
    print(b)

    print(top10_dates(all_data))