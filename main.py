import logger
from llist import LinkedList
import time

log = logger.getLogger(__name__)
log.info("start generating linked list")
start_time = time.time()
llist = LinkedList(range(0, 1000, 2))

# llist.print_list()
# for node in llist:
#     print(node)

print([node for node in llist])
print("--- %s seconds ---" % (time.time() - start_time))
