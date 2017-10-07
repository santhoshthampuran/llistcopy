import logger
from llist import LinkedList

log = logger.getLogger(__name__)
log.info("this is a test message %s %s", "yes", "no")

llist = LinkedList(range(0, 100, 2))
# llist.print_list()

for node in llist:
    print(node)

print([node for node in llist])

