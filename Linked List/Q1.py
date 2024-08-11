# Array to Linked List

class Solution:
    def constructLL(self, arr):
        # code here
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return head
