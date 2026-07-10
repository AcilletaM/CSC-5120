from cat import Cat

print(f"total number of cats created so far {Cat.numberOfCats}")
kitty = Cat("Sunny", "Orange")
# where is self? -> we don't specify it

print(f"total number of cats created so far {Cat.numberOfCats}")

print(f"Check type() of an instance of the Cat class: {type(kitty)}")

print(f"hello {kitty.name}")

cat2 = Cat("Doug", "red")
print(f"total number of cats created so far {Cat.numberOfCats}")
print(f"{cat2.name}'s color is {cat2.color}")

# what the type?
kitty.hisses_at(cat2)

#"private" variables
#print(kitty._shhh)

# declares an emptylist (think array/arrayList from other coding languages)
my_cats = []

my_cats.append(kitty)
my_cats.append(cat2)
kitty.temper = "very nice"

print(f"how many things are in the my_cat array?: {len(my_cats)}")

# something similar to java.toString()
print(f"printing my_cats: {my_cats}")
print(f"printing kitty {kitty}")
print(f"printing str(kitty){str(kitty)}")

my_cats[0].name = "hi mom"
print(my_cats)
print(kitty) # gets at same underlying Cat object in memory as my_cats[0]
# another way to print out all info in a list
#for c in my_cats:
 #   print(f"cat: {c.name}", end="|||") # end specifies whether you want a newline or something else