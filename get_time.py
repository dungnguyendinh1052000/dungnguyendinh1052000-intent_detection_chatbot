
def get_time():
    import time
    import os
    import ntplib 

    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')

    time_=str(time.localtime(response.tx_time)[3])+":"+str(time.localtime(response.tx_time)[4])+" "+str(time.localtime(response.tx_time)[2])+'/'+str(time.localtime(response.tx_time)[1])+'/'+str(time.localtime(response.tx_time)[0])
    
    return time_
