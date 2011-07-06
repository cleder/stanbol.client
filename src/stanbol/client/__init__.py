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

class Stanbol(object):
    
    def __init__(self, baseuri):
        self.baseuri = baseuri
        
    @property
    def engines(self):
        return Engines(self.baseuri, pool=self.pool)

    @property
    def store(self):
        return ContentHub(self.baseuri, pool=self.pool)

