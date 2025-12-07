import time
import re

start_time = time.perf_counter()
fresh_ingredient_id_ranges: list[tuple[int, int]] = list()
fresh_ingredient_ids_count = 0
with open('python/day5/data.txt', 'r') as f:
  parsing_fresh_ingredients = True
  for l in f.readlines():
    l = l.strip()
    if l == '':
      parsing_fresh_ingredients = False
      break
    if parsing_fresh_ingredients:
      x, y = l.split('-')
      fresh_ingredient_id_ranges.append((int(x), int(y)))

fresh_ingredient_id_ranges = sorted(fresh_ingredient_id_ranges)
optimised_ranges: list[tuple[int, int]] = list()
previous_range_min, previous_range_max = fresh_ingredient_id_ranges[0]
for id_range in fresh_ingredient_id_ranges[1:]:
  rx, ry = id_range
  if rx > (previous_range_max + 1):
    fresh_ingredient_ids_count += previous_range_max - previous_range_min + 1
    optimised_ranges.append((previous_range_min, previous_range_max))
    previous_range_min = rx
  if ry > previous_range_max:
    previous_range_max = ry
fresh_ingredient_ids_count += previous_range_max - previous_range_min + 1
optimised_ranges.append((previous_range_min, previous_range_max))

end_time = time.perf_counter() - start_time
print("Total fresh ingredients:", fresh_ingredient_ids_count)
print(f"Time: {(end_time * 1000):.4f} ms")