import time
import re

start_time = time.perf_counter()
fresh_ingredient_id_ranges: list[tuple[int, int]] = list()
fresh_ingredients = 0
with open('python/day5/data.txt', 'r') as f:
  parsing_fresh_ingredients = True
  for l in f.readlines():
    l = l.strip()
    if l == '':
      parsing_fresh_ingredients = False
      continue
    if parsing_fresh_ingredients:
      x, y = l.split('-')
      fresh_ingredient_id_ranges.append((int(x), int(y)))
    else:
      ingredient_id = int(l)
      for rx, ry in fresh_ingredient_id_ranges:
        if rx <= ingredient_id <= ry:
          fresh_ingredients += 1
          break

end_time = time.perf_counter() - start_time
print("Fresh ingredients:", fresh_ingredients)
print(f"Time: {(end_time * 1000):.4f} ms")