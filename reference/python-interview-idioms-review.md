# Python Interview Idioms — Daily Review

*Source: `Python Coding Interviews/` (39 drills). Read this right before you open a LeetCode problem — this is the DSA-idiom layer on top of [Fundamentals](./python-fundamentals-review.md).*
See also: [LeetCode Readiness gap analysis](./leetcode-readiness-gaps.md) · [Mission](../MISSION.md)

---

## 1. Your Documented Mistakes

Every one of these has a `submission-0 → submission-1` (or `-2`) fix in your history — proof you hit it once, not a hypothetical.

| # | Topic | What went wrong | Fix | Why it matters |
|---|-------|------------------|-----|-----------------|
| 1 | `python-min-max-shortcut` | `for i in range(len(nums)): diff = nums[i] - nums[i-1]` — at `i=0`, `nums[-1]` silently wraps to the **last** element instead of erroring | `for i in range(1, len(nums))`, or better: `for prev, curr in zip(nums, nums[1:])` | Python's negative indexing doesn't crash on this bug — it just gives you a wrong answer. Always ask "what does index -1 mean here, and do I want that?" |
| 2 | `python-heapify` (`heap_sort`) | `heapq.heapify(nums); nums.sort()` — heapifies, then throws the heap away and sorts anyway | Repeated `heapq.heappop(nums)` into a result list | If you build a heap, use it — popping is the point. Reaching for `.sort()` afterward means you didn't understand why the heap was built. |
| 3 | `python-heap-n-smallest` | Built a second heap + negated values just to reverse a 2-element list | `min_2[::-1]` | Overengineering — don't reach for heap/negation tricks for problems that are just slicing. |
| 4 | `python-sorted-set-basics` | `sorted_set.pop(0)` × 3 to peek at the first 3 elements — **mutates/destroys** the caller's data structure just to read it | `list(sorted_set)[:3]` | Never let a "read" operation have side effects on shared state — this is a correctness bug waiting to bite the next line of code that uses `sorted_set`. |
| 5 | `python-hash-map-basics` | `for i in range(len(keys)): res[keys[i]] = values[i]` | `for key, value in zip(keys, values): res[key] = value` | Classic index-juggling instead of `zip`. If you're indexing two parallel lists, it's a `zip`. |
| 6 | `python-dict-items` | Second submission reimplemented `.items()` manually with a loop — the *first* version (`list(d.items())`) was already correct and more idiomatic | Prefer the built-in | A reminder that "resubmit" isn't always "improve" — check you're not un-learning an idiom. |

**Unresolved bugs (no submission-1 exists yet — fix these too):**

- **`python-2d-grid` `in_bounds`**: uses `r > rows` / `c > cols` instead of `r >= rows` / `c >= cols` — classic off-by-one on the upper boundary of a grid. It slipped through because your own test cases happened to fail the `c` check first. **This exact bug pattern shows up constantly in grid/matrix BFS-DFS problems.**
- **`python-multi-dimensional-list`** (`curMax = -1`) and **`python-loop-unpacking`** (`curBest = 0`): running-max initialized with a sentinel instead of the first element or `float('-inf')` — same class of bug as the Fundamentals doc's `get_max`. Fails silently on all-negative input.

---

## 2. Anti-Patterns You Repeat

- **Importing the private `_heapq` module** (`python-heap-pop`): `from _heapq import heappop` instead of `import heapq; heapq.heappop(...)`. The underscore-prefixed module is a CPython implementation detail — always use the public `heapq` API.

- **Verbose boolean return** (`python-inequality`):
  ```python
  if 0 < len(x) <= max: return True
  else: return False
  # prefer
  return 0 < len(x) <= max
  ```

- **Inconsistent sort idiom** (`python-sort-descending`): mixes `.sort(); .reverse()` (two passes) with `.sort(reverse=True)` (one pass) in the same file. Standardize on `reverse=True` / `key=`.

