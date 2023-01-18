from data_struc import Singlylinkedlist

def merge_sort(linked_list):
    """
    sorts linked list in ascending order
    - recursively divides the linked list into sublists containing a single node
    - repeatedly merges sublists to produce sorted sublists until one remains
    returns sorted linked lists
    runs in (kn log n)
    """


    if linked_list.size() == 1:
        return linked_list

    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    divide unsorted list at midpoint into sublists
    split - O(k log n) time - k for slicing
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1) # O(K) - time

        left_half = linked_list
        right_half = Singlylinkedlist()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):

    """
    merges two linked lists, sorting by data in nodes
    returns a new, merged list
    O(K) - linear time
    """

    # create a new linked list that conataines nodes from
    # merging left and right
    merged = Singlylinkedlist()

    # add a fake head that is discarded later
    merged.add(0)

    # set current to head of linked list
    current = merged.head

    # obtain head nodes for left and right linked list
    left_head = left.head
    right_head = right.head

    #iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # if head node of left is none, we are past the tail
        # add the node from right to merged linked list

        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop cond to false
            right_head = right_head.next_node

        #if head node of right is node, same thing
        elif right_head is None:
            current.next_node = left.head
            left_head = left_head.next_node

        else:
            #not at either tail node
            # obtain node data to perform comparison
            left_data = left_head.data
            right_data = right_head.data
            # if data on left < right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left_head to next node
                left_head = left_head.next_node

                #if data is left is greater
            else:
                current.next_node = right_head
                right_head = right_head.next_node

            #move current to next node
            current = current.next_node

        #discard fake head and set first merged node as head

        head = merged.head.next_node
        merged.head = head

        return merged

l = Singlylinkedlist()
l.add(10)
l.add(44)
l.add(2)
l.add(15)
l.add(200)

print(l)

sorted_linked_list = merge_sort(l)

print(sorted_linked_list)

