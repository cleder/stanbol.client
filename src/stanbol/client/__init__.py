##
# Created on Jun 5, 2011
# @author: "Encolpe Degoute"
# @author: "Jens W. Klein"
# @author: "Yannis Mazzer"
    
from restkit.globals import set_manager, get_manager
try:
    import eventlet
    eventlet.monkey_patch()
    from restkit.manager.meventlet import EventletManager
    set_manager(EventletManager(timeout=60))
except ImportError:
    from restkit import Manager
    set_manager(Manager(max_conn=10))

from stanbol.client.engines import Engines 
from stanbol.client.contenthub import ContentHub
from stanbol.client.entityhub import EntityHub, EntityHubSite
from stanbol.client.console import Console

class Stanbol(object):
    
    def __init__(self, baseuri):
        self.baseuri = baseuri
        
    @property
    def engines(self):
        return Engines(self.baseuri)

    @property
    def contentHub(self):
        return ContentHub(self.baseuri)

    @property
    def entityHub(self):
        return EntityHub(self.baseuri)

    @property
    def entityHubSite(self):
        return EntityHubSite(self.baseuri)
    
    @property
    def console(self):
        return Console(self.baseuri)

