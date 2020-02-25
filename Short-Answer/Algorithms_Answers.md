#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
I looked up whether it's possible to use the \* operator on iterables in Python, and the internet said no. So, in my answer, I am assuming only ints/floats will not break this code.

O(n) - there is a while loop with no conditions for lessening the amount of the value within it

b)
outer loop O(n) - no lessening
inner loop O(log n) - j gets increased, so it skips
nested = multiply
answer = O(n log n)

c)
O(n) because a recursive call is made for every element

## Exercise II

My first solution is to not throw eggs out of buildings in general.

If you have a building that has a certain number of floors, at a certain height, eggs will break if dropped. If they are lower than that floor and get dropped, they will be okay.

This is a search problem, because we are trying to find the floor where things eggs start breaking. Because buildings don't usually have hundreds of floors, I am not worried about speed/recursion too much.

For now, I would just go through every floor and make a note of the first floor where the egg breaks

```python
def floor_finder(building):
  first_floor_where_eggs_break = None

  while floor_where_eggs_break is None :
    throw egg
    if broken:
      first_floor_where_eggs_break = floor

  return first_floor_where_eggs_break
```

The runtime complexity is O(n), since I used linear search instead of binary search
