from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): 


# setUp and tearDown are special methods which get run before and after each test. 
# in that tearDown will run even if there’s an error during the test itself.[4] 
# I’m using them to start and stop our browser—note that they’re a bit like a try/except,
# No more Firefox windows left lying around!
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) 

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  #We use self.assertIn instead of just assert to make our test assertions. unittest provides lots of helper functions like this to make test assertions, like assertEqual, assertTrue, assertFalse, and so on. 
        self.fail('Finish the test!')  # We use self.assertIn instead of just assert to make our test assertions. unittest provides lots of helper functions like this to make test assertions, like assertEqual, assertTrue, assertFalse, and so on. 


if __name__ == '__main__':  #  we have the if __name__ == '__main__' clause (if you’ve not seen it before, that’s how a Python script checks if it’s been executed from the command line, rather than just imported by another script). We call  unittest.main()
    unittest.main(warnings='ignore')