import logger
from llist import LinkedList

log = logger.getLogger(__name__)
log.info("this is a test message %s %s", "yes", "no")

llist = LinkedList(range(0, 100, 2))
# llist.print_list()

print(node.value for node in llist)

