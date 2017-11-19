## tinyurl

### setup

1. git config --global core.editor vim
1. git config --global --edit
1. install [vimrc](https://github.com/amix/vimrc) 
1. sudo yum install python36
1. sudo pip install virtualenv
1. sudo python36 -m pip install --upgrade pip setuptools wheel virtualenv tox
1. python36 -m tox
1. source .tox/py36/bin/activate
1. python api.py
1. curl http://127.0.0.1:5000/
1. `curl -v http://127.0.0.1:5000/shorten -X POST -d "url=https://www.google.com"`
1. `curl -v -L http://127.0.0.1:5000/xxx`
1. python run_keygen.py

### scenarios

#### functional

1. user can get short url given original url
1. user can redirect to original url using short url
1. user can add custom url
1. url can have expiration time

#### non-functional

1. short url can't be guessable
1. add analytics data

#### estimation

* Assumption
  * write 500M req/month
  * read/write ratio = 100
  * size of url object = 500 byte

* QPS
  * write: 500M req/month = 500M / (30 * 24 * 3600) =~ 200 req/s
  * read: 500M * 100 req/month = 500M * 100 / (30 * 24 * 3600) =~ 20K req/s 

* Storage (5 years)
  * number of urls: 500M * 12 * 5 = 30B
  * size: 30B * 500 byte = 15PB

* Bandwidth
  * write: 200 req/s * 500 byte = 100 KB/s
  * read: 20K req/s * 500 byte = 10 MB/s

* Memory (80/20 rules, 20% of daily read should be cached)
  * 20K req/s * 500 byte * 24 * 3600 * 0.2 =~ 172GB

### service

#### TinyUrlService

* POST createUrl(api_key, original_url, custom_alias=None, expired_at=None)
  * return short url if success
  * otherwise, return http error

* DELETE deleteUrl(api_key, short_alias):
  * return 200
  * otherwise, return 404, 403, 401

* GET <short_url>
  * return 301 and Host header with original url
  * otherwise return 404

#### KeyGenService

* base64, i.e. [0-9a-zA-Z-.]
  * 6 letters: 64^6 =~ 68.7B > 30B, should be enough for 5 years!
  * 7 letters: 64^7 =~ 4.4T
  * 8 letters: 64^8 =~ 281T
* generate url id offline with 6 random letters

#### CacheService

* use memcached

### storage

* use NoSQL, e.g. Cassandra
  * no complex relationship
  * billions of records

* Schemas

|   | url |
| -- | -- |
| PK | id: varchar(6) |
|    | url: varchar(512) |
|    | created_at: datetime |
|    | expired_at: datetime |

|   | custom_url |
| -- | -- |
| PK | id: varchar(32) |
|    | url: varchar(512) |
|    | created_at: datetime |
|    | expired_at: datetime |

### work solution

![CreateUrl](https://github.com/jwyx3/practices/tree/master/project/tinyurl/diagrams/CreateUrl.svg)

![GetUrl](https://github.com/jwyx3/practices/tree/master/project/tinyurl/diagrams/GetUrl.svg)

### scale


### stack

* flask
* cassandra
* redis

### refer

![lua-redis](https://www.redisgreen.net/blog/intro-to-lua-for-redis-programmers/)
![spop-not-valid-in-lua](https://github.com/antirez/redis/issues/2139)

### issue

* keygen: not random enough
* no expired_at, stats
* duplicate between url and custom_url
