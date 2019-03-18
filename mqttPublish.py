import paho.mqtt.client as mqtt  #import the client1
import time


def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)



"""
port=1883

mqtt.Client.connected_flag=False#create flag in class
broker="139.59.4.99"
client = mqtt.Client("python1")             #create new instance 
client.on_connect=on_connect  #bind call back function
client.loop_start()
#client.loop_forever()
print("Connecting to broker ",broker)
client.connect(broker,port)      #connect to broker



while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")

ret=client.publish("house/bulb1","Test massage 1",1)
print("published return",ret)
time.sleep(3)


ret=client.publish("house/bulb1","Test massage 1",2)
print("published return",ret)
time.sleep(3)


ret=client.publish("house/bulb1","Test massage 1",3)
print("published return",ret)
time.sleep(3)



client.loop_stop()    #Stop loop 
client.disconnect() # disconnect
"""


count=1
mqtt.Client.connected_flag=False#create flag in class
broker="139.59.4.99"
port =1883
while True:
	client = mqtt.Client("python1")             #create new instance 
	client.on_connect=on_connect  #bind call back function
	client.loop_start()
	#client.loop_forever()
	print("Connecting to broker ",broker)
	client.connect(broker,port)      #connect to broker
	while not client.connected_flag:
		print("i am in wait state")
		time.sleep(1)
	print(count)
#	count=count+1
	print("I am in main loop")
	ret=client.publish("house/bulb1","Test massage 1",count)

	##
	print("Published return ",ret)
	#time.sleep(10)	
	client.loop_stop()
	client.disconnect()
	time.sleep(100)
