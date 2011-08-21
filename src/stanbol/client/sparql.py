""" 
@package stanbol.client
Created on Jun 5, 2011
@author: "Encolpe Degoute"
@author: "Jens W. Klein"
@author: "Yannis Mazzer"
"""

from stanbol.client.base import (
    StanbolCommunicator
)
from urllib import urlencode

class SparQL(StanbolCommunicator):
    """

    """
    
    ##
    _subpath = 'sparql'

    def __call__(self, query):
        """

        """
        payload = urlencode({'query' : query})
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self._resource.post(payload=payload, headers=headers)
        return response
    #
#
