#Intro to Redis (NoSql)
import redis

red = redis.StrictRedis(host='localhost', port=6379, db=0)
if red.set('Hell','Bound'):
    print 'All Done !'
    print red.get('Hell')
if red.get(raw_input()):
    print 'Key Exist in DB'
else:
    print 'No Key found'
print 'Flush DB'
red.flushall()

