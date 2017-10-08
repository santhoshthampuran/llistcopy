import logger
from llist import LinkedList
import time

log = logger.getLogger(__name__)
log.info("generating linked list...")
start_time = time.time()
llist = LinkedList(range(0, 100, 2))
log.info("elements in the linked list are:")
log.info([node for node in llist])
log.info("copying linked list...")
llist_copy = llist.copy_linked_list()
log.info("elements in the copy of the linked list are:")
log.info([node for node in llist_copy])
log.info("--- execution time = %s seconds ---" % (time.time() - start_time))
