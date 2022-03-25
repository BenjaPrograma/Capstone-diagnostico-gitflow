import json
import time
from collections import defaultdict
from operator import itemgetter


def read_dataset():
    all_data = []
    with open("farmers-protest-tweets-2021-03-5.json", "r", encoding="utf-8") as f:
        for line in f:
            line = line[:len(line)-1]
            all_data.append(json.loads(line))
    return all_data


def top_10_tweeters(all_data):
    freq_dict = defaultdict(int)

    user_id_to_user = dict()
    for tweet in all_data:
        user_id = tweet["user"]["id"]
        freq_dict[user_id] +=1
        if user_id not in user_id_to_user:
            user_id_to_user[user_id] = tweet["user"]
    top10 = dict(sorted(freq_dict.items(), key=lambda x:x[1], reverse=True))
    return [user_id_to_user[_id] for _id in list(top10.keys())[:10]]

def top_10_most_retweeted(all_data):
    top_10 = sorted(all_data, key=itemgetter('retweetCount'), reverse=True)[:10]
    return top_10



if __name__ == '__main__':
    a = time.time()
    all_data = read_dataset()
    print(len(all_data))
    b = time.time() - a
    print(b)