- **`range(len(x))` again, one level up** (`python-dict-comprehension`): `{nums[i]: i for i in range(len(nums))}` — same habit flagged in the [Fundamentals doc](./python-fundamentals-review.md), still showing up in comprehension form. Prefer `{num: i for i, num in enumerate(nums)}`.

---

## 3. Quick Reference by Category

### Sorting & comparators
```python
sorted(lst)                          # new list; lst.sort() mutates in place
sorted(lst, reverse=True)            # descending, single pass — don't .sort();.reverse()
sorted(lst, key=lambda x: x[1])      # sort by 2nd tuple element
sorted(lst, key=lambda x: (-x[0], x[1]))  # multi-key: primary desc, secondary asc
```
`sorted()`/`.sort()` are **stable** — equal-key elements keep their relative order. Useful for multi-pass sorts.
`key=` accepts any callable, not just a `lambda` — a named function works too (`python-sort-custom` uses `key=get_word_length`), which is handy when the comparator is complex enough to want a name or reuse.

### Heaps (`heapq` is a MIN-heap only)
```python
import heapq
heapq.heapify(lst)          # O(n) in-place min-heap
heapq.heappush(lst, x)
heapq.heappop(lst)          # smallest
heapq.heappush(lst, -x)     # negate to fake a MAX-heap; remember to re-negate on pop
heapq.nlargest(k, lst); heapq.nsmallest(k, lst)   # skip manual heap-building for this
```
If you build a heap, **pop from it** — don't heapify and then `.sort()` (mistake #2 above). And `heapify()` only guarantees `heap[0]` is the minimum — the rest of the list is heap-ordered, **not** fully sorted; don't try to read it in order without popping.

**Heap of tuples (priority + payload)** — push `(priority, value)` so you can sort/pop by a key that isn't the value itself:
```python
heap = []
for num in nums:
    heapq.heappush(heap, (-num, num))   # sort by -num (i.e. descending), keep num as payload
res = [heapq.heappop(heap)[1] for _ in range(len(heap))]
```
This is the pattern behind Dijkstra (`(distance, node)`) and "k closest points" problems — the thing you sort by and the thing you return don't have to be the same value.
Ties in a heap of tuples compare element-by-element — if item 0 can tie, add a tiebreaker (index) as item 1, since arbitrary objects at position 2+ may not support `<`.

### Hashing: set / dict / Counter / defaultdict
```python
s = set(lst)                         # O(1) average membership test: x in s
s.add(x); s.discard(x)               # discard: no error if missing (vs s.remove(x), which raises)
{x for x in lst}                     # set comprehension — see python-set-comprehension

from collections import Counter, defaultdict
Counter(lst)                         # {value: count}, .most_common(k)
counter.update(other_iterable)       # merge/add counts from another string or iterable in place
defaultdict(int)                     # missing key -> 0, no KeyError
defaultdict(list)                    # missing key -> []
d.get(key, default)                  # for a plain dict, avoids KeyError
```
**Sets have no guaranteed iteration order.** `python-hash-set-basics`, `python-set-comprehension`, and `python-tuple-keys` all `sorted(list(...))` their output before printing for exactly this reason — if your own tests print a raw set/dict and the order looks "random" or changes between runs, that's expected, not a bug.

### Sorted structures — `sortedcontainers` (SortedDict / SortedSet)
Third-party, not stdlib (`pip install sortedcontainers`) — but NeetCode's drills use it, so know it. Unlike `heapq` (which only guarantees the *smallest* is at index 0), these keep the **entire** collection in sorted order at all times, at O(log n) per insert/remove. Reach for them when you need repeated inserts/removals *and* full sorted-order iteration or slicing; reach for `heapq` when you only ever need the current extreme; reach for `sorted()` for a one-shot sort.
```python
from sortedcontainers import SortedDict, SortedSet

sd = SortedDict({'b': 2, 'a': 1})
sd.items()                 # iterates in key-sorted order, always
sd.pop(key)                 # KeyError if missing — same as a plain dict
sd.pop(key, default)        # safe form

ss = SortedSet([3, 1, 2])
ss.add(x)
ss.discard(x)                # no error if x is missing (use this, not .remove, for a "delete if present")
ss.remove(x)                  # raises KeyError if missing
list(ss)[:3]                  # first 3 smallest — read-only, doesn't mutate ss
```
**Your mistake #4 above is the one to remember here**: `ss.pop(0)` × 3 *removes* the smallest 3 elements from the set as a side effect. If you just want to *read* the first k, slice a `list(ss)` instead — never `.pop()` to peek.

