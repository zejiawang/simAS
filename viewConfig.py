'''
Created on Mar 26, 2017

@author: sginne
'''
import database

if __name__ == '__main__':
    dbObject=database
    routers=dbObject.listRouters()
    for router in routers:
        name=router[1]
        id=router[0]
        print ("We have router by name '{}', with id={}".format(name,id))
        print ("Ports belonging to router are:")
        ports=dbObject.listPorts('WHERE Router_Id={}'.format(id))
        for port in ports:
            print ("Port {} with assigned ip={}".format(port[0],port[2]))