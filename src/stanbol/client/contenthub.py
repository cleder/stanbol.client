""" 
@package stanbol.client
Created on Jun 5, 2011
@author: "Encolpe Degoute"
@author: "Jens W. Klein"
@author: "Yannis Mazzer"
""" 

import urlparse
from restkit.errors import (
    ResourceNotFound
)
from stanbol.client.base import (
    StanbolCommunicator,
    RDFFORMATS,
)

class ContentHub(StanbolCommunicator):
    """
    class ContentHub
    """
    
    _subpath = 'contenthub'

    def __getitem__(self, cid):
        """
        Get raw content back from contenthub.
        @param self: the object itself
        @param cid: 
        """
        headers = {
            'Accept': 'text/plain',
        }        
        path = "raw/%s" % cid
        try:
            response = self._resource.get(path=path, headers=headers)
        except ResourceNotFound, e:
            raise KeyError, cid           
        self._check_response(response, KeyError, 
                             'Cant get content with id %s from stanbol' % id)
        return response.body_string()
    
    def get(self, cid, default=None):
        """
        @param self: the object itself
        @param cid: 
        @param default: 
        """
        try:
            return self[cid]
        except KeyError:
            return default

    def __setitem__(self, cid, payload):
        """
        Adds or updates content to contenthub using given id.
        @param self: the object itself
        @param cid: 
        @param payload:
        """
        headers = {
            'Content-Type': 'text/plain',
        }        
        path = "content/%s" % cid
        response = self._resource.put(path=path, payload=payload, 
                                      headers=headers)
        self._check_response(response, ValueError, 
                             'Can\'t put content with id %s to stanbol' % cid, 
                             code=201)

    def add(self, payload):
        """
        Adds content to contenthub and let FISE create an ID. Returns new ID.
        @param self: the object itself
        @param payload: 
        """
        headers = {
            'Content-Type': 'text/plain',
        }        
        response = self._resource.post(payload=payload, headers=headers)
        self._check_response(response, ValueError, 
                             'Cant put content to fise', code=201)
        path = urlparse.urlparse(response.headers['location']).path
        path = path.split('/')
        return path[-1]        

    def metadata(self, cid, format='rdfxml', parsed=False):
        """
        Get extracted rdf+xml metadata of content with given id.
        @param self: the object itself
        @param cid: 
        @param format: 
        @param parsed: 
        """
        self._check_format(format, parsed)
        headers = {
            'Accept': RDFFORMATS[format],
        }        
        path = "metadata/%s" % cid
        response = self._resource.get(path=path, headers=headers)
        self._check_response(response, KeyError, 
                             'Cant get metadata with id %s from stanbol' % cid)
        return self._make_result(response, format, parsed)
    
    def page(self, cid):
        """
        URL to HTML summary view of the extracted RDF metadata.
        @param self: the object itself
        @param cid:         
        """
        headers = {
            'Accept': 'text/html',
        }        
        path = "page/%s" % cid
        response = self._resource.get(path=path, headers=headers)
        self._check_response(response, KeyError, 
                             'Cant put content with id %s to stanbol' % cid)
        return response.body_string()
