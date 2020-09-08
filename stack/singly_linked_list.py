class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next # The next node in the list

class LinkedList:
    def __init__(self):
        self.head = None # point to the first node in the list
        self.tail = None  # point to the last node in the list
        self.length = 0


    def __str__(self):
        output = " "
        current = self.head
        while current is not None:
            output += f'{current.value} -> '
            current = current.next

        return output

    def add_to_head(self, value):
        # Check if there's a head
        # If there is no head (empty list)
        if self.head is None:
        # Create a new node
            new_head = Node(value)
        # Set self.head and self.head to the new node
            self.head = new_head
            self.head = new_head
        else:
        # Create a new node with the value we want to add
            new_head = Node(value)
        # set New Head.next to the old head node
            old_head = self.head
            new_head.next = old_head
        # Set self.head to the new node
            self.head = new_head
        self.length += 1    

    def add_to_tail(self, value):
        # Check if there's a tail
        # If there is no tail (empty list)
        if not self.tail:
        # Create a new node
            new_tail = Node(value, None)
        # Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        else:
        # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
        # set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
        # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        # If there is no head
        if not self.head:
            return None  

        # If List has one element 
        if self.head == self.tail: #or if self.length == 1
        # Set self.head to current_head.next 
            current_head = self.head
            self.head = None
        # Set self.tail to None
            self.tail = None
        # Decrement length by 1
            self.length = self.length -1
            return current_head.value
        # If the head exists
        else:
        # Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
        # return current_head.value
            self.length = self.length -1
            return current_head.value

    def remove_tail(self):
        # If there is no head
        if not self.tail:
            return None 

        # If List has 1 element
        if self.head == self.tail:
            # Save the current_tail.value
            current_tail = self.tail
            # Set self.tail to None
            self.tail = None
            #  Set self.head to None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        else:
        # Start at head and iterate to the next-to-last node
            current_node = self.head
        # Stop when current_node.next == self.tail
            while current_node.next == self.tail:
            # once we exit the while loop, current_node is pointing to the node
        #Save the current_tail value
                tail_value = current_node.next.value
        # Set self.tail to current_node
                self.tail = current_node
        # Set current_node.next to None
                current_node.next = None
                self.length = self.length - 1
                return tail_value 