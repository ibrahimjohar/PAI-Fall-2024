set = {1, 12, 32, 43, 53}

print("original set: ", set)
set.add(4)
print("add(element): ", set)

intersection_set = set.intersection({32, 53})
print("intersection set: ", intersection_set)

union_set = set.union({31, 54, 123})
print("union set: ", union_set)

# add(elem): Adds an element to the set.
# clear(): Removes all elements from the set.
# copy(): Returns a shallow copy of the set.
# difference(*s): Returns a new set with elements in the set that are not in the others.
# difference_update(*s): Removes elements found in the specified sets.
# discard(elem): Removes an element from the set if it is a member.
# intersection(*s): Returns a new set with elements common to all specified sets.
# intersection_update(*s): Updates the set with the intersection of itself and others.
# isdisjoint(s): Returns True if the set has no elements in common with s.
# issubset(s): Returns True if the set is a subset of s.
# issuperset(s): Returns True if the set is a superset of s.
# pop(): Removes and returns an arbitrary element from the set.
# remove(elem): Removes an element from the set; raises KeyError if the element is not present.
# discard(elem): Removes an element from the set if it is present.
# union(*s): Returns a new set with elements from the set and all others.
# update(*s): Updates the set with the union of itself and others.