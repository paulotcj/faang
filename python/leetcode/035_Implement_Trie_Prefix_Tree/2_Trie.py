# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from typing import Dict

#-------------------------------------------------------------------------
class TrieNode:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.bool_end : bool = False
        self.dict : Dict[str, TrieNode] = {} # must start with a dummy dict
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Trie:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.root = TrieNode()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def insert(self, word : str) -> None:
        current : TrieNode = self.root
        
        #-----------------------------------
        for char in word:
            #-----------------------------------
            if char not in current.dict:
                current.dict[char] = TrieNode()
            #-----------------------------------
            current = current.dict[char]
        #-----------------------------------
        current.bool_end = True
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def search(self, word : str, node : TrieNode = None) -> bool :
        
        # if node is not set, then this is the fist call, we must set it to root
        if node is None:
            node : TrieNode = self.root
            
        # the word matched so far (and it's the end of the word) and we found the end 
        #   of a word marker, so it's a match (return True)
        if len(word) == 0 and node.bool_end == True: return True
        
        # the word matched so far, but it's the end of the word and no end of word marker
        #   was found
        elif len(word) == 0: return False
        
        # char is not a match (note since this is a recursive function, this can be the fist or 
        #   the n-th char) - return false
        elif word[0] not in node.dict: return False
        
        # the char matched. But it's not the end of the word, so we continue to explore via
        #   recursive calls
        else:
            word_0 : str = word[0]
            substring : str = word[1:]
            trie_node : TrieNode = node.dict[word_0]
            
            return self.search(word = substring , node = trie_node)
            
        # and we are done - this condition should not be reached - nothing to return
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def startsWith(self, word_prefix : str, node : TrieNode = None) -> bool:
        # if node is not set then it's the first call and we must set it to root
        if node is None:
            node : TrieNode = self.root
            
        ''' since this is a re ursive all, if the word_prefix has a len of 0, this
          means we explored until the end of the prefix and until now everything
          matched (what is unless the word_prefix was empty, in which case) we 
          still return true '''
        if len(word_prefix) == 0 : return True
        
        
        # if the word prefix is not preset at this level of the dict, then it's not a match
        #   return False
        word_prefix_0 : str = word_prefix[0]
        substring : str = word_prefix[1:]
        trie_node : TrieNode = node.dict[word_prefix_0]
        
        if word_prefix_0 not in node.dict: return False
        
        # else condition - it's a match and not the end of the word, we must continue looking
        return self.startsWith( word_prefix = substring, node = trie_node)        
        
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