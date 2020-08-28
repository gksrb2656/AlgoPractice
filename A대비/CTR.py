# import os
#
# read_u = []
# click_u = []
# n = input()
# for i in range(int(n)):
#     row = input()
#     data = row.split(',')
#

dir = []
tos = ['T','O','S','S']
for i in range(4):
    for j in range(4):
        
n = int(input())
data = ['']*n
for d in range(n):
    id,act = input().split(',')
    id = int(id)
    if data[id-1] == 'X':
        continue
    if act == 'X':
        data[id-1]='X'
    if act in 'TOSZ':
        data[id-1] += act

for d in range(n):


