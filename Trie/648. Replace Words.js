/*
 * APPROACH :
 * ➀ Insert all the words of the array dictionary into a "Trie".
 * ➁ Extract each word from sentence & invoke "getReplacedWord" method on each sentence word :
 *   1. Create an empty string ans.
 *   1. If the word is not present in the trie, return empty ans directly
 *   2. If a prefix of the word exists & isEnd of the last letter of the prefix is true, then that's the root & the remaining is the successor. So add the 'root' part to the ans, return current ans
 *   3. After traversing the whole word, we still not return ans, it means the word is on the trie, but it is not reach the end of current branch, so return empty ans. 例如 trie 中记录的单词是 "bat", 而当前的 word 是 "ba", 此时也要返回 ""
 * ➂ For each returned ans of the word returned by "getReplacedWord" method:
 *   1. If ans == "", we will add old word to the result sentence
 *   2. if ans !== "", which means we get the replacedWord in the ans variable, so we use the new replacedWord in the result sentence
 */

class TrieNode {
    constructor() {
        this.children = {};
        this.isEnd = false;
        this.word = "";
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    addWord(word) {
        let curNode = this.root;
        for (let char of word) {
            if (!curNode.children.hasOwnProperty(char))
                curNode.children[char] = new TrieNode();
            curNode = curNode.children[char];
        }

        curNode.isEnd = true;
        curNode.word = word;
    }

    getReplacedWord(word) {
        let ans = "";
        let curNode = this.root;
        for (let char of word) {
            if (!curNode.children.hasOwnProperty(char)) return ans;
            curNode = curNode.children[char];
            if (curNode.isEnd) {
                ans = curNode.word;
                return ans;
            }
        }

        return ans;
    }
}

/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function (dictionary, sentence) {
    let trie = new Trie();
    for (let word of dictionary) {
        trie.addWord(word);
    }
    // console.log(JSON.stringify(trie.root, null, 2));
    let sentenceArr = sentence.split(" ");

    for (let i = 0; i < sentenceArr.length; i++) {
        let curWord = sentenceArr[i];
        let replacedWord = trie.getReplacedWord(curWord);
        if (replacedWord !== "") sentenceArr[i] = replacedWord;
    }

    return sentenceArr.join("");
};

replaceWords(
    ["cat", "bat", "rat"],
    "the cattle was rattled by the battery r a"
);
