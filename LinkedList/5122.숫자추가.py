# for t in range(1,int(input())+1):
#     N, M, L = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(M):
#         idx, n = map(int,input().split())
#         arr.insert(idx,n)
#     print("#{} {}".format(t,arr[L]))

class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n

class LinkedList:
    size = 0
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def printList(lst):
    if lst.head is None:return #빈 리스트 일 경우

    cur = lst.head
    print(lst.size, '[', end=' ')

    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next

    print(']')

def insertLast(lst,new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def deletLast(lst):
    if lst.head is None:return

    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -= 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new

    lst.size += 1
def insertAt(lst, idx, new):
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    elif idx>= lst.size:
        insertLast(lst,new)# 마지막 추가하는 경우 idx >= lst.size
    else:# 중간에 추가하는 경우
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

def deleteAt(lst, idx):
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    elif idx>=lst.size:
        deletLast(lst)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1

def search(lst, idx):
    if lst.head is None or lst.size<idx:
        print(-1)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre=cur
            cur = cur.next
        print("#{} {}".format(t,cur.data))

def deleteFirst(lst):
    if lst.head is None:return
    # 노드가 1개일 경우 주의한다.
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None
    lst.size -=1

for t in range(1,int(input())+1):
    mylist = LinkedList()
    N, M, L = map(int, input().split())
    for i in list(map(int, input().split())):
        insertLast(mylist,Node(i))
    for _ in range(M):
        idx, n = map(int,input().split())
        insertAt(mylist,idx,Node(n))
    search(mylist,L)