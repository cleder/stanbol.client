#'''
#Created on Jun 7, 2011
#
#@author: "Yannis Mazzer"
#'''
#import unittest
#import doctest 
#from pprint import pprint
#from interlude import interact
#
#optionflags = doctest.NORMALIZE_WHITESPACE | \
#              doctest.ELLIPSIS | \
#              doctest.REPORT_ONLY_FIRST_FAILURE
#
#TESTFILES = [
#    'engines.txt',
#    'store.txt',
#]
#
#
#
#
#class Test(unittest.TestCase):
#
#
#    def testName(self):
#        pass
#
#    def testSuite(self):
#        return unittest.TestSuite([
#            doctest.DocFileSuite(
#                file, 
#                optionflags=optionflags,
#                globs={'interact': interact,
#                       'pprint': pprint},
#            ) for file in TESTFILES
#        ])
#
#if __name__ == "__main__":
#    #import sys;sys.argv = ['', 'Test.testName']
#    #doctest.testmod()
#    unittest.main()
#    
##if __name__ == '__main__':                  #pragma NO COVERAGE
##    unittest.main(defaultTest='test_suite') #pragma NO COVERAGE







import unittest
import doctest 
from pprint import pprint
from interlude import interact

optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE

TESTFILES = [
    'engines.txt',
    'store.txt',
]

def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            file, 
            optionflags=optionflags,
            globs={'interact': interact,
                   'pprint': pprint},
        ) for file in TESTFILES
    ])

if __name__ == '__main__':                  #pragma NO COVERAGE
    unittest.main(defaultTest='test_suite') #pragma NO COVERAGE