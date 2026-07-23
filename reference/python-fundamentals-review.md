# Python Fundamentals — Daily Review

*Source: `Python For Beginners/` (82 drills). Read this before opening a LeetCode problem.*
See also: [Interview Idioms review](./python-interview-idioms-review.md) · [LeetCode Readiness gap analysis](./leetcode-readiness-gaps.md) · [Mission](../MISSION.md)

---

## 1. Your Documented Mistakes

These are things you actually got wrong (proven by a `submission-1.py` fix, or a live bug still sitting in the code). Interviewers will hit exactly these patterns.

| # | Topic | What went wrong | Fix | Why it matters |
|---|-------|------------------|-----|-----------------|
| 1 | `python-for-loops-step` | Looped `range(0,11,1)` then manually multiplied output by 10 | `range(0,101,10)` — the 3rd arg **is** the step | You didn't trust `range`'s step argument. In interviews, `range(start, stop, step)` should be reflexive. |
| 2 | `python-list-find` | Used `nums.index(target)` where the drill wanted manual index tracking, then rewrote with a hand-rolled counter | Should have been `for i, n in enumerate(nums): if n == target: return i` | Neither version used `enumerate`, the actual idiomatic tool for "value + its index." Default to it. |
| 3 | **`python-list-functions` — `get_max` (still unfixed, no submission-1)** | `res = 0` as the starting "max so far", only updates when a bigger value is seen | Initialize with `res = nums[0]` (or `float('-inf')`) | **Silently wrong on all-negative lists.** This is a classic interview bug (max-subarray, best-score problems) — it passes on happy-path tests and fails in the interviewer's edge case. |
| 4 | **`python-list-functions` — `get_min` (still unfixed, no submission-1)** | `if res > n or res == 0: res = n` — the `or res == 0` clause means that once the running min legitimately becomes `0`, the *next* element overwrites it regardless of whether it's actually smaller | Initialize with `res = nums[0]` (or `float('inf')`), drop the `== 0` clause entirely | **Sharper than the `get_max` bug**: `get_min([0, 5, 3])` returns `3`, not `0` — wrong even though every element is non-negative. `0` was used as *both* the sentinel and a valid data value, so the code can't tell them apart. |

**Action:** go fix `get_max`/`get_min` right now — these are the two real correctness bugs still sitting in your code.

---

## 2. Anti-Patterns You Repeat (no bug yet, but bad habits)

- **`range(len(x))` instead of iterating directly / `enumerate`**
  Seen in: `python-string-looping`, `python-intro-to-dictionaries`.
  ```python
  # you wrote
  for i in range(len(my_string)): print(my_string[i])
  # prefer
  for ch in my_string: print(ch)
  for i, ch in enumerate(my_string): ...   # when you need the index too
  ```
  You already know the better pattern — `python-string-looping-shorthand` (a separate drill) iterates the string directly with `for c in word`. The gap isn't understanding, it's applying it consistently.

- **Manual `if key in dict: ... else: ...` counting instead of `.get(key, default)`** (`python-dict-practice`)
  ```python
  if c in res: res[c] += 1
  else: res[c] = 1
  # prefer
  res[c] = res.get(c, 0) + 1
  ```

- **Hand-rolled loop to build a set instead of the `set()` constructor** (`python-intro-to-sets`)
  ```python
  res = set()
  for n in nums: res.add(n)
  # prefer
  res = set(nums)
  ```

- **`len(x) - n` instead of negative indexing** (appears 3×: `python-list-slicing`, `python-string-slicing-part-2`, `python-string-indexing`)
  ```python
  my_list[len(my_list) - 3:]   # you wrote
  my_list[-3:]                 # prefer
  word[len(word) - 1]          # you wrote
  word[-1]                     # prefer
  ```

- **Verbose boolean wrapping** — 4 separate instances: `python-list-operations` (both `check_list_empty` and `check_element_in_list`), `python-set-practice.contains_duplicate`, `python-logic-condition.discount_applies`
  ```python
  if x: return True
  else: return False
  # prefer
  return bool(x)          # or just `return x` if x is already boolean-ish
  ```
  This is your single most-repeated habit in the whole set — worth drilling until it's automatic.

- **Bare `except:`** (`python-try-except`) — catches *everything*, including `KeyboardInterrupt`/typos, and hides what actually failed.
  ```python
  except:                       # avoid
  except ValueError as e:       # prefer — name the exception you expect
  ```
  You already do this correctly in `python-multiple-except-blocks` and `python-error-catching` — just apply it consistently from the start.

