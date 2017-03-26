'''
Created on Mar 26, 2017

@author: sginne
'''
import database

if __name__ == '__main__':
    dbObject=database
    dbObject.initSQL('fill.sql') #reinitialize database
    dbObject.listRouters()
    