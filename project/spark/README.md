### setup up hadoop and spark using docker-compose

# from https://bitbucket.org/uhopper/hadoop-docker

# issues:

1. need to create spark-logs in namenode of hdfs

```
hadoop fs -mkdir /spark-logs
```

2. install python in spark container

```
apt-get install python-setuptools python-dev build-essential
easy_install pip
pip install --upgrade virtualenv
pip install -U nltk
```

3. prepare pyspark

```
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.1-src.zip:$PYTHONPATH
```

4. make sure docker-compose version > 1.6
