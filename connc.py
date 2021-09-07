import unittest
import MySQLdb
class TestConnnection(unittest.TestCase):
       def test_connection(self): 
            self.db_connection = MySQLdb.connect(
               host = "localhost",
               user = "root",
               password = "bhavyateja",
                     
            )
            self.assertTrue("connection is established")
            