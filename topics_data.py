#!/usr/bin/python

BROKER_LIST = '0,1,2,3,4'
ZK_ADDR = '172.16.10.130:2181'
GENERATE_COMMAND = '/usr/local/kafka_2.9.2-0.8.1.1/bin/kafka-reassign-partitions.sh --zookeeper %s --topics-to-move-json-file %s --broker-list %s --generate'
REASSIGNMENT_EXEC = '/usr/local/kafka_2.9.2-0.8.1.1/bin/kafka-reassign-partitions.sh --zookeeper %s --reassignment-json-file %s --execute --throttle 300000000'
REASSIGNMENT_VERIFY = '/usr/local/kafka_2.9.2-0.8.1.1/bin/kafka-reassign-partitions.sh --zookeeper %s --reassignment-json-file %s --verify'
ALLTOPICS = []
