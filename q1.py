# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

class TrieNode(object):
    def __init__(self,key):
        self.key = key
        self.children =[]
    def add(self,word):
        node = self
        for i in word:
            is_in = False
            for child in node.children:
                if i == child.key:
                    node = child
                    is_in = True
                    break
            if not is_in:
                new_node = TrieNode(i)
                node.children.append(new_node)
                node = new_node

    def query(self, word):
        node = self
        a = ""
        for i in word:
            is_set = False
            for child in node.children:
                if int(i)^int(child.key):
                    a += "1"
                    node = child
                    is_set = True
                    break
            if not is_set:
                a += "0"
                node = node.children[0]
                    
        return a
# modify this function, and create other functions below as you wish
def question01(tins):
  ans = 0
    for i in tins:
        num = str(bin(i))[2:].rjust(16,"0")
        t.add(num)
        q = t.query(num)
        if q > ans:
            ans = q
    
  answer = int(ans,2)
  return answer
