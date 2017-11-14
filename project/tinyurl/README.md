## tinyurl

### setup

1. git config --global core.editor vim
1. git config --global --edit
1. install [vimrc](https://github.com/amix/vimrc) 

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
  1. write 500M req/month
  1. read/write ratio = 100
  1. size of url object = 500 byte

* QPS
  1. write: 500M req/month = 500M / (30 * 24 * 3600) =~ 200 req/s
  1. read: 500M * 100 req/month = 500M * 100 / (30 * 24 * 3600) =~ 20K req/s 

* Storage (5 years)
  1. number of urls: 500M * 12 * 5 = 30B
  1. size: 30B * 500 byte = 15PB

* Bandwidth
  1. write: 200 req/s * 500 byte = 100 KB/s
  1. read: 20K req/s * 500 byte = 10 MB/s

* Memory (80/20 rules, 20% of daily read should be cached)
  1. 20K req/s * 500 byte * 24 * 3600 * 0.2 =~ 172GB

### service


### storage


### scale


