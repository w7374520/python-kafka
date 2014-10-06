# -*- coding: utf-8 -*-
#!/usr/bin/python
#encoding=utf-8
import threading, logging, time
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer


class Producers:
    def __init__(self, address):
        print("exec class Producer")
        self.address = address

    def __del__(self):
        print('--Bye!--')

    def run(self):
        print("debug1")
        client = KafkaClient(self.address)  
        print("debug2")
        producer = SimpleProducer(client)

        #while True:
        print("send message now:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        producer.send_messages('test', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

class Consumers:
    def __init__(self, address):
        print("exec class Consumer")
        self.address = address

    def __del__(self):
        print('--Bye!--')

    def run(self):
        client = KafkaClient(self.address)
        consumer = SimpleConsumer(client, "test-group", "my-topics")
        #print(consumer.get_message())

if __name__ == "__main__":
    p = Producers("192.168.1.107:9092")
    p.run()
    ''' 
    for count in xrange(0,1):
        p = Producers('192.168.1.114:9092')
        p.run()
        time.sleep(2)
    '''
    #c = Consumers("localhost:9092")
    #c = Consumers("192.168.1.114:9092")
    #c.run()

