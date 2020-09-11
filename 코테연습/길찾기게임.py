# import sys
#
# sys.setrecursionlimit(10 ** 6)  # 이걸 안해주면 횟수제한에 걸려서 재귀가 막혀버림
#
# preorder = list()
# postorder = list()
#
#
# def solution(nodeinfo):
#     levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)  # 어떤 레벨이 있는지 파악
#     nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)),
#                    key=lambda x: (-x[1][1], x[1][0]))  # 노드좌표와 인덱스를 서로 연결 해 줌
#     order(nodes, levels, 0)
#     return [preorder, postorder]
#
#
# def order(nodeList, levels, curLevel):
#     n = nodeList[:]
#     print(n)
#     cur = n.pop(0)
#     preorder.append(cur[0])
#     if n:
#         for i in range(len(n)):
#             if n[i][1][1] == levels[curLevel + 1]:
#                 if n[i][1][0] < cur[1][0]:
#                     order([x for x in nodeList if x[1][0] < cur[1][0]], levels, curLevel + 1)
#                 else:
#                     order([x for x in nodeList if x[1][0] > cur[1][0]], levels, curLevel + 1)
#     postorder.append(cur[0])
#
# solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])




class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)

        else:
            if data[0] < node.data[0] and data[1]<node.data[1]:
                node.left = self._insert_value(node.left, data)
            elif data[0] > node.data[0] and data[1]<node.data[1]:
                node.right = self._insert_value(node.right, data)
        return node

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)

        _pre_order_traversal(self.root)


bst = BinarySearchTree()
for n in sorted([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]], key=lambda x: - x[1]):
    bst.insert(n)

bst.pre_order_traversal()