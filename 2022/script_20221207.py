# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 00:18:04 2022

@author: Leo Zhang
"""

def part1(path, limit):
    
    class Folder:
        def __init__(self, name=None, type='folder', children=None, size=0, parent=None):
            self.parent = parent
            self.name = name
            self.type = type
            if children is None: 
                self.children = {}
            self.size = size
            
        
    root = Folder('/')
    curr_folder = None
    tmp_ls = []
    xx = 1
    with open(path, 'r') as f:
        for line in f: 
            if line[0] == '$':
                if line[:4] == '$ cd': 
    
                    if curr_folder is not None and not curr_folder.children: 
                        curr_folder.children = dic
                    file_name = line[5:-1]                    
                    if file_name != '..': 
                        if file_name == '/': 
                            curr_folder = root
                        else: 
                            if file_name in curr_folder.children: 
                                tmp = curr_folder.children[file_name]
                            else: 
                                tmp = Folder(file_name)    
                            tmp.parent = curr_folder
                            curr_folder = tmp
                            if file_name == 'qcznqph': 
                                xx = curr_folder
                    else: 
                        curr_folder = curr_folder.parent
                elif line[:4] == '$ ls': 
                    dic = {}
            elif line[0] == '\n':
                if curr_folder is not None and curr_folder.children == []: 
                    curr_folder.children = tmp_ls
            elif line[0] == 'd': 
                file_name = line[4:-1]
                tmp = Folder(file_name, parent=curr_folder)
                dic[file_name] = tmp
            else: 
                size, name = line[:-1].split(' ')
                size = int(size)
                new_file = Folder(name, type='file', size=size, parent=curr_folder)
                dic[name] = new_file
                
    result = [0]
    def calc_size(node):
        if node is None:
            return 0
        if node.type == 'file': 
            return node.size
        else: 
            if node.children is None: 
                return 0
            else: 
                res = 0
                for child in node.children.values(): 
                    res += calc_size(child)
                node.size = res
                if res <= limit: 
                    result[0] += res
                return res
    calc_size(root)
    return result[0]

def part2(path, target):
    
    class Folder:
        def __init__(self, name=None, type='folder', children=None, size=0, parent=None):
            self.parent = parent
            self.name = name
            self.type = type
            if children is None: 
                self.children = {}
            self.size = size
            
        
    root = Folder('/')
    curr_folder = None
    tmp_ls = []
    xx = 1
    with open(path, 'r') as f:
        for line in f: 
            if line[0] == '$':
                if line[:4] == '$ cd': 
    
                    if curr_folder is not None and not curr_folder.children: 
                        curr_folder.children = dic
                    file_name = line[5:-1]                    
                    if file_name != '..': 
                        if file_name == '/': 
                            curr_folder = root
                        else: 
                            if file_name in curr_folder.children: 
                                tmp = curr_folder.children[file_name]
                            else: 
                                tmp = Folder(file_name)    
                            tmp.parent = curr_folder
                            curr_folder = tmp
                            if file_name == 'qcznqph': 
                                xx = curr_folder
                    else: 
                        curr_folder = curr_folder.parent
                elif line[:4] == '$ ls': 
                    dic = {}
            elif line[0] == 'd': 
                file_name = line[4:-1]
                tmp = Folder(file_name, parent=curr_folder)
                dic[file_name] = tmp
            else: 
                size, name = line[:-1].split(' ')
                size = int(size)
                new_file = Folder(name, type='file', size=size, parent=curr_folder)
                dic[name] = new_file
        if curr_folder is not None and not curr_folder.children: 
            curr_folder.children = dic
                
    result = []
    def calc_size(node):
        if node is None:
            return 0
        if node.type == 'file': 
            return node.size
        else: 
            if node.children is None: 
                return 0
            else: 
                res = 0
                for child in node.children.values(): 
                    res += calc_size(child)
                node.size = res
                result.append(res)
                return res
    total = calc_size(root)
    result = sorted(result)
    target = total - target
    def bs(val, ls): 
        def bs_(l, r): 
            if val <= ls[l]: 
                return l
            if val > ls[r]: 
                return r + 1
            if r - l == 1: 
                return r
            mid = (l + r) // 2
            if val < ls[mid]: 
                return bs_(l, mid)
            elif val == ls[mid]: 
                return mid
            else: 
                return bs_(mid, r)
        return bs_(0, len(ls) - 1)
    idx = bs(target, result)
    print(target, result[idx])
    print(idx, result[idx - 1:idx + 2])
    
    

path1 = 'inputPartial_20221207.txt'
path2 = 'inputFull_20221207.txt'
limit = 100000
target = 70000000 - 30000000

# print(part1(path1, limit))
# print(part1(path2, limit))
a = part2(path1, target)
b = part2(path2, target)

            

                    
                
            