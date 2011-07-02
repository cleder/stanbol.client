## @package stanbol.client
# Created on Jun 5, 2011
# @author: "Encolpe Degoute"
# @author: "Jens W. Klein"
# @author: "Yannis Mazzer"

import os
import urlparse
from restkit.errors import (
    ResourceNotFound
)
from stanbol.client.base import (
    StanbolCommunicator,
    RDFFORMATS,
)

## class Store
class Store(StanbolCommunicator):
    
    _subpath = 'store'

    ## Get raw content back from store.
    # @param self: the object itself
    # @param cid: 
    def __getitem__(self, cid):
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
    
    ##
    # @param self: the object itself
    # @param cid: 
    # @param default: 
    def get(self, cid, default=None):
        try:
            return self[cid]
        except KeyError:
            return default

    ## Adds or updates content to store using given id.
    # @param self: the object itself
    # @param cid: 
    # @param payload:           
    def __setitem__(self, cid, payload):
        headers = {
            'Content-Type': 'text/plain',
        }        
        path = "content/%s" % cid
        response = self._resource.put(path=path, payload=payload, 
                                      headers=headers)
        self._check_response(response, ValueError, 
                             'Can\'t put content with id %s to stanbol' % cid, 
                             code=201)

    ## Adds content to store and let FISE create an ID. Returns new ID.
    # @param self: the object itself
    # @param payload: 
    def add(self, payload):
        headers = {
            'Content-Type': 'text/plain',
        }        
        response = self._resource.post(payload=payload, headers=headers)
        self._check_response(response, ValueError, 
                             'Cant put content to fise', code=201)
        path = urlparse.urlparse(response.headers['location']).path
        path = path.split('/')
        return path[-1]        

    ## Get extracted rdf+xml metadata of content with given id.
    # @param self: the object itself
    # @param cid: 
    # @param format: 
    # @param parsed: 
    def metadata(self, cid, format='rdfxml', parsed=False):
        self._check_format(format, parsed)
        headers = {
            'Accept': RDFFORMATS[format],
        }        
        path = "metadata/%s" % cid
        response = self._resource.get(path=path, headers=headers)
        self._check_response(response, KeyError, 
                             'Cant get metadata with id %s from stanbol' % cid)
        return self._make_result(response, format, parsed)
    
    ## URL to HTML summary view of the extracted RDF metadata.
    # @param self: the object itself
    # @param cid: 
    def page(self, cid):
        headers = {
            'Accept': 'text/html',
        }        
        path = "page/%s" % cid
        response = self._resource.get(path=path, headers=headers)
        self._check_response(response, KeyError, 
                             'Cant put content with id %s to stanbol' % cid)
        return response.body_string()