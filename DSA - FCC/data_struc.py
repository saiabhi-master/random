#Data Structure: a data storage format
#It is collec of values and the format they are stored in

#array: stores a collection of values where each value is refrenced using an index/key
# in some language, arrays are homogenous (java) and hetergenous in others(python)
# stored in blocks of memory next to each other ( contiguous )
# Non-contiguous ==> Linked Lists

#Operations on DS: access & read values, Search, Insert, Data

#python list growth (list resize ) : 0, 4, 8, 16, 25, 35, 46
#on average, append operation has constant time complexity
#delete operations have an upper bound of O(n) run time

# linked lists are better when there is more inserting and deleting than accessing
#linked Lists: linear data structure where each element in the list is contained
#in seperate object called Node, contains element and reference to the next node

#singly linked list: each node ref to next node
#doubly linked list: each node stores reference for next and before node

#Building singly linked list

class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<None data: %s>" %self.data



class Singlylinkedlist:

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """"
        Inserts new node at index position
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
             if current.data == key and current is self.head:
                 found = True
                 self.head = current.next_node

             elif current.data == key:
                 found = True
                 previous.next_node = current.next_node

             else:
                previous = current
                current = current.next_node

        return current

# l1 = Singlylinkedlist()
# l1.add(3)
# l1.add(9)
# l1.add(8)
# l1.insert("Hi", 1)
# l1.remove(9)
# print(l1)

#-----------------------------------------------------------


