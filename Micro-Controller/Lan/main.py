def setup():
    pin_no = (5,4,0,14,12,13,15,10)
    
    return tuple(Pin(i, Pin.OUT).value for i in pin_no)
    
<<<<<<< Updated upstream
do_connect()
=======
#do_connect()
>>>>>>> Stashed changes

def get_link():
    d={
    "host":"192.168.29.157",
    "port":'8888',
    "room_id": '1',
}


    
    link = 'http://'+d['host']+":"+d['port']+"/api/"+d['room_id']+"/"
    return link

def loop():
    link  = get_link()
    pins=setup()
    e=0
    from urequests import get
    from time import sleep
    while 1:
        gc.collect()
        try:
            sleep(0.6)
            respon = get(link).json()['pin_status']

            for i in respon:
                pins[i[0]-1](i[1])
            e=0        
        except:
            e+=1
            if e>=3:
                print('Resetting')
                sleep(1)
                machine.reset()
                
            print('error -',e,'free ram -',gc.mem_free())
            sleep(2)
            do_connect()
            

<<<<<<< Updated upstream
loop()
=======
#loop()
>>>>>>> Stashed changes

