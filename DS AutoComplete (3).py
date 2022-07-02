#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

_end = '_end_'

class TrieTree:


    def __init__(self):
        self.root = dict()

    def insert(self, words):
        if not self.check_input(words):
            return
        words = re.findall("[a-zA-Z]+", words.lower())
        for word in words:
            current_dict = self.root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end

    def search(self, word):
        if not self.check_input(word):
            return
        searchTrie = self.root
        for letter in word.lower():
            if searchTrie.get(letter, None):
                searchTrie = searchTrie[letter]
            else:
                print(word + " NOT FOUND!")
                return

        if _end in searchTrie:
            print(word + " FOUND!")
        else:
            print(word + " NOT FOUND!")

    def delete(self, words):
        if not self.check_input(words):
            return
        for word in words.split(' '):
            trie = self.root
            lasted = True
            for letter in word:
                if trie.get(letter, None):
                    trie = trie[letter]

                else:
                    lasted = False
                    break
            if _end in trie and lasted:
                del trie[_end]

                print(word + ' DELETED!')
            else:
                print(word + ' NOT FOUND!')

    def _walk_trie(self, trie, partial_word, word_list):
        if trie:
            for char in trie:
                word_new = partial_word + char
                if type(trie) == dict:
                    if _end in trie[char] and _end not in word_new:
                        word_list.append(word_new)
                    self._walk_trie(trie[char], word_new, word_list)
        return word_list

    def auto_complete(self, partial_word):
        if not self.check_input(partial_word):
            return
        trie = self.root
        partial_word = partial_word.lower()
        word_list = []
        #find the self.root for last char of word
        for char in partial_word:
            if char in trie:
                trie = trie[char]
            else:
                print('NOTHING FOUND TO COMPLETE!')
                return
        if _end in trie:
            word_list.append(partial_word)

        # word_list will be created in this method for suggestions that start with partial_word
        mylist = self._walk_trie(trie, partial_word, word_list)
        if mylist:
            print(*mylist, sep='\n')
        else:
            print('NOTHING FOUND TO COMPLETE!')

    def check_input(self, word):
        if not re.findall("[a-zA-Z]+", word):
            print('THERE IS NO VALID INPUT')
            return False
        return True


trie = TrieTree()
trie.insert('h hi hilarious')
trie.search('hello')
trie.delete('h hi')

