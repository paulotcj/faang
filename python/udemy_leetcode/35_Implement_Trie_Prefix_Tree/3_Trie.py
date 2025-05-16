# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from typing import Tuple

#-------------------------------------------------------------------------
class TrieNode: 
    #-------------------------------------------------------------------------
    def __init__(self):
        self.children : dict[str, TrieNode] = {}
        self.is_end_of_word = False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Trie:
    #-------------------------------------------------------------------------
    def __init__(self):
        # Root node does not hold any character
        self.root : TrieNode = TrieNode()
    #------------------------------------------------------------------------- 
    #-------------------------------------------------------------------------
    def insert(self, word : str) -> None:
        node : TrieNode = self.root
        
        #-----------------------------------
        for char in word:
            #-----------------------------------
            if char not in node.children:
                node.children[char] = TrieNode()
            #-----------------------------------
            
            node = node.children[char]
        #-----------------------------------
        
        # after all the letters of the word we end up with node where its children
        #  is an empty dict - and we also need to mark it as the end of the word
        node.is_end_of_word = True    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def search(self, word : str) -> bool : 
        
        node : TrieNode | None = self._find_node(prefix_or_word = word)
        return_val : bool = node.is_end_of_word if node is not None else False
        
        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def startsWith(self, prefix : str) -> bool:
        return_val : bool = self._find_node(prefix_or_word = prefix) is not None
        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _find_node(self, prefix_or_word : str) -> TrieNode | None :
        node : TrieNode = self.root
        
        #-----------------------------------
        for char in prefix_or_word:
            if char not in node.children: return None
            
            node = node.children[char]
        #-----------------------------------
        
        return node
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

obj = Trie()

obj.insert("apple")
result = obj.search("apple")
expected = True
print('\n\n')
print(f'result: {result} - expected: {expected} - Is the result what was expected?: {result==expected}')
print('-------------------')

result = obj.search("app")
expected = False
print('\n\n')
print(f'result: {result} - expected: {expected} - Is the result what was expected?: {result==expected}')
print('-------------------')

result = obj.startsWith("app")
expected = True
obj.insert("app")
result = obj.search("app")
print('\n\n')
print(f'result: {result} - expected: {expected} - Is the result what was expected?: {result==expected}')
print('-------------------')