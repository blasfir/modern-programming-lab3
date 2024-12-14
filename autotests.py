import unittest
from observer import SubclassSubject, Observer


class TestObserver(Observer):
    
    def __init__(self):
        self.update_called = False

    def update(self, subject: SubclassSubject) -> None:
        self.update_called = True


class TestObserverPattern(unittest.TestCase):

    def setUp(self):

        SubclassSubject._observers = []

    def test_attach(self):

        subject = SubclassSubject()
        observer = TestObserver()
        self.assertEqual(len(subject._observers), 0) 
        subject.attach(observer)
        self.assertEqual(len(subject._observers), 1)
        self.assertIn(observer, subject._observers)

    def test_detach(self):
        
        subject = SubclassSubject()
        observer = TestObserver()
        subject.attach(observer)
        subject.detach(observer)
        self.assertEqual(len(subject._observers), 0) 
        self.assertNotIn(observer, subject._observers)

    def test_inform(self):
        
        subject = SubclassSubject()
        observer1 = TestObserver()
        observer2 = TestObserver()
        subject.attach(observer1)
        subject.attach(observer2)
        subject.inform()  
        self.assertTrue(observer1.update_called)
        self.assertTrue(observer2.update_called)

    def test_business_logic(self):
        
        subject = SubclassSubject()
        initial_state = subject._state
        subject.some_business_logic() 
        self.assertNotEqual(subject._state, initial_state) 


if __name__ == "__main__":
    unittest.main()