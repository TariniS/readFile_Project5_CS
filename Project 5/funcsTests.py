#Name: Tarini Srikanth
#Instructor: Clark Turner
#Project 5 - Tests

import unittest
from fileMatchingFuncs import *

#wrote test cases for the functions. The first two do not match due to an error in the test
#cases that was discussed in class. However, the two output files are correct when running my 
#code. 

class TestCases(unittest.TestCase):
          
   def test_entry_init(self):
      entry = Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO')
      self.assertEqual(entry.account_num, '345')
      self.assertEqual(entry.name, 'Bob Jones')
      self.assertAlmostEqual(entry.balance, 87.12)
      self.assertEqual(entry.phone, '8055551234')
      self.assertEqual(entry.city, 'SLO')   

   def test_read_file_0(self):
      entries = []
      entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
      entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
      # call read_file with 'test0.dat'
      self.assertEqual(read_file('test0.dat'), entries)

   def test_read_file_1(self):
      entries = []
      entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
      entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
      entries.append(Entry('300', 'Mary Smith', 27.19, '8057901237', 'Santa_Maria'))
      entries.append(Entry('800', 'Mike Rosen', -104.58, '8051200891','Pismo_Beach'))
      # call read_file with 'test1.dat'
      self.assertEqual(read_file('test1.dat'), entries)

   def test_sort(self):
      #testing the sort function
      entries = []
      entry1= Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO')
      entries.append(entry1)
      entry2= Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO')
      entries.append(entry2)
      entry3=Entry('300', 'Mary Smith', 27.19, '8057901237', 'Santa_Maria')
      entries.append(entry3)
      entry4= Entry('800', 'Mike Rosen', -104.58, '8051200891','Pismo_Beach')
      entries.append(entry4)
      newListOfEntries=[]
      newListOfEntries.append(entry1)
      newListOfEntries.append(entry3)
      newListOfEntries.append(entry2)
      newListOfEntries.append(entry4)
      self.assertEqual(sort(entries),newListOfEntries)
      
      # call read_file with 'test1.dat'

       

      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

