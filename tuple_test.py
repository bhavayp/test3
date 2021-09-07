import unittest
import MySQLdb
import logging
class TestConnnection(unittest.TestCase): 
     logging.basicConfig(filename=r"C:\Users\nagab\test.log, encoding='utf-8', level=logging.INFO")
     try:
       def test_connection(self): 
            self.db_connection = MySQLdb.connect(
               host = "localhost",
               user = "root",
               password = "bhavyateja",
                     
            )
            self.assertTrue("connection is established")
            
     except:
         logging.error("Some error on working")
         print("erroer occured")

     else:
        logging.info("successfullly working")

class TestTuples(unittest.TestCase):
      def setup(self):
         self.tuple1=("pythonunit testing")
         self.tuple2=("pythonunit testing")
      def test_tuple_eq1(self):
         self.assertTupleEqual(self.tuple1,self.tuple2)
      def test_tuple_eq2(self):
         message = "lists are equal and test failed"
         self.assertTupleNotEqual(self.tuple1,self.tuple2,message)