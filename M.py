from node import Node
from node import new_sender
from node import new_listener
from constants import ADDRESS_MC
from constants import ADDRESS_CM

core = Node()

core.add_listener(new_listener(ADDRESS_CM))
core.accept_connection(ADDRESS_CM)
message = core.receive_message(ADDRESS_CM)
print("I received " + message)
core.close_connection(ADDRESS_CM)

core.add_sender(new_sender(ADDRESS_MC))
core.send_message_to_address(ADDRESS_MC, "test test")
core.close_connection(ADDRESS_MC)

