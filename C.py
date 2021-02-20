from node import Node
from node import new_sender
from node import new_listener
from constants import ADDRESS_MC
from constants import ADDRESS_CM

core = Node()

core.add_sender(new_sender(ADDRESS_CM))
core.add_listener(new_listener(ADDRESS_MC))

core.send_message_to_address(ADDRESS_CM, "test")
core.close_connection(ADDRESS_CM)

core.accept_connection(ADDRESS_MC)
print(core.receive_message(ADDRESS_MC))

core.close_connection(ADDRESS_MC)
