from LinkedList import LinkedList
from datetime import date

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)



  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
     
    array = []

    for i in range(size):
        new_linked_list = LinkedList()
        array.append(new_linked_list)

    return array



  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    # Takes the number of the current day and either divides it by the word length or gets divided by the word length
    # depending on which number is greater
    today = date.today()
    day_number = int(today.strftime('%d'))
    word_length = len(key)

    if day_number > word_length:
      x = day_number / word_length
    else:
      x = word_length / day_number

    index = int(x) % self.size

    return index



  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    new_data = (key, value)

    array_index = self.hash_func(key)

    linked_list = self.arr[array_index]

    # Only append if this key is not in table.
    # If not found, append
    ll_index = linked_list.find(key)
    if ll_index == -1:
        linked_list.append(new_data)
    # Otherwise, if this word is already in the table,
    # don't create a new node, just update the value
    else:
       linked_list.update(key)



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



