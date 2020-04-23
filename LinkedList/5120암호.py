class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


def addLast(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1

def printList(lst):
    if lst.head is None:return
    # cur = lst.head
    # for _ in range(lst.size):
    #     print(cur.data, end=' ')
    #     cur = cur.next
    # print()
    print("#{}".format(t), end=' ')
    cur = lst.head.prev
    cnt = 0
    if lst.size>10:
        cnt = 10
    else:
        cnt = lst.size
    for _ in range(cnt):
        print(cur.data, end=' ')
        cur = cur.prev
    print()


for t in range(1,int(input())+1):
    myl = LinkedList()
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    for val in arr:
        addLast(myl, Node(val))
    cur = myl.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next
        prev = cur.prev
        new = Node(prev.data+cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new
        myl.size += 1
    printList(myl)
