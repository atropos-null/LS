# Traversal Shapes — Notebook Reference

> **Let the relationship required by the contract determine the traversal shape.**

Ask: **What must be available at the same moment?**

Contract (required behavior) → relationship → values needed together → traversal shape → state/access.

Common finite-sequence patterns from Topic 7. Clues suggest a shape; the full contract decides. Patterns can overlap.

| Problem style | Contract / keyword clues | What must be available together | Typical traversal shape | State/access needed | Common boundary issue |
|---|---|---|---|---|---|
| Current-item only | Count, filter, sum items satisfying X | Current item | Single pass | Count, total, result | Empty input; end of input |
| Previous/current comparison | Immediately before; changed from previous | Previous + current | Adjacent, backward | Previous value + summary | First item has no previous |
| Current/next comparison | Immediately after; followed by; next value | Current + next | Lookahead | Index or buffered next item | Last item has no next |
| Fixed window | Rolling k values; contiguous block of length k | k neighboring items | Sliding window; chunks if non-overlapping | Window buffer or indices | Incomplete windows; define overlap |
| Run tracking | Longest consecutive; maximal run; continues while | Current item + run context | Sequential run tracking | Run length, previous/category, best | Final run must be counted |
| Grouping by change | Group consecutive equal/same-category values | Current item + group identity | Sequential grouping | Current group, category, results | Changed item starts next group |
| Delimiter grouping | Split on comma, 0, marker, sentinel | Current item + current group | Scan for delimiters | Group buffer + results | Empty groups; final group lacks delimiter |
| Mode / phase | After START; before/after event; while active | Current event + mode | State-machine scan | Mode/flag + ordinary state | Define how transition item is handled |
| Distinct pairs | Every pair; combinations of two | One item + each later item | Nested pair traversal | Outer/inner positions, summary | Avoid self-pairs and duplicates: j > i |
| Cartesian / all-against-all | Every A with every B | One A item + each B item | Nested loops over two collections | Outer/inner items | Revisit all B for each A; empty input |
| Parallel / lockstep | Corresponding items; A[i] with B[i] | Items at matching positions | Advance together | Paired items + summary | Unequal lengths; zip stops at shortest |
| Merge-style | Merge sorted lists; take whichever comes next | Current A + current B | Advance sources independently | Position/current item per source, output | One ends first; append the remainder |
| Independent multi-stream | Process whichever source qualifies next | Relevant state of each source | Independently advancing sources | Position/state per source | Each source can end separately |
| Index-dependent | Position; every nth item; index and value | Current item + index | Indexed pass | Index + value | Zero/one-based counting; off-by-one |
| Search from each position | For each item, search later items | Anchor item + later region | Outer pass + inner search | Anchor/index, search state | Inner start/end; no match |
| Whole history | All earlier items; everything seen so far | Current item + needed history | Pass with retained history | List/set/dict as required | Compare before adding current item |
| History summary | Best, count, frequency so far | Current item + summary of past | Single pass | Accumulator, frequency map, best | Empty input; initialize summary correctly |
| Nested regions | Nested START/END; parentheses; matched markers | Current token + open-region context | Scan with depth/stack | Depth counter or stack | Unmatched markers; flag cannot track depth > 1 |

## Six terms to keep straight

- **Adjacent comparison:** Compares neighbors: previous + current or current + next.
- **Lookahead:** Inspects future input before deciding about the current item. Often one item ahead, but may be more.
- **Parallel traversal:** Processes corresponding positions together, such as names and scores. Both advance in lockstep.
- **Merge-style traversal:** Compares current items from sorted sources; advances the source whose item is consumed. Sources may move at different rates.
- **Nested traversal:** For each outer item, traverses multiple inner items. This differs from tracking nested regions with a stack.
- **Pairwise traversal:** Here, visits each distinct pair from one collection once, usually with j > i. Terminology varies: Python's `itertools.pairwise` produces adjacent pairs instead.

**Boundary rule:** A traversal must stop at the last position for which the required relationship can still be observed. For indexed current/next comparisons, use `range(len(items) - 1)`.

*Print tip: render the Markdown and print in landscape orientation so the six-column table stays readable.*
