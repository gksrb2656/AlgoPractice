# class Node:
#     def __init__(self, d=0, n=None):
#         self.data = d
#         self.next = n
#
# class LinkedList:
#     size = 0
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#
# def printList(lst):
#     if lst.head is None:return #빈 리스트 일 경우
#
#     cur = lst.head
#     print(lst.size, '[', end=' ')
#
#     while cur is not None:
#         print(cur.data, end=' ')
#         cur = cur.next
#
#     print(']')
#
# def insertLast(lst,new):
#     if lst.head is None:
#         lst.head = lst.tail = new
#     else:
#         lst.tail.next = new
#         lst.tail = new
#     lst.size += 1
#
# def deletLast(lst):
#     if lst.head is None:return
#
#     pre, cur = None, lst.head
#     while cur.next is not None:
#         pre = cur
#         cur = cur.next
#     if pre is None:
#         lst.head = lst.tail = None
#     else:
#         pre.next = None
#         lst.tail = pre
#     lst.size -= 1
#
# def insertFirst(lst, new):
#     if lst.head is None:
#         lst.head = lst.tail = new
#     else:
#         new.next = lst.head
#         lst.head = new
#
#     lst.size += 1
# def insertAt(lst, idx, new):
#     # 빈리스트일 경우, idx == 0
#     if lst.head is None or idx == 0:
#         insertFirst(lst, new)
#     elif idx>= lst.size:
#         insertLast(lst,new)# 마지막 추가하는 경우 idx >= lst.size
#     else:# 중간에 추가하는 경우
#         pre, cur = None, lst.head
#         for _ in range(idx):
#             pre = cur
#             cur = cur.next
#         new.next = cur
#         pre.next = new
#         lst.size += 1
#
# def deleteAt(lst, idx):
#     if lst.head is None or idx == 0:
#         deleteFirst(lst)
#     elif idx>=lst.size:
#         deletLast(lst)
#     else:
#         pre, cur = None, lst.head
#         for _ in range(idx):
#             pre = cur
#             cur = cur.next
#         pre.next = cur.next
#         lst.size -= 1
#
# def search(lst, idx):
#     if lst.head is None or lst.size<idx or lst.tail is None:
#         print("#{} {}".format(t,-1))
#     else:
#         pre, cur = None, lst.head
#         for _ in range(idx):
#             pre=cur
#             cur = cur.next
#         print("#{} {}".format(t,cur.data))
#
# def change(lst,idx,new):
#     if lst.head == None or lst.tail==None:return
#     if idx>lst.size:return
#     if idx == 0:
#         new.next = lst.head.next
#         lst.head = new
#     elif idx==lst.size:
#         lst.tail = new
#     else:
#         pre, cur = None, lst.head
#         for _ in range(idx):
#             pre=cur
#             cur = cur.next
#         new.next = cur.next
#         cur = new
#         pre.next=cur
#
#
# def deleteFirst(lst):
#     if lst.head is None:return
#     # 노드가 1개일 경우 주의한다.
#     lst.head = lst.head.next
#     if lst.head is None:
#         lst.tail = None
#     lst.size -=1
#
# for t in range(1,int(input())+1):
#     mylist = LinkedList()
#     N, M, L = map(int, input().split())
#     for i in map(int, input().split()):
#         insertLast(mylist,Node(i))
#     for _ in range(M):
#         command = input().split()
#         if len(command)<3:
#             f, idx = command
#             deleteAt(mylist, int(idx))
#         else:
#             f, idx, n = command
#             if f=='I':
#                 insertAt(mylist,int(idx),Node(int(n)))
#             elif f == 'C':
#                 change(mylist, int(idx), Node(int(n)))
#         printList(mylist)
#     search(mylist,L)
#

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def L_append(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        self.size += 1

    def L_insert(self, idx, data):
        if idx >= self.size:
            self.L_append(data)
            return
        new = Node(data)
        if idx == 0:
            new.next = self.head.next
            self.head = new
            return
        node = self.L_search(idx)
        node_next = node.next
        node.next = new
        new.next = node_next
        self.size += 1

    def L_delete(self,idx):
        if self.head is None: return
        if idx ==0:
            self.head=self.head.next
            return
        node = self.L_search(idx-1)
        if idx<self.size:
            node.next = node.next.next
        else:
            node.next=None
        self.size -= 1

    def L_change(self,idx,data):
        if idx > self.size or self.head is None: return
        node = self.L_search(idx)
        node.data = data

    def L_search(self,idx):
        node=self.head
        cnt=0
        if self.size < idx:
            return -1
        while cnt!=idx:
            node=node.next
            cnt+=1
        return node

    # def L_print(self):
    #     if self.head is None:
    #         return
    #     else:
    #         res = self.head
    #         while res:
    #             print(res.data, end=" ")
    #             res = res.next
    #         print()

for tc in range(1, int(input()) + 1):
    n, m, l = map(int, input().split())
    num = list(map(int, input().split()))
    li=Linkedlist()
    for i in range(n):
        li.L_append(num[i])

    for i in range(m):
        rule = list(map(str, input().split()))
        if rule[0] == 'I':
            li.L_insert(int(rule[1]), int(rule[2]))
        elif rule[0] == 'D':
            li.L_delete(int(rule[1]))
        elif rule[0] == 'C':
            li.L_change(int(rule[1]), int(rule[2]))

    if li.size < l:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc,(li.L_search(l)).data))