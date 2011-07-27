## @package stanbol.client
# Created on Jun 5, 2011
# @author: "Encolpe Degoute"
# @author: "Jens W. Klein"
# @author: "Yannis Mazzer"


import os
import restkit
import rdflib

RDFFORMATS = {
    'jsonld'     : 'application/json',
    'rdfxml'     : 'application/rdf+xml',
    'rdfjson'    : 'application/rdf+json',
    'rdfntriples': 'text/rdf+nt',
    'turtle'     : 'text/turtle',
}

## StanbolCommunicator is the base class of the stanbol client 
#
#
class StanbolCommunicator(object) :
    
    
    ## The constructor of the StanbolCommunicator class
    # @param self: the object itself
    # @param baseuri: the base uri of the stanbol webservice
    # @param pool:
    def __init__(self, baseuri):
        ''' The constructor of the StanbolCommunicator class
        
        '''
        self._baseuri = baseuri
        self._instance = None
      
    ## The complete uri of the service including the subpath from subclasses
    # @param self: the object itself
    # @return: the uri of the stanbol webservice
    @property
    def _uri(self):
        return os.path.join(self._baseuri, self._subpath)

    ## 
    # @param self: the object itself
    # @return:         
    @property
    def _resource(self):        
        return restkit.Resource(self._uri)
    
    ##
    # @param self: the object itself
    # @param format: format to be requested. Does not work toegther with 
    #                'parsed'.
    # @type format: String, one out of 'jsonld', 'rdfxml', 'rdfjson', 
    #                'rdfntriples', 'turtle'.
    # @param parsed:
    def _check_format(self, format, parsed):
        if parsed and format != "rdfxml":
            raise ValueError, "If you want it parsed do not touch the format!"
        if format not in RDFFORMATS:
            raise ValueError, 'Format "%s" is not possible.' % format
        
    ##
    # @param self: the object itself
    # @param response:
    # @param exception_cass:
    # @param errormsg:
    # @param code:      
    def _check_response(self, response, exception_class, errormsg, code=200):
        if response.status_int != code:
            raise exception_class, '%s Status %i' % (errormsg, 
                                                     response.status_int)

    ##
    # @param self: the object itself
    # @param response:
    # @param format: format to be requested. Does not work toegther with 
    #                'parsed'.
    # @type format: String, one out of 'jsonld', 'rdfxml', 'rdfjson', 
    #                 'rdfntriples', 'turtle'.
    # @param parsed:     
    def _make_result(self, response, format, parsed):
        if not parsed:
            return response.body_string()
        graph = rdflib.Graph()
        graph.parse(source=response.body_stream(), format='xml')
        return graph

