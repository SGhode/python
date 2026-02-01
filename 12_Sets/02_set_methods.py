s = {34, 23, 1, 3, 22}

print(s)

s.add(32)
s.add(322)
s.remove(1)
s.discard(3343) # If the element is present in the set, only then it removes. No error if the element not found.
s.pop() # Remove random elements
print(s)