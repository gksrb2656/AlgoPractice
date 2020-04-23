class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data>arr[0]:break
            cur = cur.next
            # search(lst,idx)
        if cur is None: #뒤에
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None: #앞에
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)

def printList(lst):
    if lst.head is None:return
    # cur = lst.head
    # while cur is not None:
    #     print(cur.data, end=' ')
    #     cur = cur.next
    # print()
    cur = lst.tail
    cnt = 0
    print("#{}".format(t), end=' ')
    while cur is not None and cnt<10:
        print(cur.data, end=' ')
        cur = cur.prev
        cnt += 1
    print()

def search(lst,idx):
    if idx == 0:
        return lst.head
    elif idx==lst.size:
        return lst.tail
    elif idx<lst.size//2:
        pre, cur = None, lst.head
        while cur.next is not None:
            pre = cur
            cur = cur.next
    else:
        pre, cur = None, lst.tail
        while cur.prev is not None:
            pre = cur
            cur = cur.prev

for t in range(1,int(input())+1):
    myl = LinkedList()
    N, M = map(int, input().split())
    for _ in range(M):
        arr = list(map(int,input().split()))
        addList(myl,arr)
    printList(myl)

# myl = LinkedList()
#
# arr = [1,3,5,7,9]
# addList(myl, arr)
# printList(myl)
#
# addList(myl, [0,1,2])
# printList(myl)