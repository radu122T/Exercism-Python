# Instructions
# Take a nested list and return a single flattened list with all values except nil/null.

# The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

# For Example

# input: [1,[2,3,null,4],[null],5]

# output: [1,2,3,4,5]

def flatten(l):
  out = []
  k = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  for item in out:
      if type(item)==int:
          k.append(item) 
  return k
