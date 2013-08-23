#!/usr/bin/env python
 
import os
import sys
import cx_Oracle
 
 
class OracleDB_Library():
   """Library for connecting to Oracle databases."""
 
   def __init__(self):
       os.environ["NLS_LANG"] = "AMERICAN_AMERICA.NEE8ISO8859P4"
       self.con = None
       self.cur = None
 
   def connect_to_database(self, username, password, dsn):
       self.con = cx_Oracle.connect(username, password, dsn)
       self.con.outputtypehandler = OutputTypeHandler
 
   def query_from_file(self, file):
       print os.getcwd()
       fileObj = open(file)
       query = fileObj.read()
       self.cur = self.con.cursor()
       self.cur.execute(query)
       result = self.cur.fetchall()
       self.cur.close()
       return result
 
   def query_from_string(self, string):
       self.cur = self.con.cursor()
       self.cur.execute(string)
       result = self.cur.fetchall()
       self.cur.close()
       return result
 
   def insert_or_delete(self, string):
       self.cur = self.con.cursor()
       self.cur.execute(string)
       self.con.commit()
       self.cur.close()
 
   def disconnect_from_database(self):
       self.con.close()
 
   def decode(self, string):
       return string.decode('latin1')
 
   def delete_tuple_from_list(self, list, value):
       items_to_be_deleted = []
       print 'Deleting tuples from list.'
       print 'List to be inspected: '
       print list
       for index_of_tuple, tuple in enumerate(list):
           for index_of_item, tuple in enumerate(list[index_of_tuple]):
               if value in list[index_of_tuple]:
                   items_to_be_deleted.insert(0, index_of_tuple)
                   break
       print "Tuple in these indexes will be deleted: "
       print items_to_be_deleted
       for index_deletion_item, deletion_index in enumerate(items_to_be_deleted):
           del list[deletion_index]
       return list
 
 
def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
   if defaultType in (cx_Oracle.STRING, cx_Oracle.FIXED_CHAR):
       return cursor.var(unicode, size, cursor.arraysize)
 
 
#test = OracleDB_Library()
#test.connect_to_database('tmdappc_lng5','tmdappc_lng51','Falcon_AT')
#test.disconnect_from_database()