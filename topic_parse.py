#!/usr/bin/python

import fileinput,subprocess
import json
from  topics_data import *


def topic_parase():
    TOPICS = {}
    config = {}
    for line in fileinput.input():
        t,p,r,c = line.split('\t')
        topic = t.split(':')[1]
        config.setdefault(p.split(':')[0],p.split(':')[1])
        config.setdefault(r.split(':')[0],r.split(':')[1])
        TOPICS.setdefault(topic,config)
    return  TOPICS
    #l = len(TOPICS.keys())
    #print TOPICS.keys()[:l/2]
    #print TOPICS.keys()[l/2:]
    #print TOPICS.keys(),len(TOPICS.keys())

def topics_yield(topics,num):
    y = len(topics)
    while y >= num:
         x,y = y,y - num
         yield topics[y:x]
    else:
         if topics[0:y%num]:
             yield topics[0:y%num]

def write_dict_file(dict_data,filename):
    jsObj = json.dumps(dict_data)
    with open(filename,'w') as f:
        f.write(jsObj)

def write_topics2move_file(topics,filename):
    topics2move = {}
    topics2move.setdefault('topics',[{'topic': item} for item in topics])
    topics2move.setdefault('version',1)
    write_dict_file(topics2move,filename)

def gen_reassignment_file(topcis2movefile):
    #output = subprocess.check_output(GENERATE_COMMAND % (ZK_ADDR,topcis2movefile,BROKER_LIST),shell=True)
    output = subprocess.Popen(GENERATE_COMMAND % (ZK_ADDR,topcis2movefile,BROKER_LIST),shell=True,stdout=subprocess.PIPE).communicate()[0]
    #The current assignment should be saved in case you want to rollback to it
    current_assignment = json.loads(output.split('\n')[2])
    new_assignment = json.loads(output.split('\n')[5])
    print current_assignment
    print new_assignment
"topic_parse.py" 73L, 2063C                                                                                                                                                               1,1           Top
