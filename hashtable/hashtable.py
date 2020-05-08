class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.element_count = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        hash_value = 0

        for byte in key.encode('utf-8'):
            hash_value = hash_value * 0x100000001b3
            hash_value = hash_value ^ byte(byte)
        return hash_value

        

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash_value = 5381

        for byte in key.encode('utf-8'):
            hash_value = ((hash_value * 33) + hash_value) + byte # hash * 33 + byte
        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ## simple implemntation
        # index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)

        # find the has index
        # search the list for the key
        # if there, replace the value
        # if not, append new record to the list
        index = self.hash_index(key)
        node = self.storage[index]

        if node is None:
            self.element_count += 1
            self.storage[index] = HashTableEntry(key, value)

            if (self.element_count / self.capacity) >= 0.7:
                self.resize()

        while node is not None:
            if node.key == key:
                node.value = value
            if node.next is None:
                self.element_count += 1
                node.next = HashTableEntry(key, value)

                if (self.element_count / self.capacity) >= 0.7:
                    self.resize()

                break

            node = node.next
            




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Simple Implementation
        # index = self.hash_index(key)
        # self.storage[index] = None

        # Find the index hash table
        # Search the list for the key
        # If found delete the node from the list and return warning
        # else return none
        index = self.hash_index(key)
        node = self.storage[index]
        
        prev = None
        while node is not None:
            # node.key is key
                # if the previous node
                    # previous.next equals node.next (essential removing the node from the linked list)
                # else our hashtable is at the head, self.storage[index] = node.next
            # iterations
            # prev is node
            # node is node.next
            if node.key == key:
                if prev:
                    self.element_count -= 1
                    prev.next = node.next

                    if (self.element_count / self.capacity) <= 0.2:
                        self.resize()
                else:
                    self.element_count -= 1
                    self.storage[index] = node.next

                    if (self.element_count / self.capacity) <= 0.2:
                        self.resize()
            prev = node
            node = node.next
        return "Item not found"


        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # simple implementation
        # index = self.hash_index(key)
        # return self.storage[index].value if self.storage[index] is not None else None

        # find hash index
        # search list for key
        # if found return value
        # else return none

        index = self.hash_index(key)
        node = self.storage[index]

        if node is None:
            return None

        while node is not None:
            if node.key == key:
                return node.value
            if node.next is None:
                return None

            node = node.next

    def resize(self, new_capacity=0):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        if new_capacity == 0:
            new_capacity = 2
        else:
            new_capacity = new_capacity

        if (self.element_count / self.capacity) >= 0.7:
            self.capacity = int(self.capacity * 2)

        elif (self.element_count / self.capacity) <= 0.2:
            self.capacity = int(self.capacity / 2)

        else:
            self.capacity = new_capacity

        new_storage = [None] * self.capacity
        for index in self.storage:
            node = index
            while node is not None:
                h = self.hash_index(node.key)
                if new_storage[h] is None:
                    new_storage[h] = node
                else:
                    new_storage[h].next = node
                node = node.next
        self.storage = new_storage

    def __len__(self):
        return self.capacity      


    def __setitem__(self, key, value):
        return self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.delete(key)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
