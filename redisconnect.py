import os
import redis
from dotenv import load_dotenv
import csv
load_dotenv('.env.dev')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    username="default",
    password=REDIS_PASSWORD,
)

with open('conn.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row_id, row in enumerate(csv_reader):
        key = f"conn:{row_id}"
        r.hset(key, mapping=row)
        print(f"Stored {key}: {row}")
        
for key in r.scan_iter("conn:*"):
    print(key, r.hgetall(key))


