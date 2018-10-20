"""
16. 给一个国王家的family tree （n-ary tree），王位继承是先传国王最年长的儿子，
假如最年长儿子死了，就传给死儿子最年长的儿子。。。如果这些人都不存在，再考虑国王次年长的儿子，
以此类推。要求设计这样一棵树，死掉的人不要求删除，实现birth（）
和输出王位继承顺序的method（死掉的人不在继承顺序结果里）。（及其变种）
https://hihocoder.com/problemset/problem/1716

描述
H国的国王有很多王子，这些王子各自也都有很多王孙，王孙又各自有很多后代…… 总之，H国王族的族谱形成了一棵以国王为根的树形结构。

根据H国的法律，王族的继承顺位这样规定的：

假设A和B是两位王族

1. 如果其中一位是另一位的直系父亲、祖先，则辈份高的王族继承顺位更高

2. 否则，假设C是A和B的最近公共祖先。显然A和B一定是C的两位不同子嗣的后代。其中C较年长的子嗣的后代的继承顺位更高

按时间顺序给出所有国王后代的出生和死亡记录，请你计算所有还活着的后代的继承顺位。

输入
第一行包含一个整数N和一个只包含大写字母和数字的字符串，分别代表记录的条数和国王的名字。

以下N行每行包含一条记录：

birth name1 name2 代表name1的儿子name2出生

death name 代表name死亡

1 <= N <= 10000

名字长度不超过20，并且没有重名的王族。

输出
按继承顺位从高到低输出每位王族的名字。(不包括国王)

每个名字一行。

样例输入
4 KING
birth KING ALI
birth KING BOB
birth ALI CARRO
death ALI
样例输出
CARRO
BOB
"""

"""
为了方便起见 我们assume input是个list of string
[["birth", "KING", "ALI"],
 ["birth", "KING", "BOB"],
 ["birth", "ALI", "CARRO"]
 ["death", "ALI"]]
"""


class Prince:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.is_dead = False


class FamilyTree:
    def __init__(self):
        self.king = Prince("KING")
        self.name2node = {}
        self.name2node["KING"] = self.king

    def birth(self, father, son):
        if father not in self.name2node:
            raise InputError("Father not exist")
        if son in self.name2node:
            raise InputError("Son already exist")
        fnode = self.name2node[father]
        snode = Prince(son)
        self.name2node[son] = snode
        fnode.children.append(snode)

    def death(self, person):
        if person not in self.name2node:
            raise InputError("Person not exist")
        self.name2node[person].is_dead = True

    def king_sequence(self):
        result = []
        self.dfs(self.king, result)
        print(result)

    def dfs(self, node, result):
        if not node:
            return
        if not node.is_dead:
            result.append(node.name)

        for child in node.children:
            self.dfs(child, result)


"""
为了方便起见 我们assume input是个list of string
[["birth", "KING", "ALI"],
 ["birth", "KING", "BOB"],
 ["birth", "ALI", "CARRO"]
 ["death", "ALI"]]
"""
family = FamilyTree()
family.birth("KING", "ALI")
family.birth("KING", "BOB")
family.birth("ALI", "CARRO")
family.death("ALI")
family.king_sequence()
