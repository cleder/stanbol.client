## @package stanbol.client
# Created on Jun 5, 2011
# @author: "Encolpe Degoute"
# @author: "Jens W. Klein"
# @author: "Yannis Mazzer"

from stanbol.client.base import (
    StanbolCommunicator,
    RDFFORMATS,
)

## Engines class
#
#
class Engines(StanbolCommunicator):
    
    ##
    _subpath = 'engines'
    
    ## Submit payload to FISE engines and get enhancements back.
    # @param self: the object itself
    # @param payload: content for submission to fise.
    # @type payload: String, Unicode or UTF8, Content-Type 'text/plain'
    # @param format: format to be requested. Does not work toegther with 
    #                'parsed'.
    # @type format: String, one out of 'jsonld', 'rdfxml', 'rdfjson', 
    #                'rdfntriples', 'turtle'.
    # @param parsed: get the result as python 'rdflib.Graph' instance.
    # @type parsed: String or rdflib.Graph instance
    def __call__(self, payload, format='rdfxml', parsed=False):
        self._check_format(format, parsed)
        headers = {
            'Accept': RDFFORMATS[format],
            'Content-Type': 'text/plain',
        }        
        response = self._resource.post(payload=payload, headers=headers)
        return self._make_result(response, format, parsed)