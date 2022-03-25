import json
import time
from operator import itemgetter


def read_dataset():
    all_data = []
    i = 0
    with open("farmers-protest-tweets-2021-03-5.json", "r", encoding="utf-8") as f:
        for line in f:
            line = line[:len(line)-1]
            all_data.append(json.loads(line))
    return all_data

def top_10_most_retweeted(all_data):
    top_10 = sorted(all_data, key=itemgetter('retweetCount'), reverse=True)[:10]
    return top_10


if __name__ == '__main__':
    a = time.time()
    all_data = read_dataset()
    print(len(all_data))
    b = time.time() - a
    print(b)