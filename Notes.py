##################################################
# leetcode 599. Minimum Index Sum of Two Lists
##################################################
# Difficulty: Easy
# Given two lists of strings list1 and list2, return the common elements between the lists. If there are no common elements return an empty list.
# You may assume that each list's length is at least 1.

# Example 1:
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

# Output: ["Shogun"]
# Explanation: The only common element is "Shogun".

# Example 2:
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]

# Output: ["Shogun"]

# Example 3:
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]

# Output: ["KFC","Burger King","Tapioca Express","Shogun"]


class Solution:
    def findRestaurant(self, list1, list2):
        MapList1 = {}
        for i, x in enumerate(list1):
            MapList1[x] = i

        cur_min = float("inf")
        res = []
        for i, x in enumerate(list2):
            if x in MapList1:
                if cur_min == MapList1[x] + i:
                    res.append(x)
                elif cur_min > MapList1[x] + i:
                    cur_min = MapList1[x] + i
                    res = [x]
        return res


Solution().findRestaurant(list1, list2)


##################################################
# leetcode 350. Intersection of Two Arrays II
##################################################
# Difficulty: Easy
# Given two arrays, write a function to compute their intersection.

# Example 1:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


# Output: [2,2]
class Solution:
    def intersect(self, nums1, nums2):
        HashMap1 = {}
        HashMap2 = {}
        for x in nums1:
            if x in HashMap1:
                HashMap1[x] += 1
            else:
                HashMap1[x] = 1
        res = []
        for y in nums2:
            if y in HashMap1 and HashMap1[y] > 0:
                res.append(y)
                HashMap1[y] -= 1

        #         for y in nums2:
        #             if y in HashMap2:
        #                 HashMap2[y] += 1
        #             else:
        #                 HashMap2[y] = 1
        #         res = []
        #         for num in HashMap1:
        #             if num in HashMap2:
        #                 res.extend([num] * min(HashMap1[num], HashMap2[num]))
        return res


Solution().intersect(nums1, nums2)

##################################################
# leetcode 219. Contains Duplicate II
##################################################
# Difficulty: Easy
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.

# Example 1:
nums = [1, 2, 3, 1]
k = 3

# Output: true

# Example 2:
nums = [1, 0, 1, 1]
k = 1

# Output: true

# Example 3:
nums = [1, 2, 3, 1, 2, 3]
k = 2

i = 3
x = 1


# Output: false
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        HashMap = {}
        for i, x in enumerate(nums):
            if x not in HashMap:
                HashMap[x] = i
            else:
                if (i - HashMap[x]) <= k:
                    return True
                HashMap[x] = i
        return False


Solution().containsNearbyDuplicate(nums, k)

##################################################
# leetcode 359. Logger Rate Limiter
##################################################
# Difficulty: Easy
# Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not
# printed in the last 10 seconds.
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise
# returns false.
# It is possible that several messages arrive roughly at the same time.


class Logger:
    def __init__(self):
        self.message_dic = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.message_dic:
            self.message_dic[message] = timestamp
            return True
        else:
            if timestamp - self.message_dic[message] >= 10:
                self.message_dic[message] = timestamp
                return True
            else:
                return False

    def message_dic(self):
        return self.message_dic


Logger = Logger()

Logger.shouldPrintMessage(1, "foo")
Logger.shouldPrintMessage(2, "bar")
Logger.shouldPrintMessage(3, "foo")
Logger.shouldPrintMessage(8, "bar")
Logger.shouldPrintMessage(10, "foo")
Logger.shouldPrintMessage(11, "foo")

##################################################
# leetcode 49. Group Anagrams
##################################################
# Difficulty: Medium
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters
# exactly once.

# Example 1:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# import collections
# ans = collections.defaultdict(list)
# collections.defaultdict(list)


class Solution:
    def groupAnagrams(self, strs):
        HashMap = {}
        for i, x in enumerate(strs):
            count = [0] * 26
            for c in x:
                count[ord(c) - ord("a")] += 1
            if tuple(count) in HashMap:
                HashMap[tuple(count)].append(x)
            else:
                HashMap[tuple(count)] = [x]

        return HashMap.values()


Solution().groupAnagrams(strs)

##################################################
# leetcode 249. Group Shifted Strings
##################################################
# Difficulty: Medium
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which
# forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# Example:
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

x = strings[1]


class Solution:
    def groupStrings(self, strings):
        HashMap = {}
        for x in strings:
            indx = []
            if len(x) != 1:
                for j in range(1, len(x)):
                    indx.append((ord(x[j]) - ord(x[j - 1])) % 26)
                if tuple(indx) in HashMap:
                    HashMap[tuple(indx)].append(x)
                else:
                    HashMap[tuple(indx)] = [x]
            else:
                if "single" in HashMap:
                    HashMap["single"].append(x)
                else:
                    HashMap["single"] = [x]
        return HashMap.values()


