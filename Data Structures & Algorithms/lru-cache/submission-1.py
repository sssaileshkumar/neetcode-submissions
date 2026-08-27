class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Add a node just before the tail
    # This means it becomes the most recently used
    def add_to_mru(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        # Key doesn't exist
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]

        # Move node to MRU position
        self.remove(node)
        self.add_to_mru(node)

        return node.value

    def put(self, key, value):
        # Key already exists
        if key in self.hashmap:
            node = self.hashmap[key]

            # Update value
            node.value = value

            # Move to MRU position
            self.remove(node)
            self.add_to_mru(node)

            return

        # Create new node
        node = Node(key, value)
        # Add to hash map
        self.hashmap[key] = node
        # Add to MRU position
        self.add_to_mru(node)
        # Cache exceeded capacity
        if len(self.hashmap) > self.capacity:
            # Least recently used node
            lru = self.head.next
            # Remove from linked list
            self.remove(lru)
            # Remove from hash map
            del self.hashmap[lru.key]
