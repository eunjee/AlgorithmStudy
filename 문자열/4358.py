#생태학 22-02-27
from collections import defaultdict
import sys
input = sys.stdin.readline

trees= defaultdict(int)
n=0
while True:
    tree= input().strip()
    if not tree:
        break
    trees[tree]+=1
    n+=1

tree_names = list(trees.keys())
tree_names.sort()

for name in tree_names:
    print("%s %.4f" %(name,trees[name]/n*100))