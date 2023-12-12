# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:41:01 2023

@author: Leo Zhang
"""

path = 'inputPartial_20221220.txt'

def part1(path, ls_idx): 
    ls = []
    with open(path, 'r') as f:
        for line in f: 
            ls.append(int(line[:-1]))
    # print(ls)
    
    class Node: 
        def __init__(self, val, left=None, right=None): 
            self.val = val
            self.left = left
            self.right = right
    
    ls_nodes = []
    node0 = None
    n = len(ls)
    
    for i in range(n): 
        val = ls[i]
        node = Node(val)
        if i > 0: 
            node.left = ls_nodes[i - 1]
            ls_nodes[i - 1].right = node
        if i == n - 1: 
            node.right = ls_nodes[0]
        ls_nodes.append(node)
        if val == 0: 
            node0 = node
    ls_nodes[0].left = ls_nodes[-1]
    
    for node in ls_nodes: 
        rnode = node.right
        lnode = node.left
    
        val = node.val % (n - 1)
        if val > (n - 1) // 2: 
            val -= n - 1
        if val == 0: 
            continue
        elif val > 0: 
            rnode.left, lnode.right = lnode, rnode
            tmp = rnode
            cnt = 1
            while cnt < val: 
                tmp = tmp.right
                cnt += 1
            nodel = tmp
            noder = tmp.right
            nodel.right = node
            node.left= nodel
            noder.left = node
            node.right = noder
        else: 
            rnode.left, lnode.right = lnode, rnode
            tmp = lnode
            cnt = 1
            while cnt < -val:
                tmp = tmp.left
                cnt += 1
            noder = tmp
            nodel = tmp.left
            nodel.right = node
            node.left= nodel
            noder.left = node
            node.right = noder
            
        # result = []
        # result1 = []
        # tmp = node0
        # cnt = 0
        # while cnt < n: 
        #     result.append(tmp.val)
        #     result1.append([tmp.left.val, tmp.val, tmp.right.val])
        #     tmp = tmp.right
        #     cnt += 1
        # print(val, node.val, result, result1)
        # print()
    
    result = []
    # tmp = node0
    # cnt = 0
    # while cnt < n: 
    #     print(tmp.val)
    #     tmp = tmp.right
    #     cnt += 1
    
    for idx in ls_idx: 
        idx %= n
        # print(idx)
        tmp = node0
        cnt = 0
        while cnt < idx: 
            tmp = tmp.right
            cnt += 1
        result.append(tmp.val)
    
    return result

path1 = 'inputPartial_20221220.txt'
path2 = 'inputFull_20221220.txt'
ls_idx = [1000, 2000, 3000]

print(sum(part1(path1, ls_idx)))
print(sum(part1(path2, ls_idx)))

            
    
    

    