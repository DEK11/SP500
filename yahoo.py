import urllib.request
import os
import time

path = "/home/debasish/Downloads/intraQuarter"

def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in sorted(stock_list)[1:]:
        try:
            e = e.replace("/home/debasish/Downloads/intraQuarter/_KeyStats/","")
            link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
            resp = urllib.request.urlopen(link).read()
            save = "forward/"+str(e)+".html"
            store = open(save,"w")
            store.write(str(resp))
            store.close()

        except Exception as e:
            print(str(e))


Check_Yahoo()