Solution().groupStrings(strings)

##################################################
# leetcode 36. Valid Sudoku
##################################################
# Difficulty: Medium
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", ".", "9"],
]


class Solution:
    def isValidSudoku(self, board):
        N = len(board)
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for i in range(N):
            for j in range(N):
                element = board[i][j]
                if element != "." and (
                    element in rows[i]
                    or element in columns[j]
                    or element in boxes[(i // 3) * 3 + j // 3]
                ):
                    return False
                else:
                    rows[i].add(element)
                    columns[j].add(element)
                    boxes[(i // 3) * 3 + j // 3].add(element)
        return True


Solution().isValidSudoku(board)

##################################################
# leetcode 652. Find Duplicate Subtrees
##################################################
# Difficulty: Medium
# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.

# Example 1:
root = [1, 2, 3, 4, None, 2, 4, None, None, 4]

# Output: [[2,4],[4]]

# Example 2:
root = [2, 1, 1]

# Output: [[1]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        subtrees = defaultdict(list)

        def dfs(node):
            if not node:
                return "null"
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        res = []
        dfs(root)
        return res


##################################################
# leetcode 347. Top K Frequent Elements
##################################################
# Difficulty: Medium
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
nums = [1, 1, 1, 2, 2, 3]
k = 2

# Output: [1,2]

# Example 2:
nums = [1]
k = 1

# Output: [1]


class Solution:
    def topKFrequent(self, nums, k):
        HashMap = {}
        for x in nums:
            if x in HashMap:
                HashMap[x] += 1
            else:
                HashMap[x] = 1
        return sorted(HashMap, key=lambda x: HashMap[x], reverse=True)[:k]


Solution().topKFrequent(nums, k)

##################################################
# Unique Word Abbreviation
##################################################
# Difficulty: Medium
# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
# a) it                      --> it    (no abbreviation)
#      1
#      ↓
# b) d|o|g                   --> d1g
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓
# c) i|nternationalizatio|n  --> i18n
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
# A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example:
dictionary = ["deer", "door", "cake", "card"]
word = "dear"
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true


class ValidWordAbbr:
    def __init__(self, dictionary):
        self.dic = {}
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr not in self.dic:
                self.dic[abbr] = word
            elif self.dic[abbr] != word:
                self.dic[abbr] = ""

    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word):
        abbr = self.getAbbr(word)
        return abbr not in self.dic or self.dic[abbr] == word


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(dictionary)
obj.isUnique(word)

##################################################
# leetcode 707. Design Linked List
##################################################
# Difficulty: Medium
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/
# reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous
# node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:
# 1. MyLinkedList() Initializes the MyLinkedList object.
# 2. int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# 3. void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will
# be the first node of the linked list.
# 4. void addAtTail(int val) Append a node of value val as the last element of the linked list.
# 5. void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length
# of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be
# inserted.
# 6. void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

# Constraints:
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        # deal with edge cases
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.next = self.left

    def get(self, index):
        cur = self.left
        while cur and index > 0 and cur != self.right:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val):
        node, prev, next = ListNode(val), self.left, self.left.next
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val):
        node, prev, next = ListNode(val), self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtIndex(self, index, val):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            node, prev, next = ListNode(val), cur.prev, cur
            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    def deleteAtIndex(self, index):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev


myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
myLinkedList.get(1)
myLinkedList.deleteAtIndex(1)
myLinkedList.get(1)
　
##################################################
# leetcode 88. Merge Sorted Array
##################################################
# Difficulty: Easy
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

# Example 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# Output: [1,2,2,3,5,6]

# Example 2:
nums1 = [1]
m = 1
nums2 = []
n = 0

# Output: [1]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.size = 0
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        if index < self.size:
            cur = self.left.next
            while cur and index > 0:
                cur = cur.next
                index -= 1
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            self.size += 1
            cur = self.left
            while cur and index > 0:
                cur = cur.next
                index -= 1
            prev, next, node = cur, cur.next, ListNode(val)
            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            self.size -= 1
            cur = self.left.next
            while cur and index > 0:
                cur = cur.next
                index -= 1
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev


myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
myLinkedList.get(1)
myLinkedList.deleteAtIndex(1)
myLinkedList.get(1)

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
myLinkedList.get(1)
myLinkedList.deleteAtIndex(0)
myLinkedList.get(0)

##################################################
# leetcode 430. Flatten a Multilevel Doubly Linked List
##################################################
# Difficulty: Medium
# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may
# not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a
# multilevel data structure, as shown in the example below.
# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the
# list.

# Example 1:
head = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]

# Output: [1,2,3,7,8,11,12,9,10,4,5,6]

# Example 2:
head = [1, 2, None, 3]

