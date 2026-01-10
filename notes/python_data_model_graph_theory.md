# Python's Data Model Through Graph Theory

## A Comprehensive Guide to Understanding Python's Internals

---

# Table of Contents

1. [Introduction: What is Graph Theory?](#part-1-introduction)
2. [Python's Data Model as a Graph](#part-2-pythons-data-model-as-a-graph)
3. [Dunder Methods as Graph Operations](#part-3-dunder-methods-as-graph-operations)
4. [Async/Await as Coroutine Graphs](#part-4-asyncawait-as-coroutine-graphs)
5. [Generators as Execution Graphs](#part-5-generators-as-execution-graphs)
6. [Python's Import System as a Dependency Graph](#part-6-pythons-import-system-as-a-dependency-graph)
7. [Decorators as Function Graph Transformers](#part-7-decorators-as-function-graph-transformers)
8. [Garbage Collection and Cycle Detection](#part-8-garbage-collection-and-cycle-detection)
9. [Conclusion: Python as a Living Graph](#part-9-conclusion-python-as-a-living-graph)

---

# Part 1: Introduction

## What is Graph Theory?

**Graph Theory** is a branch of mathematics that studies **graphs** — structures made up of: 

- **Nodes (vertices)**: Individual entities or objects
- **Edges**:  Connections or relationships between nodes

Graphs can be:
- **Directed**:  Edges have a direction (A → B)
- **Undirected**: Edges go both ways (A ↔ B)
- **Weighted**: Edges have associated values
- **Cyclic/Acyclic**:  Whether paths can loop back to themselves

---

# Part 2: Python's Data Model as a Graph

## Object References as a Graph

In Python, everything is an object, and variables are just **references** (pointers) to objects. 

```python
a = [1, 2, 3]
b = a  # b references the same object as a
```

**As a graph:**
```
   a ──────┐
           ▼
         [1, 2, 3]  (list object in memory)
           ▲
   b ──────┘
```

- **Nodes**: Variables (`a`, `b`) and the list object
- **Edges**: References pointing from names to objects

## Inheritance Hierarchy (Class Graph)

Python's class inheritance forms a **Directed Acyclic Graph (DAG)**:

```python
class Animal:  pass
class Mammal(Animal): pass
class Bird(Animal): pass
class Bat(Mammal): pass  # A mammal that flies
```

**As a graph:**
```
        object
           ▲
        Animal
        ▲    ▲
    Mammal   Bird
       ▲
      Bat
```

- **Nodes**: Classes
- **Edges**:  Inheritance relationships (child → parent)
- Python uses the **MRO (Method Resolution Order)** which is essentially a **topological sort** of this graph

## Attribute Lookup as Graph Traversal

When you access `obj.attribute`, Python traverses a graph: 

```
obj.__dict__  →  type(obj).__dict__  →  parent_class.__dict__  →  ...   →  object.__dict__
```

This is a **graph traversal** following the MRO path until the attribute is found. 

## Mutable Container Objects as Graphs

Nested data structures form natural graphs:

```python
data = {
    'users': [
        {'name': 'Alice', 'friends': [...]},
        {'name': 'Bob', 'friends':  [...]}
    ]
}
```

**As a graph:**
```
data (dict)
    │
    └──► 'users' ──► list
                      ├──► dict {'name': 'Alice', ... }
                      └──► dict {'name': 'Bob', ...}
```

## Circular References

Python allows **cyclic graphs** in its object model:

```python
a = []
a.append(a)  # a contains itself! 
```

**As a graph:**
```
a ──► [ ●─┐ ]
      ▲   │
      └───┘  (cycle!)
```

Python's garbage collector uses **cycle detection** (graph algorithms) to clean these up.

## Key Insights from This Perspective

| Python Concept | Graph Theory Concept |
|----------------|---------------------|
| Variable assignment | Creating an edge (reference) |
| Object identity (`is`) | Same node in the graph |
| Inheritance | DAG with topological ordering |
| Attribute lookup | Graph traversal (BFS/DFS along MRO) |
| Garbage collection | Finding unreachable nodes |
| Shallow vs deep copy | Copying edges vs.  copying subgraph |
| Circular references | Cycles in the graph |

---

# Part 3: Dunder Methods as Graph Operations

Dunder methods define how objects behave in Python's graph of operations.  Think of them as **edge transformers** and **node operators**.

## Object Lifecycle Methods:  Node Creation & Destruction

### `__new__` and `__init__`: Node Creation

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        # Creates the node in memory
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        # Initializes edges from the node
        self. value = value

obj = MyClass(42)
```

**Graph interpretation:**

```
PHASE 1: __new__ (Node Creation)         PHASE 2: __init__ (Edge Creation)

     ┌──────────────────┐                      ┌──────────────────┐
     │                  │                      │                  │
     │   MyClass        │                      │   MyClass        │
     │   (template)     │                      │   (template)     │
     │                  │                      │                  │
     └────────┬─────────┘                      └────────┬─────────┘
              │                                         │
              │ instantiate                             │ instance of
              ▼                                         ▼
     ┌──────────────────┐                      ┌──────────────────┐
     │                  │                      │                  │
     │   Empty Node     │        ───►          │   obj            │
     │   (no edges yet) │                      │     │            │
     │                  │                      │     └─► value ──► 42
     └──────────────────┘                      └──────────────────┘
```

### `__del__`: Node Destruction Callback

```python
class TrackedObject:
    instances = []  # Class-level edge to all instances
    
    def __init__(self, name):
        self.name = name
        TrackedObject.instances.append(self)  # Add edge
    
    def __del__(self):
        # Called when node is about to be removed
        print(f"Removing {self.name} from graph")
        TrackedObject.instances.remove(self)  # Remove edge
```

## Attribute Access Methods: Edge Operations

### `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`

```python
class DynamicGraph:
    def __init__(self):
        object.__setattr__(self, '_edges', {})
    
    def __getattribute__(self, name):
        # Intercepts ALL attribute access
        print(f"Traversing edge: {name}")
        return object.__getattribute__(self, name)
    
    def __getattr__(self, name):
        # Only called if edge doesn't exist
        print(f"Edge '{name}' not found, creating dynamic edge")
        return f"dynamic_{name}"
    
    def __setattr__(self, name, value):
        # Creating/updating an edge
        print(f"Creating edge: {name} ──► {value}")
        self._edges[name] = value
    
    def __delattr__(self, name):
        # Removing an edge
        print(f"Deleting edge: {name}")
        del self._edges[name]
```

**Graph operations visualization:**

```
__getattribute__('x')           __getattr__('x')
        │                               │
        ▼                               ▼
┌───────────────────┐           ┌───────────────────┐
│ Search for edge   │           │ Edge not found    │
│ 'x' in node       │   ───►    │ Create dynamic    │
│                   │  (if not  │ response          │
│ obj ──? ─► x       │   found)  │                   │
└───────────────────┘           └───────────────────┘

__setattr__('x', 10)            __delattr__('x')
        │                               │
        ▼                               ▼
┌───────────────────┐           ┌───────────────────┐
│ Create/update     │           │ Remove edge       │
│ edge 'x'          │           │ 'x' from node     │
│                   │           │                   │
│ obj ────► x ──► 10│           │ obj ──✗─► x       │
└───────────────────┘           └───────────────────┘
```

### The Complete Attribute Lookup Graph

```
                    obj. some_attr
                         │
                         ▼
        ┌────────────────────────────────────┐
        │  obj.__getattribute__('some_attr') │
        │  (ALWAYS called first)             │
        └────────────────────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │  Check:  Data descriptor in         │
        │  type(obj).__mro__?                 │
        └────────────────────────────────────┘
               │                    │
              YES                   NO
               │                    │
               ▼                    ▼
        ┌─────────────┐    ┌────────────���───────┐
        │ descriptor  │    │ Check:              │
        │ .__get__()  │    │ obj.__dict__       │
        └─────────────┘    └────────────────────┘
                                  │         │
                                FOUND    NOT FOUND
                                  │         │
                                  ▼         ▼
                           ┌──────────┐  ┌────────────────────┐
                           │ Return   │  │ Check: Non-data    │
                           │ value    │  │ descriptor in MRO?  │
                           └──────────┘  └────────────────────┘
                                               │         │
                                             FOUND    NOT FOUND
                                               │         │
                                               ▼         ▼
                                        ┌──────────┐  ┌──────────────┐
                                        │descriptor│  │ __getattr__  │
                                        │.__get__()│  │ (fallback)   │
                                        └──────────┘  └──────────────┘
```

## Container Methods: Subgraph Operations

### `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`

```python
class Graph:
    def __init__(self):
        self. nodes = {}
        self.edges = {}  # {from_node: {to_node: weight}}
    
    def __getitem__(self, key):
        """Traverse to a node"""
        if isinstance(key, tuple):
            from_node, to_node = key
            return self.edges[from_node][to_node]
        return self.nodes[key]
    
    def __setitem__(self, key, value):
        """Create node or edge"""
        if isinstance(key, tuple):
            from_node, to_node = key
            if from_node not in self.edges:
                self. edges[from_node] = {}
            self.edges[from_node][to_node] = value
        else:
            self.nodes[key] = value
    
    def __delitem__(self, key):
        """Remove node or edge"""
        if isinstance(key, tuple):
            from_node, to_node = key
            del self.edges[from_node][to_node]
        else:
            del self.nodes[key]
            self.edges.pop(key, None)
            for node in self.edges:
                self. edges[node].pop(key, None)
    
    def __contains__(self, key):
        """Check if node or edge exists"""
        if isinstance(key, tuple):
            from_node, to_node = key
            return from_node in self.edges and to_node in self. edges[from_node]
        return key in self.nodes

# Usage
g = Graph()
g['A'] = {'name': 'Alice'}  # Create node
g['B'] = {'name': 'Bob'}    # Create node
g['A', 'B'] = 5             # Create edge with weight
```

### `__iter__` and `__next__`: Graph Traversal

```python
class BFSIterator:
    """Breadth-First Search traversal of a graph"""
    
    def __init__(self, graph, start):
        self.graph = graph
        self.queue = [start]
        self.visited = set()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.queue:
            node = self. queue.pop(0)
            if node not in self.visited:
                self. visited.add(node)
                neighbors = self.graph. edges.get(node, {})
                self.queue.extend(neighbors.keys())
                return node
        raise StopIteration
```

## Operator Methods: Edge Transformations

### Arithmetic:  `__add__`, `__mul__`, etc.

```python
class Vector:
    def __init__(self, *components):
        self.components = list(components)
    
    def __add__(self, other):
        """Combine two vector nodes into a new node"""
        if isinstance(other, Vector):
            new_components = [a + b for a, b in 
                           zip(self.components, other.components)]
            return Vector(*new_components)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Transform node by scalar"""
        return Vector(*[c * scalar for c in self.components])
    
    def __rmul__(self, scalar):
        """Handle scalar * vector"""
        return self.__mul__(scalar)
```

**Graph of operations:**

```
v1 + v2 operation: 

    v1                v2
    │                 │
    │ (1,2,3)         │ (4,5,6)
    │                 │
    └────────┬────────┘
             │
             ▼ __add__
    ┌─────────────────┐
    │  Create new     │
    │  Vector node    │
    │  (5, 7, 9)      │
    └────────┬────────┘
             │
             ▼
            v3
```

## Context Managers:  Scoped Subgraphs

```python
class TransactionGraph:
    def __init__(self):
        self.committed_nodes = {}
        self.committed_edges = {}
        self._pending_nodes = None
        self._pending_edges = None
    
    def __enter__(self):
        """Create temporary subgraph for transaction"""
        self._pending_nodes = dict(self.committed_nodes)
        self._pending_edges = dict(self. committed_edges)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Commit or rollback subgraph"""
        if exc_type is None:
            self.committed_nodes = self._pending_nodes
            self.committed_edges = self._pending_edges
            print("Transaction committed")
        else:
            print(f"Transaction rolled back due to {exc_type.__name__}")
        
        self._pending_nodes = None
        self._pending_edges = None
        return False
```

## Descriptor Protocol: Computed Edges

```python
class CachedEdge:
    """A descriptor that caches computed values"""
    
    def __init__(self, func):
        self.func = func
        self. cache_name = f'_cached_{func.__name__}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        if not hasattr(obj, self.cache_name):
            value = self.func(obj)
            setattr(obj, self.cache_name, value)
        
        return getattr(obj, self.cache_name)
    
    def __set__(self, obj, value):
        setattr(obj, self.cache_name, value)
    
    def __delete__(self, obj):
        if hasattr(obj, self. cache_name):
            delattr(obj, self.cache_name)

class GraphNode:
    def __init__(self, neighbors):
        self.neighbors = neighbors
    
    @CachedEdge
    def degree(self):
        """Computed property:  number of edges"""
        print("Computing degree...")
        return len(self.neighbors)
```

## Special Method Lookup:  The Meta-Graph

Python has a special rule:  dunder methods are looked up on the **type**, not the instance. 

```python
class Sneaky:
    def __len__(self):
        return 10

obj = Sneaky()
obj.__len__ = lambda:  999  # Instance attribute

print(len(obj))        # 10, not 999! 
print(obj.__len__())   # 999 (direct call uses instance)
```

---

# Part 4: Async/Await as Coroutine Graphs

## The Event Loop:  A Task Scheduler Graph

```
                    ┌─────────────────────────────────────┐
                    │           EVENT LOOP                │
                    │                                     │
                    │  ┌─────────┐    ┌─────────┐        │
                    │  │ READY   │    │ WAITING │        │
                    │  │ QUEUE   │    │ QUEUE   │        │
                    │  │         │    │         │        │
                    │  │ Task A ─┼────►  Task B │        │
                    │  │ Task C  │    │  Task D │        │
                    │  └────┬────┘    └────┬────┘        │
                    │       │              │              │
                    │       ▼              ▼              │
                    │  ┌─────────────────────────┐       │
                    │  │    RUNNING (1 task)     │       │
                    │  │       Task A            │       │
                    │  └─────────────────────────┘       │
                    │                                     │
                    └─────────────────────────────────────┘
```

## Coroutines: Pausable Execution Nodes

```python
async def fetch_data(url):
    print(f"Starting fetch:  {url}")
    await asyncio.sleep(1)  # Suspension point
    print(f"Completed fetch: {url}")
    return f"data from {url}"

async def process():
    result = await fetch_data("http://example.com")
    return result. upper()
```

**Coroutine state graph:**

```
     CREATED ─────► RUNNING ─────► SUSPENDED ─────► RUNNING ─────► COMPLETED
        │              │               │               │               │
        ▼              ▼               ▼               ▼               ▼
    ┌────────┐    ┌────────┐      ┌────────┐      ┌────────┐     ┌────────┐
    │ coro   │    │ Exec   │      │ Waiting│      │ Resumed│     │ Return │
    │ object │    │ code   │      │ on I/O │      │ exec   │     │ value  │
    │ created│    │ until  │      │ or     │      │        │     │        │
    │        │    │ await  │      │ timer  │      │        │     │        │
    └────────┘    └────────┘      └────────┘      └────────┘     └────────┘
```

## The `await` Expression: Edge Between Coroutines

```python
async def parent():
    result = await child()  # Creates dependency edge
    return result + 1

async def child():
    await asyncio.sleep(0.1)
    return 42
```

**Dependency graph:**

```
         parent coroutine
               │
               │ await (blocked until child completes)
               ▼
         child coroutine
               │
               │ await (blocked until sleep completes)
               ▼
         asyncio.sleep(0.1)
               │
               ▼
          Timer fires
               │
               ▼
         child returns 42
               │
               ▼
         parent returns 43
```

## Concurrent Execution:  Parallel Subgraphs

```python
async def main():
    # Sequential (chain)
    a = await task_a()
    b = await task_b()
    
    # Concurrent (parallel branches)
    c, d = await asyncio.gather(task_c(), task_d())
    
    # Concurrent with first-wins
    done, pending = await asyncio.wait(
        [task_e(), task_f()],
        return_when=asyncio. FIRST_COMPLETED
    )
```

**Execution graph comparison:**

```
SEQUENTIAL:                      CONCURRENT (gather):

    main                              main
      │                                 │
      ▼                                 ▼
   task_a                         ┌────┴────┐
      │                           │         │
      ▼                           ▼         ▼
   task_b                      task_c    task_d
      │                           │         │
      ▼                           └────┬────┘
   (done)                              ▼
                                   (both done)

Time: t_a + t_b                  Time: max(t_c, t_d)
```

## Async Iterators: Streaming Graphs

```python
class AsyncRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self. stop:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.1)
        value = self.current
        self.current += 1
        return value

async def consumer():
    async for value in AsyncRange(0, 5):
        print(value)
```

## Async Context Managers:  Scoped Async Subgraphs

```python
class AsyncConnection:
    def __init__(self, host):
        self.host = host
        self.connected = False
    
    async def __aenter__(self):
        print(f"Connecting to {self.host}...")
        await asyncio.sleep(0.5)
        self.connected = True
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Disconnecting...")
        await asyncio.sleep(0.2)
        self.connected = False
        return False

async def main():
    async with AsyncConnection("db.example.com") as conn:
        result = await conn.query("SELECT * FROM users")
```

## Task Cancellation: Pruning the Graph

```python
async def long_running():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Cleaning up...")
        raise

async def main():
    task = asyncio.create_task(long_running())
    await asyncio.sleep(2. 5)
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")
```

## Summary: Graph Concepts in Async Python

| Graph Concept | Async Application |
|---------------|-------------------|
| **Nodes** | Tasks, coroutines, futures |
| **Directed edges** | `await` dependencies |
| **Parallel branches** | `asyncio.gather()`, `asyncio.wait()` |
| **Node states** | PENDING, RUNNING, SUSPENDED, DONE, CANCELLED |
| **Graph traversal** | Event loop scheduling |
| **Subgraphs** | Async context managers (`async with`) |
| **Streaming nodes** | Async iterators (`async for`) |
| **Graph pruning** | Task cancellation |

---

# Part 5: Generators as Execution Graphs

## Generator Basics: Linear Execution Graphs

### Simple Generator:  A Chain of Nodes

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i  # Suspension point (node)
        i += 1
```

**Execution graph:**

```
count_up_to(3)

   START
     │
     ▼
┌─────────┐  next()  ┌─────────┐  next()  ┌─────────┐  next()  ┌─────────┐
│  i = 1  │ ───────► │ yield 1 │ ───────► │ yield 2 │ ───────► │ yield 3 │
└─────────┘          └─────────┘          └─────────┘          └─────────┘
                                                                     │
                                                                     ▼ next()
                                                               ┌───────────┐
                                                               │ StopIter  │
                                                               │ ation     │
                                                               └───────────┘
```

### Generator States

```python
def simple():
    yield 1
    yield 2

gen = simple()
print(gen.gi_frame)  # Frame exists (GEN_CREATED)
next(gen)            # Moves to first yield (GEN_SUSPENDED)
next(gen)            # Moves to second yield (GEN_SUSPENDED)
next(gen)            # StopIteration (GEN_CLOSED)
```

**State machine graph:**

```
    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
    │ GEN_CREATED │──next()─► GEN_RUNNING │─���yield──► GEN_SUSPENDED│
    │  (initial)  │         │ (executing) │         │ (paused)    │
    └─────────────┘         └──────┬──────┘         └─────────────┘
                                   │                       ▲
                                   │                       │
                                   │        next()         │
                                   │       ┌───────────────┘
                                   │       │
                                   │ return/exhausted
                                   ▼
                            ┌─────────────┐
                            │ GEN_CLOSED  │
                            │  (finished) │
                            └─────────────┘
```

## `yield` as a Bidirectional Edge

### `.send()`: Pushing Values Into the Generator

```python
def accumulator():
    total = 0
    while True:
        value = yield total  # Bidirectional:  outputs total, receives value
        if value is None: 
            break
        total += value

gen = accumulator()
next(gen)           # Prime the generator, get 0
gen.send(10)        # Send 10, get 10
gen.send(20)        # Send 20, get 30
gen. send(5)         # Send 5, get 35
```

## Generator Pipelines: Chained Graphs

```python
def read_lines(filename):
    """Source node:  produces raw lines"""
    with open(filename) as f:
        for line in f: 
            yield line. strip()

def filter_comments(lines):
    """Filter node: removes comments"""
    for line in lines:
        if not line.startswith('#'):
            yield line

def parse_numbers(lines):
    """Transform node: converts to integers"""
    for line in lines:
        try:
            yield int(line)
        except ValueError:
            pass

def sum_all(numbers):
    """Sink node: consumes and aggregates"""
    total = 0
    for num in numbers: 
        total += num
    return total

# Build the pipeline
lines = read_lines("data.txt")
filtered = filter_comments(lines)
numbers = parse_numbers(filtered)
result = sum_all(numbers)
```

**Pipeline graph:**

```
   data. txt
      │
      ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  read_lines  │──►│filter_comment│──►│parse_numbers │──►│   sum_all    │
│   SOURCE     │   │    FILTER    │   │  TRANSFORM   │   │     SINK     │
│ yields str   │   │ yields str   │   │ yields int   │   │ returns int  │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘

         LAZY:  No work done until sum_all pulls values through the chain
```

## `yield from`: Subgraph Delegation

```python
def leaf_a():
    yield 1
    yield 2

def leaf_b():
    yield 3
    yield 4

def tree():
    yield from leaf_a()  # Delegate to subgraph
    yield 'middle'
    yield from leaf_b()  # Delegate to another subgraph
```

**Graph with delegation:**

```
                              tree()
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
    ┌───────────────┐     ┌───────────┐     ┌───────────────┐
    │   leaf_a()    │     │  'middle' │     │   leaf_b()    │
    │ ┌───┐   ┌───┐ │     │  (direct  │     │ ┌───┐   ┌───┐ │
    │ │ 1 │──►│ 2 │ │     │   yield)  │     │ │ 3 │──►│ 4 │ │
    │ └───┘   └───┘ │     │           │     │ └───┘   └───┘ │
    └───────────────┘     └───────────┘     └───────────────┘
    
    Output sequence:  1 ──► 2 ──► 'middle' ──► 3 ──► 4
```

## Exception Handling in Generators:  Error Edges

### `.throw()`: Injecting Exceptions

```python
def resilient_generator():
    while True:
        try:
            value = yield "ready"
            yield f"processed: {value}"
        except ValueError as e:
            yield f"error handled: {e}"

gen = resilient_generator()
print(next(gen))                          # "ready"
print(gen.throw(ValueError, "bad input")) # "error handled:  bad input"
print(next(gen))                          # "ready" (continues!)
```

### `.close()`: Graceful Termination

```python
def managed_resource():
    print("Acquiring resource")
    try:
        while True:
            yield "data"
    except GeneratorExit: 
        print("Releasing resource")
    finally:
        print("Cleanup complete")

gen = managed_resource()
next(gen)      # "Acquiring resource", returns "data"
gen.close()    # Triggers GeneratorExit
# Prints: "Releasing resource"
# Prints:  "Cleanup complete"
```

## Recursive Generators: Tree Traversal Graphs

```python
class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self. children = children or []

def dfs_preorder(node):
    """Depth-first pre-order traversal"""
    yield node. value
    for child in node.children:
        yield from dfs_preorder(child)

def dfs_postorder(node):
    """Depth-first post-order traversal"""
    for child in node.children:
        yield from dfs_postorder(child)
    yield node.value

def bfs(node):
    """Breadth-first traversal"""
    queue = [node]
    while queue: 
        current = queue.pop(0)
        yield current. value
        queue.extend(current. children)
```

## Summary: Graph Concepts in Generators

| Graph Concept | Generator Application |
|---------------|----------------------|
| **Nodes** | Yield points (suspension states) |
| **Directed edges** | Execution flow between yields |
| **Bidirectional edges** | `send()` / `yield` value exchange |
| **Subgraph delegation** | `yield from` |
| **Lazy evaluation** | Pull-based computation |
| **Pipeline** | Chained generators |
| **State machine** | Generator with conditional yields |
| **Tree traversal** | Recursive generators |
| **Error edges** | `.throw()` exception injection |
| **Termination** | `.close()` and `GeneratorExit` |

---

# Part 6: Python's Import System as a Dependency Graph

## The Module Graph: Nodes and Edges

```python
# main.py
import json
import requests
from utils import helper

# utils/helper.py
import os
import json  # Same json as main.py! 
from .  import constants
```

**Module dependency graph:**

```
                                    main.py
                                       │
                    ┌──────────────────┼��─────────────────────┐
                    │                  │                      │
                    ▼                  ▼                      ▼
                  json               requests            utils. helper
                    ▲                  │                      │
                    │           ┌──────┴──────┐         ┌─────┴─────┐
                    │           ▼             ▼         ▼           ▼
                    │       urllib3      certifi       os     utils.constants
                    │           │                               │
                    │           ▼                               ▼
                    └───────  ssl                              sys
```

## `sys.modules`: The Module Cache Graph

```python
import sys

print(sys.modules['json'])      # <module 'json' from '...'>
print(sys.modules['requests'])  # <module 'requests' from '...'>
```

Key insight:  Importing the same module twice returns the SAME node!

```python
>>> import json
>>> import json as j
>>> json is j
True  # Same node in the graph
```

## Import Resolution:  Graph Traversal Algorithm

```
                              import foo. bar. baz
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │   1. Check sys.modules cache        │
                    │      'foo.bar.baz' in sys.modules?   │
                    └──────────────────┬──────────────────┘
                              │                 │
                            FOUND           NOT FOUND
                              │                 │
                              ▼                 ▼
                    ┌──────────────┐   ┌────────────────────────────┐
                    │ Return cached│   │ 2. Try each finder in      │
                    │ module       │   │    sys.meta_path           │
                    └──────────────┘   └─────────────┬──────────────┘
                                                     │
                         ┌───────────────────────────┼───────────────┐
                         │                           │               │
                         ▼                           ▼               ▼
                ┌─────────────────┐        ┌─────────────────┐  ┌─────────────┐
                │ BuiltinImporter │        │ FrozenImporter  │  │ PathFinder  │
                └─────────────────┘        └─────────────────┘  └─────────────┘
```

## Circular Imports: Cycles in the Dependency Graph

```python
# module_a.py
print("Loading module_a")
from module_b import func_b

def func_a():
    return "A"

# module_b.py
print("Loading module_b")
from module_a import func_a  # Circular! 

def func_b():
    return "B"
```

**Solutions:**

```python
# Solution 1: Import at function level (lazy edge creation)
def func_a():
    from module_b import func_b
    return func_b() + " from A"

# Solution 2: Import the module, not the attribute
import module_b

def func_a():
    return module_b.func_b()

# Solution 3: Restructure to break the cycle
# common.py - shared functionality
# module_a.py - imports common
# module_b.py - imports common
```

## Import Hooks: Custom Graph Edges

```python
import sys
from importlib. abc import MetaPathFinder, Loader
from importlib.util import spec_from_loader

class VirtualModuleFinder(MetaPathFinder):
    """Creates modules that don't exist on disk"""
    
    VIRTUAL_MODULES = {
        'virtual. config': {'DEBUG': True, 'VERSION': '1.0'},
    }
    
    def find_spec(self, fullname, path, target=None):
        if fullname in self. VIRTUAL_MODULES: 
            return spec_from_loader(fullname, VirtualModuleLoader(fullname))
        return None

# Install the hook
sys.meta_path.insert(0, VirtualModuleFinder())

# Now we can import virtual modules! 
from virtual.config import DEBUG, VERSION
```

---

# Part 7: Decorators as Function Graph Transformers

## Basic Decorator: Node Wrapping

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# Equivalent to:  add = log_calls(add)
```

**Decorator transformation graph:**

```
BEFORE DECORATION                AFTER DECORATION

Global Namespace                 Global Namespace
      │                                │
      └──► 'add' ──► <function add>    └──► 'add' ──► <function wrapper>
                                                            │
                                                            └──► func ──► <original add>
```

## Decorator Stacking:  Layered Wrapping

```python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

# Equivalent to: greet = bold(italic(greet))
print(greet("World"))  # <b><i>Hello, World</i></b>
```

## `functools.wraps`: Preserving Node Metadata

```python
from functools import wraps

def log_calls(func):
    @wraps(func)  # Copies metadata from func to wrapper
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # 'add' (not 'wrapper')
print(add.__doc__)   # 'Add two numbers.'
```

## Decorators with Arguments: Factory Pattern

```python
def repeat(times):
    """Decorator factory that returns a decorator"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results. append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}"

# Equivalent to: greet = repeat(times=3)(greet)
```

## Class Decorators:  Transforming Class Nodes

```python
def singleton(cls):
    """Class decorator that ensures only one instance exists"""
    instances = {}
    
    @wraps(cls, updated=[])
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        print(f"Connecting to {host}")

db1 = DatabaseConnection("localhost")  # Prints "Connecting..."
db2 = DatabaseConnection("otherhost")  # No print! 
print(db1 is db2)  # True
```

---

# Part 8: Garbage Collection and Cycle Detection

## Reference Counting: Edge Counting

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (a + getrefcount's reference)

b = a
print(sys.getrefcount(a))  # 3

del b
print(sys.getrefcount(a))  # 2
```

**When refcount = 0: Object is immediately deallocated! **

## The Problem: Reference Cycles

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

a = Node("A")
b = Node("B")
a.ref = b
b.ref = a

del a, b  # Both still have refcount=1 due to cycle! 
```

## Generational Garbage Collection

```python
import gc

print(gc.get_threshold())  # (700, 10, 10)

# Generation 0: New objects (collected most frequently)
# Generation 1: Survived one collection
# Generation 2: Long-lived objects (collected least frequently)
```

**Generational GC graph:**

```
                              NEW OBJECTS
                                   │
                                   ▼
    ┌──────────────────────────────────────────────────────────────────────────┐
    │                        GENERATION 0                                       │
    │   Most objects die young!  Collected when:  700 allocations                │
    └──────────────────────────────────────────────────────────────────────────┘
                                   │ (survivors promoted)
                                   ▼
    ┌──────────────────────────────────────────────────────────────────────────┐
    │                        GENERATION 1                                       │
    │   Objects that survived one collection                                   │
    └──────────────────────────────────────────────────────────────────────────┘
                                   │ (survivors promoted)
                                   ▼
    ┌──────────────────────────────────────────────────────────────────────────┐
    │                        GENERATION 2                                       │
    │   Long-lived objects (modules, classes, cached data)                     │
    └──────────────────────────────────────────────────────────────────────────┘
```

## Cycle Detection Algorithm:  Tri-Color Marking

```
INITIAL: All objects WHITE (unvisited)

    ROOTS ──► A ──► B ──► C     D ◄───► E (orphaned cycle)
              WHITE   WHITE   WHITE   WHITE   WHITE

STEP 1: Mark reachable from roots as GREY

    ROOTS ──► A ──► B ──► C     D ◄───► E
              GREY   WHITE  WHITE   WHITE   WHITE

STEP 2: Process GREY, mark children GREY, self BLACK

    ROOTS ──► A ──► B ──► C     D ◄───► E
              BLACK  GREY  WHITE   WHITE   WHITE

FINAL: WHITE objects are garbage

    ROOTS ──► A ──► B ──► C     D ◄───► E
              BLACK  BLACK BLACK   WHITE   WHITE
                                   ▲
                                   │
                              GARBAGE! 
```

## Weak References: Non-Counting Edges

```python
import weakref

class ExpensiveObject: 
    def __init__(self, name):
        self.name = name

obj = ExpensiveObject("Important")
weak_ref = weakref.ref(obj)  # Doesn't prevent collection

print(weak_ref())  # <ExpensiveObject object>

del obj  # Object is collected

print(weak_ref())  # None
```

## Debugging Memory Leaks

```python
import gc

def find_cycles():
    gc.collect()
    gc.set_debug(gc. DEBUG_SAVEALL)
    gc.collect()
    
    print(f"Uncollectable objects: {len(gc.garbage)}")
    for obj in gc.garbage:
        print(f"  {type(obj).__name__}: {obj! r:. 50}")

# Find who references an object
referrers = gc. get_referrers(suspicious_object)

# Find what an object references
referents = gc.get_referents(suspicious_object)
```

---

# Part 9: Conclusion - Python as a Living Graph

## The Unified Python Object Graph

Every running Python program is a single, interconnected graph: 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE COMPLETE PYTHON RUNTIME GRAPH                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  TYPE LAYER:      type ◄═══► object                                         │
│                      ▲                                                       │
│                      │ (inherits)                                           │
│                   int, str, list, User Classes...                            │
│                                                                              │
│  OBJECT LAYER:   obj_a ──► obj_b ──► obj_c ◄── obj_d                        │
│                                                                              │
│  NAMESPACE LAYER: builtins ──► globals ──► enclosing ──► locals             │
│                                                                              │
│  MODULE LAYER:   sys. modules:  'os', 'sys', 'json', 'myapp'...                │
│                                                                              │
│  EXECUTION LAYER: Call Stack, Generators, Async Tasks                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Seven Fundamental Graph Operations

| Python Operation | Graph Operation | Example |
|------------------|-----------------|---------|
| `a = value` | Create Edge | name 'a' ──► object |
| `del a` | Remove Edge | name 'a' ──✗──► object |
| `a.attr` | Traverse Edge | a ──► __dict__ ──► 'attr' ──► val |
| `class C(A, B)` | DAG Construction | C ──► A ──► object |
| `C.method()` | Graph Search | MRO traversal (topological order) |
| `import module` | Lazy Node Loading | Add node to sys.modules |
| `gc.collect()` | Find Unreachable | Mark-and-sweep from roots |

## Graph Invariants Python Maintains

1. **TYPE GRAPH**: Always a DAG (no inheritance cycles)
2. **MODULE GRAPH**: DAG preferred, cycles handled specially
3. **REFERENCE GRAPH**: Arbitrary (cycles allowed, GC handles them)
4. **NAMESPACE GRAPH**: Strictly layered (LEGB)
5. **ASYNC TASK GRAPH**: No await cycles (deadlock prevention)

## Graph Algorithms Hidden in Python

| Algorithm | Python Application |
|-----------|-------------------|
| C3 Linearization | Method Resolution Order (MRO) |
| Mark and Sweep | Garbage Collection |
| Depth-First Search | Import Resolution |
| Breadth-First Search | Attribute Lookup |
| Cycle Detection | repr() and pickle |

## Practical Mental Models

### 1. ASSIGNMENT = EDGE CREATION
```python
a = [1, 2, 3]     # a ──► [1, 2, 3]
b = a             # b ──► [1, 2, 3] (same object!)
b. append(4)       # Both see the change
```

### 2. OBJECTS EXIST INDEPENDENTLY OF NAMES
```python
def make_list():
    x = [1, 2, 3]  # x is local edge
    return x       # return creates new edge from caller

result = make_list()  # x is gone, but object survives
```

### 3. INHERITANCE = PATH IN DAG
```python
obj. method()
# Search:  type(obj) ──► parent ──► grandparent ──► object
```

### 4. CLOSURES = CAPTURED EDGES
```python
def outer(x):
    def inner():
        return x  # inner holds edge to x's value
    return inner

f = outer(10)  # f holds edge to 10
```

### 5. DECORATORS = EDGE REDIRECTION
```
BEFORE: 'func' ──► original function
AFTER:  'func' ──► wrapper ──► original function
```

### 6. GENERATORS = PAUSABLE GRAPH TRAVERSAL
```
START ──► yield 1 ──► yield 2 ──► END
             │            │
          (pause)      (pause)
```

### 7. ASYNC = TASK DEPENDENCY GRAPH
```
main ──► fetch ──► process
         await      await
```

## Graph Theory Toolkit Summary

| Graph Concept | Python Applications |
|---------------|---------------------|
| Nodes | Objects, modules, classes, frames, tasks |
| Edges | References, imports, inheritance, await |
| Directed | References (a → obj), inheritance (child → parent) |
| In-degree | Reference count (for GC) |
| DAG | Inheritance hierarchy, import graph |
| Cycle | Circular references, circular imports |
| Topological Sort | MRO (C3 linearization) |
| Reachability | Garbage collection, closure capture |
| Tree | Call stack, AST, nested data structures |
| Subgraph | Namespaces, packages, async context |
| Traversal (DFS) | Deep copy, import resolution |
| Traversal (BFS) | Attribute lookup |
| Weak Edges | weakref (don't prevent GC) |

## Key Takeaways

1. **EVERYTHING IN PYTHON IS A NODE IN A GRAPH**
   Objects, classes, modules, frames, tasks — all nodes. 

2. **EVERY RELATIONSHIP IS AN EDGE**
   References, inheritance, imports, closures — all edges. 

3. **PYTHON OPERATIONS ARE GRAPH OPERATIONS**
   Assignment = edge creation, del = edge removal, attribute access = edge traversal.

4. **GRAPH INVARIANTS EXPLAIN PYTHON'S RULES**
   No inheritance cycles (DAG), MRO is topological sort, GC finds unreachable nodes.

5. **THIS MENTAL MODEL HELPS YOU:**
   - Debug reference issues (trace the edges)
   - Understand mutability (shared nodes)
   - Design better code (minimize unnecessary edges)
   - Optimize memory (break cycles, use weak refs)
   - Reason about concurrency (task dependency graphs)

---

## Final Thought

The graph-theoretic view of Python reveals an elegant truth: **Python's simplicity at the surface hides sophisticated graph algorithms underneath**. 

When you write: 

```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

buddy = Dog()
buddy.speak()
```

You're actually: 
1. **Constructing a DAG** (Dog → Animal → object)
2. **Performing a topological sort** (computing MRO)
3. **Traversing the graph** (method lookup)
4. **Managing reference counts** (keeping buddy alive)

Understanding Python through graph theory transforms you from someone who *uses* Python to someone who truly *understands* it. 

---

*Document generated from a comprehensive discussion about Python's data model through the lens of Graph Theory.*