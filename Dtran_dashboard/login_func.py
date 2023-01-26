# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:21:09 2023

@author: robert
"""

import copy
import decimal
import pandas as pd

from pymongo  import MongoClient
from bson     import ObjectId, Binary
from datetime import datetime

class get_cursor():
    
    def __init__(self, login):
        self.user           = login['mongo_user']
        self.password       = login['mongo_pswd']
        self.mongo_host     = login['mongo_host']
        self.mongo_database = login['mongo_database']
        self.collections    = login['mongo_col']
        self.add_info       = login['mongo_add_info']
        
    def Cursor(self):
        try:
            try:
                myclient = MongoClient(f"mongodb://{self.user}:{self.password}@{self.mongo_host}:27017/{self.add_info}",
                                       serverSelectionTimeoutMS=3000)#192.168.0.150
            except:
                myclient = MongoClient(f"mongodb://{self.mongo_host}:27017/", serverSelectionTimeoutMS=3000)#192.168.0.150   
        except:
            return None
        mydb   = myclient[self.mongo_database]
        mycol  = mydb[self.collections]
        cursor = mycol.find()#get last #records
        return cursor
    
    def xydatas(self, cursor, xtitle, ytitle):
        x = []
        y = []
        for item in cursor:
            x.append(item.get(xtitle))
            y.append(item.get(ytitle))
        return x, y

def find_index(ls, e):
    nls = copy.copy(ls)
    aldex = []
    for ele in e :
        if any(x==ele for x in nls):
      
            indx = ls.index(ele)
            aldex.append(indx)
            #del nls[indx]
        
    return aldex

def read_mongo(login, types):
    user           = login['mongo_user']
    password       = login['mongo_pswd']
    mongo_host     = login['mongo_host']
    mongo_database = login['mongo_database']
    collections    = login['mongo_col']
    add_info       = login['mongo_add_info']
    
    #mongodb connection
    try:
        try:
            myclient = MongoClient(f"mongodb://{user}:{password}@{mongo_host}:27017/{add_info}", serverSelectionTimeoutMS=3000)#192.168.0.150
        except:
            myclient = MongoClient(f"mongodb://{mongo_host}:27017/", serverSelectionTimeoutMS=3000)#192.168.0.150

        if types == 'dbnames':
            return myclient.list_database_names()    
    except:
        return 'fail'
        
    
    mydb = myclient[mongo_database]#'admin'
    if types == 'colnames':
        return mydb.list_collection_names()
    
    mycol = mydb[collections]#'20220424_7'
    if types == 'count':
        return mycol.count_documents({})
    
    if types == 'd_type':
        mx = read_mongo(login, 'size')
        cursor = mx
        try:
            name = list(mx.keys())
        except:
            return 'error'  #no data
        n_type = [type(cursor[j]) for j in name]
        
        indx   = find_index(n_type, [ObjectId, Binary])
        #if len(indx) > 0:
            #log.info(f'{indx} index will be changed into string')
        l = []
        for j in name:
            try:
                l.append(len(cursor[j]))
            except:
                if any(name[x]==j for x in indx):
                    l.append(len(str(cursor[j])))
                else:
                    l.append(None)
        try:
            where = n_type.index(float)
            d = decimal.Decimal(f"{cursor[0][name[where]]}")
            l[where] = -d.as_tuple().exponent
        except:
            pass
        n_type = [str(x)[8:][:-2] for x in n_type]    
        return name, n_type, l
    
    if types == 'title':
        cursor = mycol.find().limit(1)#get last #records
        name = [x.keys() for x in cursor]
        return list(name[0])
    
    if types == 'all':
        cursor = mycol.find({"$query": {}, "$orderby": {"$natural" : -1}}).limit(1000)#get last #records
        str_curs = list(cursor)
        for dicts in str_curs:
            for keys in dicts:
                dicts[keys] = str(dicts[keys])
        df =  pd.DataFrame(str_curs)

        return df
    
    if types == 'size':
        cursor = mycol.find({"$query": {}, "$orderby": {"$natural" : -1}}).limit(1000)#get #records
        try:
            l = 0
            target = 0
            for x in cursor:
                if len(x) > l:
                    l = len(x)
                    target = x
            return target
        except:
            print('no data')
            return None
    
    if types == 'datetime':
        tp = read_mongo(login, 'd_type')
        try:
            index = tp[1].index(datetime)
        except:
            index = None
        return index