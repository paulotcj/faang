/**
 * This class represents a TrieNode.
 * A TrieNode has the following properties:
 * - end: A boolean indicating if the node is the end of a word.
 * - keys: An object containing the children of the node.
 */
class TrieNode {
  constructor() {
    this.end = false;
    this.keys = {};
  }
}

/**
 * This class represents a Trie. A Trie has the following properties:
 * - root: A TrieNode representing the root of the Trie.
 * The Trie class has the following methods:
 * - insert(word): Inserts the word into the Trie.
 * - search(word): Searches for the word in the Trie and returns true if the word is found, false otherwise
 */
class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  /**
   * This function inserts the word into the Trie. It starts at the root node and inserts each character of the word into the Trie.
   * Our solution's time complexity is O(n) where n is the length of the word. This is because we need to insert each character of the word into the Trie.
   * Our solution's space complexity is O(n) where n is the length of the word. This is because we store the word in the Trie.
   * @param {string} word
   * @param {TrieNode} node
   * @returns {void}
   */
  insert(word, node = this.root) {
    if (word.length === 0) {
      node.end = true;
      return;
    } else if (!node.keys[word[0]]) {
      node.keys[word[0]] = new TrieNode();
      this.insert(word.substring(1), node.keys[word[0]]);
    } else {
      this.insert(word.substring(1), node.keys[word[0]]);
    }
  }

  /**
   * This function searches for the word in the Trie. It starts at the root node and searches for each character of the word in the Trie. If the word is found, it returns true, otherwise it returns false.
   * Our solution's time complexity is O(n) where n is the length of the word. This is because we need to search for each character of the word in the Trie.
   * Our solution's space complexity is O(1) because we are not using any additional space.
   * @param {string} word
   * @param {TrieNode} node
   * @returns {boolean}
   */
  search(word, node = this.root) {
    if (word.length === 0 && node.end) {
      return true;
    } else if (word.length === 0) {
      return false;
    } else if (!node.keys[word[0]]) {
      return false;
    } else {
      return this.search(word.substring(1), node.keys[word[0]]);
    }
  }
}

const trie = new Trie();
trie.insert('apple');
console.log(JSON.stringify(trie, null, 2)); // Pretty-print JSON
console.dir(trie, { depth: null });
console.log(trie.search('apple')); // true
console.log(trie.search('app')); // false

trie.insert('app');
console.log(JSON.stringify(trie, null, 2)); // Pretty-print JSON
console.dir(trie, { depth: null });
console.log(trie.search('app')); // true
console.log(trie);