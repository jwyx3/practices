## topk-music

similar to recommand system

### setup

* install ab: `sudo yum install httpd-tools`
* run `bash test.sh`
* run `bash test_10k.sh`

### senarios

* log listening activity of each music
* return topk music last 7 days

### estimation

### service

#### MusicService

* listened(music_id, user_id)
 * add log into cassandra

* topk(name='top10_last_7_day')
 * run spark/mapreduce to get count of music for last hour
 * update last 7 days data
 * get topk of last 7 days again

### storage

|  | ListenLog |
| -- | -- |
| pk | uuid:varchar(16) |
| pk | timestamp:int(4) |
|  | user_id:varchar(8) |
|  | music_id:varchar(8) |

* uuid.uuid4(): 16 bytes, make log load even
* timestamp: log time
* user_id: how many user??
* music_id: how many music??


|  | Music |
| -- | -- |
| pk | music_id:varchar(8) |
| pk | timestamp:int(4) |
|  | count:int(8) |

* timestamp: the count of following one hour
* count: =~ 256T
* need ttl?


|  | TopkMusic |
| -- | -- |
| pk | name:varchar(256) |
|  | musics:int(?) |

* name: aggregation name, e.g. top10_last_7_day
* musics: cassandra collection??
* cached this table into redis to fast read

### scale

### stack

* flask
* cassandra
* redis
* mapreduce/spark

### thinking

* distribute load can be achieved by two ways
 * too much data: distribute data into multiple shard
 * too much requests: distribute requests into multiple replicas