# Output: [1,3,2]

# Explanation:
# The input multilevel linked list is as follows:
#   1---2---NULL
#   |
#   3---NULL


class ListNode:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


mylistnode = ListNode(1, None, None, None)
mylistnode.val
mylistnode.next = ListNode(3, None, None, None)
mylistnode = mylistnode.next

mylistnode.child = ListNode(7, None, None, None)


##################################################
# leetcode 146. LRU Cache
##################################################
# Difficulty: Medium
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# 1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# 2. int get(int key) Return the value of the key if the key exists, otherwise return -1.
# 3. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If
# the number of keys exceeds the capacity from this operation, evict the least recently used key.

# Follow up:
# Could you do get and put in O(1) time complexity?

# Example 1:
capacity = 2
# Output
# [null,null,null,1,null,-1,3]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1

# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, None, None, None)
        self.tail = ListNode(0, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val[1]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode((key, value), None, None, None)
        self.add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.val[0]]

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        prev, next = self.tail.prev, self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


##################################################
# leetcode 622. Design Circular Queue
##################################################
# Difficulty: Medium
# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed
# based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also
# called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the
# queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we
# can use the space to store new values.
# Implementation the MyCircularQueue class:
# 1. MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# 2. int Front() Gets the front item from the queue. If the queue is empty, return -1.
# 3. int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# 4. boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# 5. boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# 6. boolean isEmpty() Checks whether the circular queue is empty or not.
# 7. boolean isFull() Checks whether the circular queue is full or not.

# Example 1:
k = 3
# Output
# [null,true,true,true,false,false,true,true]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4


class ListNode:
    def __init__(self, val, next, prev):
        self.val, self.next, self.prev = val, next, prev


class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            newNode = ListNode(value, self.right, self.right.prev)
            self.right.prev.next = newNode
            self.right.prev = newNode
            self.space -= 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.space += 1
            return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.prev.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.next.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0


myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.enQueue(4)
myCircularQueue.Rear()

##################################################
# leetcode 286. Walls and Gates
##################################################
# Difficulty: Medium
# You are given an m x n grid rooms initialized with these three possible values.
# 1. -1 A wall or an obstacle.
# 2. 0 A gate.
# 3. INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a
# gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:
rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]

# Example 2:
rooms = [[-1]]

# Output: [[-1]]

# Example 3:
rooms = [[2147483647]]

# Output: [[2147483647]]

# Example 4:
rooms = [[0]]

# Output: [[0]]

# Constraints:
# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 231 - 1.


class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        rows, cols = len(rooms), len(rooms[0])
        q = []
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        def addRooms(r, c):
            if (r < 0 or r > rows or c < 0 or c > cols or (r, c) in visited or rooms[r][c] == -1):
                return
            else:
                q.append([r, c])
                visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
        

rooms = [[2147483647,0,2147483647,2147483647,0,2147483647,-1,2147483647]]


Solution().wallsAndGates(rooms)
rooms
    

##################################################
# leetcode 200. Number of Islands
##################################################
# Difficulty: Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
# edges of the grid are all surrounded by water.

# Example 1:
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

# Output: 1

# Example 2:

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Solution 1: DFS


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == "0":
                return
            else:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1),
                dfs(r, c - 1)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands
Solution().numIslands(grid)
                
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == "0":
                return
            else:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands


##################################################
# leetcode 387. First Unique Character in a String
##################################################
# Difficulty: Easy
# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
str = "leetcode"
# Output: 0

# Example 2:
str = "loveleetcode"
# Output: 2

# Example 3:
str = "aabb"
# Output: -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        HashMap = {}
        for i, s in enumerate(str):
            if s not in HashMap:
                HashMap[s] = i
            else:
                HashMap[s] = float('inf')
        
        return min(HashMap.values()) if min(HashMap.values()) < float('inf') else -1


Solution().firstUniqChar(str)

##################################################
# leetcode 752. Open the Lock
##################################################
# Difficulty: Medium
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6',
# '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
# Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock
# will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of
# turns required to open the lock, or -1 if it is impossible.

# Example 1:
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" ->
# "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be
# invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

# Example 2:
deadends = ["8888"]
target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".

# Example 3:
deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.

# Example 4:
deadends = ["0000"]
target = "8888"
# Output: -1

# Constraints:
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.


class Solution:
    def openLock(self, deadends: List, target):
        
        q = []
        visited = set(deadends)
        q.append(["0000", 0])
        
        def children(lock):
            res = []
            for i  in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[0:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[0:i] + digit + lock[i+1:])
            return res
        
        while q:
            lock, turn = q.pop(0)
            if lock == target:
                return turn
            for child in children(lock):
                if child not in visited:
                    q.append(child, turn + 1)
                    visited.add(child)
        return -1

        
                  