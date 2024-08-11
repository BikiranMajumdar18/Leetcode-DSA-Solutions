# Searching an element in the linked list

class Solution:
    def searchKey(self, n, head, key):
        #Code here
        temp = head
        while temp != None:
            if temp == key:
                return 1
                break
            temp = temp.next
        return 0
