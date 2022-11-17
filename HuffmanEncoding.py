from collections import Counter
import heapq
class Node:
    def _init_(self,ch,freq,left,right):
        self.ch=ch
        self.freq=freq
        self.left=left
        self.right=right

    def _lt_(self,other):
        return self.freq<other.freq
        
def buildTree(text):
    counter=Counter(text)
    pq=[]
    for k in counter.keys():
        node=Node(k,counter[k],None,None)
        pq.append(node)

    heapq.heapify(pq)
    while(len(pq)>1):
        left=heapq.heappop(pq)
        right=heapq.heappop(pq)
        parent=Node(None,left.freq+right.freq,left,right)
        heapq.heappush(pq,parent)

    return pq[0]

def build_map(root):
    def dfs(root,code,ans_map):
        if root.ch is not None:
            ans_map[root.ch]="".join(code)
        else:
            code.append("0")
            dfs(root.left,code,ans_map)
            code.pop()

            code.append("1")
            dfs(root.right,code,ans_map)
            code.pop()
    ans_map={}
    dfs(root,[],ans_map)
    return ans_map


def encoded(text):
    root=buildTree(text)
    encoded_map=build_map(root)

    encodedTxt=""
    for ch in text:
        encodedTxt+=encoded_map[ch]

    return encodedTxt

def decoded(encoded,root):
    decoded=[]
    node=root
    for bit in encoded:
        if bit=="0":
            node=node.left
        else:
            node=node.right
        if node.ch is not None:
            decoded.append(node.ch)
            node=root

    return "".join(decoded)
            
s=input()
encodedStr=encoded(s)
root=buildTree(s)

decodedval=decoded(encodedStr,root)
print(encodedStr)
print(decodedval)