import redis

import json


redis_host = 'localhost'
redis_port = 6379
redis_pass = ''
redis_db = 0

rd = redis.Redis(host=redis_host, port=redis_port, password=redis_pass, db=redis_db)

with open("person.json") as p:
    data = json.load(p)
    
with rd.pipeline(data) as pipe:
    for id, person in enumerate(data, start=1):
        print(person)
        pipe.hsetnx("persons", id, str(person))
        