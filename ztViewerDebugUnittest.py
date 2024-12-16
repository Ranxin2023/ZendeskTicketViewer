import unittest
from ztViewerDebug import getBulkData,ztViewer

class testDemo(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        print('setup\n')
        
    @classmethod
    def tearDownClass(cls):
        print('tear down\n')
        
    def setUp(self):
        print("prepare environment...\n")
        
    def tearDown(self):
        print('clean up...\n')
    
    def testNumOfTickets(self):
        print("Test1: test total number of tickets...\n")
        print("please enter option #1 and quit for this case")
        result=ztViewer()
        self.assertEqual(203,result[0])
        print()
        
    def testSubjectOfCertainTicket(self):
        print("Test2: test #59 ticket's subject...\n")
        print("Please enter option #2, ticket number 59, and 'quit' after the input of the ticket number.\n")
        result=ztViewer()
        self.assertEqual("incididunt mollit pariatur esse esse",result[len(result)-1]['ticket']['subject'])
        print()

    def testUpdatedDateOfCertainTicket(self):
        print("Test3: test #222 ticket's update date...\n")
        print("Please enter option #2,  ticket number 222, and 'quit' after the input of the ticket number.\n")
        result=ztViewer()
        self.assertEqual("2021-11-28T09:17:09Z",result[len(result)-1]['ticket']['updated_at'])
        print()
    
    def testWrongUsername(self):
        print("Test4: test wrong username...\n")
        print("Please enter a wrong username and choose any option for the menu")
        result=ztViewer()
        self.assertEqual(401, result)
        print()
    def testWrongPassword(self):
        print("Test5: test wrong username...\n")
        print("Please enter a wrong password and choose any option for the menu")
        result=ztViewer()
        self.assertEqual(401, result)
        print()
        
if __name__=='__main__':
    unittest.main()
    