### List mutation, copying, concatenation
```python
arr1 + arr2            # NEW list — arr1, arr2 unchanged (python-list-concat)
arr1.extend(arr2)       # mutates arr1 in place, no new list (python-resizable-list-part-2)
arr.insert(idx, x)      # inserts at idx — NEVER raises, even if idx is out of range;
                        # idx too big just appends at the end, idx very negative inserts at the start
arr.remove(x)           # removes first occurrence — raises ValueError if x is missing;
                        # guard with `if x in arr:` first (python-resizable-list-part-2), same
                        # shape as dict.pop(key, default) / set.discard(x)
arr.copy()              # shallow copy — use before mutating if the caller's original must be preserved
                        # (python-list-clone: copy() first, then .remove() on the copy)
```
`insert()`'s silent clamping is the one to remember — unlike `arr[idx]`, which raises `IndexError` on an out-of-range index, `arr.insert(idx, x)` never does. If a bug looks like "my insert didn't go where I expected" rather than a crash, this is why.

### Deque / stack / queue
```python
from collections import deque
dq = deque(lst)
dq.append(x); dq.pop()               # stack ops, O(1)
dq.appendleft(x); dq.popleft()       # queue ops, O(1)
```
**Never use `list.pop(0)` as a queue** — it's O(n) per call, O(n²) overall. Use `deque` any time you dequeue from the front. A plain list *is* fine as a **stack** — `.append(x)`/`.pop()` (no arg) both operate on the end and are O(1) (`python-stack-push-pop` does exactly this correctly). The O(n) trap is specifically about removing from the *front* of a list.

### Comprehensions
```python
[x*2 for x in lst if x > 0]                 # list
{x for x in lst}                            # set
{k: v for k, v in pairs}                    # dict
[[0]*cols for _ in range(rows)]             # 2D grid — see shallow-copy trap below
```

### 2D grids / lists — the shallow-copy trap
```python
grid = [[0] * cols] * rows        # BUG: all `rows` point to the SAME inner list
grid = [[0] * cols for _ in range(rows)]   # correct: new list each row
```
You've correctly avoided this trap in your own drills (`python-nested-list-comprehension` builds each row with its own comprehension, not `*rows`) — good, keep doing it. But **watch grid boundary checks**: use `r >= rows` / `c >= cols`, not `r > rows` (see unresolved bug above).

### Unpacking / zip / enumerate
```python
for i, val in enumerate(lst): ...
for a, b in zip(list1, list2): ...           # parallel iteration — replaces index-juggling
a, *rest = lst                                # unpack first + remainder
(a, b), c = pairs[0], pairs[1]                # nested unpacking
```

### Tuples as dict keys
Tuples are hashable (if their contents are) — use `(row, col)` as a dict/set key for visited-cell tracking in grid problems: `visited = set(); visited.add((r, c))`.

---

## 4. Daily Self-Check (60 seconds, before you start practicing)

- [ ] Building a heap? Confirm I actually `heappop` from it — not `heapify()` then `.sort()`.
- [ ] Need a max-heap? Negate on push, negate again on pop — and remember to do it consistently.
- [ ] Popping/dequeuing from the **front** of a list? Switch to `deque`.
- [ ] Indexing two lists in parallel with `range(len(...))`? Use `zip`.
- [ ] Grid boundary check — is it `>=`, not `>`?
- [ ] Running max/min — seeded with the first element or `±float('inf')`, not `0`?
- [ ] About to read from a data structure — am I accidentally mutating it (e.g. `.pop()` to "peek")?
