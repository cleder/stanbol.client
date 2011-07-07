'''
Created on Jul 6, 2011

@author: "Yannis Mazzer"
'''
from stanbol.client.base import StanbolCommunicator

class Console(StanbolCommunicator):
    _subpath = 'system/console'
    
    def list_bundles(self):
        response = self._resource.get();
        return self._make_result(response)