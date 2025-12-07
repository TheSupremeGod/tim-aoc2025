import time
import re

start_time = time.perf_counter()
paper_rolls: list[list[int]] = list()
removed_rolls_of_paper = 0
with open('python/day4/data.txt', 'r') as f:
  for l in f.readlines():
    l = l.strip()
    rolls = [r.start() for r in re.finditer('@', l)]
    paper_rolls.append(rolls)
  while True:
    paper_rolls_removed = False
    for row_i, paper_rolls_row in enumerate(paper_rolls):
      for col_i, paper_roll in enumerate(paper_rolls_row):
        close_rolls = 0
        close_rolls += sum([roll in paper_rolls_row for roll in [paper_roll-1, paper_roll+1]])
        if row_i > 0:
          rolls_above = [paper_roll-1, paper_roll, paper_roll+1]
          row_above = paper_rolls[row_i-1]
          close_rolls += sum([roll in row_above for roll in rolls_above])
        if row_i < (len(paper_rolls) - 1):
          rolls_above = [paper_roll-1, paper_roll, paper_roll+1]
          row_below = paper_rolls[row_i+1]
          close_rolls += sum([roll in row_below for roll in rolls_above])
        if close_rolls < 4:
          del paper_rolls[row_i][col_i]
          removed_rolls_of_paper += 1
          paper_rolls_removed = True
    if not paper_rolls_removed:
      break

end_time = time.perf_counter() - start_time
print("Accessible paer rolls:", removed_rolls_of_paper)
print(f"Time: {(end_time * 1000):.4f} ms")