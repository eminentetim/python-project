tree_hight = input("how tall is you tree : ")
tree_hight = int(tree_hight)
space = tree_hight -1
hashes = 1

stump_space = tree_hight -1
while tree_hight != 0:

	for i in range(space):
		print(' ', end="")

	for i in range(hashes):
		print('#', end="")
	
	print()
	space -= 1
	hashes += 2
	tree_hight -= 1
for i in range(stump_space):
	print(' ', end="")
print('#')
