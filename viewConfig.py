'''
Created on Mar 26, 2017

@author: sginne
'''
import database

if __name__ == '__main__':
    DbObject=database
    routers=DbObject.ListRouters()
    ports=DbObject.ListPorts("")
    for router in routers:
        print ("We've got router with id {}, by the name {}".format(router.Id,router.Name))
        print ("Belonging ports:")
        ports=DbObject.ListPorts("")
        for port in ports:
            if port.RouterId==router.Id:
                print("Port id={}, with IP={}".format(port.Id,port.Ip))
       
       
