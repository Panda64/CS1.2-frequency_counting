from Node import Node
# Fix indents

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
        # Change this too. Don't print if empty
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
          # Change below
        print(f'Node {i}: {current.data}')
        current = current.next

  def update(self, value):
      # Fix this method
      current_node = self.head

      found = False
      counter = 0

      while current != None and not found:
          if current.data[0] == key:
              current.data = (current.data[0], current.data[1]+1)
          else:
              current = current.next