- **Redundant `str(input())`** (`python-parse-input`, `python-read-input-practice`) — `input()` already returns `str`. The wrapper is a no-op that signals you weren't sure of the return type.

- **Dead code after exhaustive control flow** (`python-truthy-and-falsy`) — an `if/else` that already returns on both branches, followed by more unreachable `return` statements. Trace your control flow to the end before adding more branches.

---

## 3. Quick Syntax Reference

**Types & truthiness**
- Falsy: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is truthy.
- `type(x)`, `isinstance(x, int)`; Python is dynamically but strongly typed — `"1" + 1` is a `TypeError`, not implicit coercion.
- **`int(x)` truncates toward zero, it does not round** (`python-type-casting`): `int(3.99) == 3`, `int(-3.99) == -3`. If you want rounding, use `round(x)`.

**Operators** (`python-arithmetic-operators`, `python-more-operators`, `python-shorthand-operators`, `python-boolean-and/or/negation`)
```python
7 // 2      # floor division -> 3 (not 3.5)
7 % 2       # modulo -> 1
2 ** 10     # exponent -> 1024
x += 1; x -= 1        # shorthand — same as x = x + 1 / x = x - 1
a and b, a or b, not a   # short-circuit: `and`/`or` return one of the operands, not always True/False
```

**Control flow: `pass` / `break` / `continue`** (`python-control-flow`)
- `pass`: no-op placeholder — use it to stub out a body you haven't written yet, never as real logic.
- `break`: exits the loop entirely.
- `continue`: skips to the next iteration, doesn't exit the loop.

**Strings** — immutable; every "modification" makes a new string.
```python
s[::-1]                 # reverse
s[a:b], s[a:b:step]      # slicing, both ends flexible/negative
f"{name} is {age}"       # f-strings > .format() > concatenation
"-".join(list_of_str)    # join, not += in a loop (O(n²) trap)
```

**Lists**
```python
lst.append(x); lst.pop(); lst.pop(0)   # pop(0) is O(n) — flag for later (see interview doc: deque)
lst[-1], lst[-3:]                       # negative indexing over len(lst)-n
sum(lst), min(lst), max(lst)            # don't hand-roll unless the drill demands it
```

**Dicts**
```python
d.get(key, default)      # avoids KeyError, avoids manual `if key in d` checks
d.pop(key, default)      # same idea for deletion — see python-dict-remove
for k in d: ...                       # iterates keys, same as d.keys()
for k, v in d.items(): ...
d.values()
```

**Sets & tuples**
```python
{1,2,3} & {2,3,4}   # intersection
{1,2,3} | {2,3,4}   # union
a, b = b, a          # tuple-unpack swap, no temp variable
```

**Functions & scope**
- `global` needed to *rebind* a global inside a function; not needed to read it.
- Default arguments are evaluated **once** at function definition — never use a mutable default (`def f(x=[])`); use `def f(x=None): x = x or []`.
- **Reassigning a parameter only rebinds the local name — it never affects the caller's variable** (`python-scope`: `n = n + 1` inside a function leaves the outer `n` unchanged). This is *not* the same as mutating a mutable object passed in (e.g. `some_list.append(x)`) — that mutation IS visible to the caller. Reassignment vs. mutation is the actual distinction, not "pass by value vs. reference."
- **A function with no `return` statement implicitly returns `None`** (`python-type-hints`: `greet()` only prints, so `type(greet(...))` is `NoneType`). Don't assume a helper function returns something just because it "does work."

**Error handling**
```python
try:
    ...
except SpecificError as e:
    ...
finally:
    ...   # runs regardless — cleanup only
```

---

## 4. Daily Self-Check (60 seconds, before you start practicing)

- [ ] Am I about to write `range(len(x))`? Stop — use direct iteration or `enumerate`.
- [ ] Am I initializing a running max/min with `0`? Use the first element or `±float('inf')` instead — and check `0` isn't also a valid data value in play (the `get_min` bug).
- [ ] Am I about to `return True`/`return False` from an `if/else`? Just `return` the boolean expression.
- [ ] Am I manually checking `if key in dict` to count/increment? Use `.get(key, 0) + 1`.
- [ ] Am I about to `except:` bare? Name the exception.
- [ ] Am I slicing with `len(x) - n`? Use `x[-n:]`.
- [ ] Did I just write a mutable default argument? Fix it before it becomes a Heisenbug.
- [ ] Am I using `int(x)` expecting it to round? It truncates — use `round(x)` if you need rounding.
