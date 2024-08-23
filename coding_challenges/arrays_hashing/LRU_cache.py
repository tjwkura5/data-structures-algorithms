# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity):
#         self.cache = {}
#         self.capacity = capacity

#     def get(self, key):
#         value = self.cache.get(key, -1)
#         if value > 0:
#             self.add_lru(key)
#         return value
    
#     def add_lru(self, key):
#         if key in self.lru:
#             self.lru.remove(key)
#         self.lru.append(key)

#     def put(self, key, value):
#         if len(self.cache) == self.capacity:
#             del self.cache[]
    
#         self.cache[key] = value
#         self.add_lru(key)
#         self.length += 1
