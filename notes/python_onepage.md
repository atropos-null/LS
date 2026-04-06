
## PYTHON EXECUTION — ONE PAGE HIERARCHY


SOURCE (text)

│ 
├── Lexing → tokens  
├── Parsing → parse tree 
├── AST → structural graph (program meaning)  
│ 
├── Symbol Table → scope graph (who owns each name)    
│  
├── Control Flow Graph → possible execution paths
│
└── COMPILATION
    └── Code Objects (blueprints)
         ├── co_code (bytecode)
         ├── co_consts / co_names
         ├── co_varnames / freevars / cellvars
         └── metadata

══════════════════════════════════════════════

RUNTIME INITIALIZATION (C level)
│
├── Interpreter State (global world)
│     ├── modules
│     ├── builtins
│     ├── sys / import system
│     └── shared runtime state
│
├── Thread State (per executing thread)
│     ├── current frame pointer
│     ├── exception state
│     ├── recursion depth
│     └── tracing/profiling
│
└── GIL (execution permission)
      └── only one thread executes bytecode at a time

══════════════════════════════════════════════

EXECUTION ENTRY (bridge from static → dynamic)
│
└── _PyEval_EvalCodeWithName
      ├── takes code object + args + globals + locals
      ├── resolves arguments
      ├── builds frame
      ├── populates fastlocals
      └── hands off →
            PyEval_EvalFrameEx(frame)

══════════════════════════════════════════════

FRAME (execution context)
│
├── code object reference
├── value stack
├── fastlocals (indexed locals)
├── globals / builtins
├── instruction pointer (next_instr)
└── link to previous frame

══════════════════════════════════════════════

EVALUATION LOOP (PyEval_EvalFrameEx)
│
└── for(;;)  ← infinite loop
     │
     ├── [FULL ENTRY]
     │     ├── GIL check
     │     ├── signal handling
     │     └── tracing hooks
     │
     ├── [FAST ENTRY] (skips above)
     │
     ├── FETCH
     │     └── opcode + oparg from next_instr
     │
     ├── EXECUTE (switch on opcode)
     │
     │    ├── MECHANICAL OPS (no meaning)
     │    │     ├── LOAD_CONST
     │    │     ├── LOAD_FAST / STORE_FAST
     │    │     ├── POP_TOP
     │    │     ├── JUMP*
     │    │     └── stack ops (PUSH / POP)
     │    │
     │    └── SEMANTIC OPS (require meaning)
     │          ├── BINARY_OP / COMPARE_OP
     │          ├── CALL_FUNCTION
     │          ├── LOAD_ATTR
     │          ├── CONTAINS_OP
     │          └── ITERATION
     │
     │          ↓
     │      abstract.c (protocol mediator)
     │          ↓
     │      PyObject*
     │          ↓
     │      object → type
     │          ↓
     │      protocol table (tp_as_number, etc.)
     │          ↓
     │      slot (function pointer)
     │          ↓
     │      C implementation
     │          ↓
     │      result PyObject*
     │
     │    └── result pushed back to stack
     │
     ├── CONTINUE CONTROL
     │     ├── DISPATCH → full loop (with checks)
     │     └── FAST_DISPATCH → skip checks
     │
     └── EXIT CONDITIONS
           ├── WHY_RETURN
           ├── WHY_EXCEPTION
           ├── WHY_BREAK / WHY_CONTINUE (internal control)
           └── frame ends

══════════════════════════════════════════════

## ⚠️ EXCEPTION HANDLING (parallel control system)

Exception state lives in:
    Thread State:
        ├── curexc_type / value / traceback
        └── exc_type / value / traceback

During eval loop:

┌──────────────────────────────────────────┐
│ If error occurs (e.g. slot fails, lookup fails): │
│     → set exception in thread state            │
│     → jump to "error" label                    │
└──────────────────────────────────────────┘

Then:

├── UNWIND_BLOCK
│     ├── pop stack entries
│     ├── unwind control blocks
│
├── UNWIND_EXCEPT_HANDLER
│     ├── locate matching except block
│     ├── bind exception to local variables
│     └── resume execution inside handler
│
├── If handler found:
│     → continue eval loop (normal execution resumes)
│
└── If no handler:
      → propagate exception upward
      → previous frame resumes and handles
      → if top-level: program terminates


══════════════════════════════════════════════

RETURN PATH

Frame finishes →
    retval set →
        return to caller frame →
            resume its eval loop →
                continue upward until top-level