chilli_wishlist = ["igloo", "chicken", "donut toy","cardboard box"]

indexing
print(len(chilli_wishlist))
print(chilli_wishlist[4])

print(chilli_wishlist[0])
print(chilli_wishlist[1])
print(chilli_wishlist[-1])
print(chilli_wishlist[0:2])
print(chilli_wishlist[1:3])
chilli_wishlist[1] = "carrot" 
print(chilli_wishlist)

print(chilli_wishlist[-1: 0])
print(chilli_wishlist[-2: 0])

chilli_wishlist.append("dig mat")
chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
chilli_wishlist.insert(1, "peanut butter")
print(chilli_wishlist)

chilli_wishlist.pop()
chilli_wishlist.pop(1)
chilli_wishlist.remove("kong")
print(chilli_wishlist)

if "tennis ball" in chilli_wishlist:
    print("Chilli would like a tennis ball.")
else:
    print("Chilli doesn't feel like playing fetch.")

if len(chilli_wishlist > 8):   # TypeError: '>' not supported between instances of 'list' and 'int'
    print("Chilli wants a lot of stuff!")

chilli_wishlist = [
    ["igloo"],  #bed
    ['donut toy','tennis ball', 'crocodile toy'], # toys
    ['chicken', 'peanut butter'], # treats
    ['cardboard box', 'kong', 'dig mat'] # activity based toys
]

print(chilli_wishlist[2])
print(chilli_wishlist[2][1])

letters = ["a", "b", "c", "d", "e"]
letters.append("f")
print(letters)
letters.extend(["g", "m"])
print(letters)
letters.insert(1, "z")
letters.pop(2)
print(letters)
letters.remove("d")
print(letters)