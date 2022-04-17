# Comment it before submitting
# class DoubleConnectedNode:  
#    def __init__(self, value, next=None, prev=None):  
#        self.value = value  
#        self.next = next  
#        self.prev = prev

def solution(node):
    while node is not None:
        if node.value == 'node0':
            node.prev, node.next = node.next, None
            node = node.prev
        else:
            next_node = node.prev 
            node.prev = node.next
            node.next = next_node
            if node.prev == None:
                break
            node = node.prev
    return node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)

    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1
