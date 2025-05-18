# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from typing import Dict

#-------------------------------------------------------------------------
class TrieNode:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.end : bool = False
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
    def insert(self, word: str) -> None:
        current : TrieNode = self.root
        
        ''' here's the summary: 
        We loop the word and for each char, we check if it's not in the current dict level 
        (we start from root). 
          - If the char is not present at that dict level, we add the char, and then we create 
            a new TrieNode for the next char in the string.
          - If the char is present we don't do anything - no else condition
        We set the current node as the TrieNode from the current.dict[char]
        And then we loop to the next char. Eventually we will finish the loop and in that
        situation the last char has a TrieNode with an empty dict. We set this last node
        property 'end' to True
        So consider we have the word 'apple':
          |root| -> a -> p -> p -> l -> e -> { }
                                    ^-end 
        Now we insert the word 'app':
          |root| -> a -> p -> p -> l -> e -> { }
                                   ^-end      ^-end 
        
        No new char was created, but we had to place an 'end' flag at the next letter after
          the final 'p' to signal it was a word ending char
        '''
        #-----------------------------------
        for char in word:
            #-----------------------------------
            if char not in current.dict:
                current.dict[char] = TrieNode()
            #-----------------------------------
            current = current.dict[char]
        #-----------------------------------
        current.end = True  
    #-------------------------------------------------------------------------  
    #-------------------------------------------------------------------------
    def search(self, word: str, node : TrieNode = None) -> bool:
        
        # if node is not set, then this is the fist call, we must set it to root
        if node is None: 
            node : TrieNode = self.root
            
        # the word matched so far and we found the end of a word marker, so it's a match
        if len(word) == 0 and node.end == True: 
            return True
        
        # the word matched so far, but there's no end of a word marker, so this word is
        #  not included
        elif len(word) == 0:
            return False
        
        # char is not a match (note since this is a recursive function, this can be the fist or 
        #   the n-th char) - return false
        elif word[0] not in node.dict:
            return False
        
        # the char matched. But it's not the end of the word, so we continue to explore via
        #   recursive calls
        else:
            word_0 : str = word[0]
            substring : str = word[1:]
            trie_node : TrieNode = node.dict[word_0]
            
            return self.search(substring, trie_node)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def startsWith(self, word_prefix: str, node : TrieNode = None) -> bool:
        
        # if node is not set then it's the first call and we must set it to root
        if node is None:
            node : TrieNode = self.root
            
        ''' since this is a re ursive all, if the word_prefix has a len of 0, this
          means we explored until the end of the prefix and until now everything
          matched (what is unless the word_prefix was empty, in which case) we 
          still return true '''
        if len(word_prefix) == 0:
            return True
        
        word_prefix_0 : str = word_prefix[0]
        substring : str = word_prefix[1:]
        trie_node : TrieNode = node.dict[word_prefix[0]]        
        
        # if the word prefix is not preset at this level of the dict, then it's not a match
        #   return False
        if word_prefix_0 not in node.dict:
            return False
        
        # the char matched, continue to look
        else:
            return self.startsWith(substring, trie_node)
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