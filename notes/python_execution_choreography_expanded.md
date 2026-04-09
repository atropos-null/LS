# Python Execution — Choreography View (Expanded)

```text
[1] SOURCE
     |
     v
[2] COMPILATION
     |
     +--> tokens
     +--> AST
     +--> symbol table (scope + bindings)
     +--> control flow graph (implicit)
     +--> code object(s)
     |
     v
[3] CODE OBJECT (what exists before execution)
     |
     +--> co_code       (bytecode stream)
     +--> co_consts     (literals)
     +--> co_names      (global names)
     +--> co_varnames   (locals)
     +--> co_freevars / co_cellvars (closures)
     +--> flags (e.g. CO_GENERATOR)
     |
     v
[4] FRAME CREATED
     |
     +--> f_code        (code object)
     +--> f_locals      (local namespace)
     +--> f_globals     (global namespace)
     +--> f_builtins    (builtins)
     +--> f_valuestack  (DATA stack)
     +--> f_blockstack  (CONTROL stack)
     +--> f_lasti       (instruction pointer)
     +--> f_back        (previous frame)
     |
     v
[5] GENERATOR?
     |
     +--> YES --> wrap frame in generator --> RETURN (paused)
     |
     +--> NO
            |
            v
[6] ENTER EVAL LOOP
     |
     +--> (GIL check / signals / tracing)
     |
     v
+--------------------------------------------------+
| LOOP START                                       |
|                                                  |
|   [7] FETCH OPCODE                               |
|        |                                         |
|        v                                         |
|   [8] EXECUTE OPCODE -------------------------+  |
|        |                                      |  |
|        |   (A) MECHANICAL                     |  |
|        |       +--> LOAD/STORE                |  |
|        |       +--> PUSH / POP                |  |
|        |       +--> JUMP                      |  |
|        |       +--> SETUP_* (push block)      |  |
|        |                                      |  |
|        |   (B) SEMANTIC                       |  |
|        |       v                              |  |
|        |    [DESCEND]                         |  |
|        |       +--> abstract.c                |  |
|        |       +--> type → slot → C           |  |
|        |       +--> result OR NULL            |  |
|        |    [ASCEND]                          |  |
|        |       +--> push result              |  |
|        |       +--> OR set exception --------+  |
|        +----------------------------------------+
|                          |
|                          v
|                [9] CONTROL CHECK
|                          |
|        +-----------------+------------------+
|        |                                    |
|        | normal                             | interruption
|        |                                    |
|        v                                    v
|   [10] CONTINUE LOOP                 [11] WHY_* SET
|        |                                    |
|        |                                    v
|        |                            [12] UNWIND LOOP
|        |                                    |
|        |   BLOCK STACK (LIFO)                |
|        |     +--> pop block                 |
|        |     +--> restore value stack       |
|        |     +--> jump to handler           |
|        |         +--> FINALLY (always)      |
|        |         +--> EXCEPT (match?)       |
|        |         +--> LOOP (break/cont)     |
|        |     +--> repeat if needed          |
|        |     +--> no blocks → exit frame    |
|        |                                    |
|        |     [13] FRAME EXIT                |
|        |         +--> return to caller      |
|        |         +--> propagate exception   |
|        |         +--> or end program        |
|        +------------------------------------+
|
+--------------------------------------------------+

[14] FUNCTION CALL PATH
     +--> new frame → jump to [5]

[15] CLASS CREATION PATH
     +--> __build_class__ → execute body → metaclass → class

[16] GENERATOR PATH
     +--> resume → run → YIELD → pause → resume later
```

