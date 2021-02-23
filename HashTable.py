from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
     
    arr = []

    for i in range(size):
        new_ll = LinkedList()
        arr.append(new_ll)

    return arr




  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    # YO make sure to make my own. Instead of using len of word to find index do something else...
    key_length = len(key)

    index = key_length % self.size

    return index


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    new_data = (key, value)

    # hash
    array_index = self.hash_func(key)

    ll = self.arr(array_index)

    # Only append if this key is not in table
    # If not found, append
    ll_index = ll.find(key)
    if ll_index == -1:
        ll.append(new_data)
    else:
        ll.update(key, value)

    # Otherwise, if this word is already in the table,
    # don't create a new node, just update the value


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for ll in self.arr:
        ll.print_nodes()



