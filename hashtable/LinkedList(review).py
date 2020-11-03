# Initialized LinkedList Node
# To handle collision in HashTables via chaining
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Prints value of LinkedList
    # walks thru LinkedList and prints value of nodes
    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f' {str(curr.value)} -->'
            curr = curr.next
        return currStr

    def find(self, value):
        # return Node with value
        # runtime: 0(n) LINEAR WHERE N = number of nodes
        current = self.head
        while current != None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        # deletes Node with given Value
        # runtime: O(n) where N = number of nodes
        current = self.head

        # if we want to delete is the Head
        if current.value == value:
            self.head = current.next
            current.next = None
            return current

        prev = None
        while current != None:
            if current.value == value:
                prev.next = current.next
                current.next = None
                return current
            else:
                prev = current
                current = current.next

        return None

    def insert_at_head(self, node):
        # runtime: 0(1) constant time
        node.next = self.head
        self.head = node

    def insert_at_head_or_overwite(self, node):
        existingNode = self.find(node.value)  # 0(N + 1)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)


a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList()
ll.insert_at_head(c)
ll.insert_at_head(b)
ll.insert_at_head(a)
print(ll)
