import gcimport uos, machinefrom time import timefrom machine import Pingc.collect()    def do_connect():    import network    import json    t1=time()    sta_if = network.WLAN(network.STA_IF)    if sta_if.isconnected():        print('wifi already connected')        return True    else:        print('connecting to network..a.')        sta_if.active(True)        with open('wifi.json', 'r') as f:            d=json.load(f)        sta_if.connect(d['wifi'], d['password'])        while not sta_if.isconnected():            pass                    print('network config:', sta_if.ifconfig())        t = str(time()-t1)        print('Took '+t+' seconds in connecting ')    