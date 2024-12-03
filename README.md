## Advent of Code 2024

### Day 01
- $\ell_1$ distance between two sorted lists
- hashmap lookup

### Day 02
- smooth strict monotonic function
- tolerate a single bad level -> l[:i] + l[i+1:]

### Day 03
- regex
- came across a smart solution
  - \_\_\_\_do\_\_\_\_don't\_\_\_\_do\_\_\_\_
  - split at **do**, getting [\_\_\_\_, \_\_\_\_don't\_\_\_\_, \_\_\_\_]
  - for each substring in the list, split at **don't**, <ins>extract the first item</ins>, append them into a list.