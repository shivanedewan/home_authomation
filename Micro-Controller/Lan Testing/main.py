def setup():
    pin_no = (5,4,0,14,12,13,15,10)
    
    return tuple(Pin(i, Pin.OUT).value for i in pin_no)
    
do_connect()

def loop():
    server  = 'http://192.168.29.157:8888/'
    room    = str(2)
    pins=setup()
    e=0
    from urequests import get
    from time import sleep
    # while 1:
    #     gc.collect()
    #     try:
    #         sleep(0.6)
    #         respon = get(server+room+'/?format=json').json()['appliance_set']
            
    #         for i, pin in enumerate(pins):
    #             pin(respon[i]['status'])
    #         e=0        
    #     except:
    #         e+=1
    #         if e>=3:
    #             print('Resetting')
    #             sleep(1)
    #             machine.reset()
                
    #         print('error -',e,'free ram -',gc.mem_free())
    #         sleep(2)
    #         do_connect()
            


loop()
