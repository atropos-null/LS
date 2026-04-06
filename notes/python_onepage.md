## Python Execution — One Page Hierarchy

SOURCE (text)  
|  
+-- Lexing -> tokens  
+-- Parsing -> parse tree  
+-- AST -> structural graph (program meaning)  
|  
+-- Symbol Table -> scope graph (who owns each name)  
|  
+-- Control Flow Graph -> possible execution paths  
|  
+-- COMPILATION  
    |  
    +-- Code Objects (blueprints)  
        +-- co_code (bytecode)  
        +-- co_consts / co_names  
        +-- co_varnames / freevars / cellvars  
        +-- metadata  

==================================================  

RUNTIME INITIALIZATION (C level)  
|  
+-- Interpreter State (global world)  
|   +-- modules  
|   +-- builtins  
|   +-- sys / import system  
|   +-- shared runtime state  
|  
+-- Thread State (per executing thread)  
|   +-- current frame pointer  
|   +-- exception state  
|   +-- recursion depth  
|   +-- tracing / profiling  
|  
+-- GIL (execution permission)  
    +-- only one thread executes bytecode at a time  

==================================================  

EXECUTION ENTRY (static -> dynamic bridge)  
|  
+-- _PyEval_EvalCodeWithName  
    +-- takes code object + args + globals + locals  
    +-- resolves arguments  
    +-- builds frame  
    +-- populates fastlocals  
    +-- calls -> PyEval_EvalFrameEx(frame)  

==================================================  

FRAME (execution context)  
|  
+-- code object reference  
+-- value stack  
+-- fastlocals (indexed locals)  
+-- globals / builtins  
+-- instruction pointer (next_instr)  
+-- link to previous frame  

==================================================  

EVALUATION LOOP (PyEval_EvalFrameEx)  
|  
+-- for (;;)  
    |  
    +-- FULL ENTRY  
    |   +-- GIL check  
    |   +-- signal handling  
    |   +-- tracing hooks  
    |  
    +-- FAST ENTRY (skips checks)  
    |  
    +-- FETCH  
    |   +-- opcode + oparg from next_instr  
    |  
    +-- EXECUTE (switch on opcode)  
    |   |  
    |   +-- MECHANICAL OPS (no type dispatch)  
    |   |   +-- LOAD_CONST  
    |   |   +-- LOAD_FAST / STORE_FAST  
    |   |   +-- POP_TOP  
    |   |   +-- JUMP*  
    |   |   +-- stack ops (PUSH / POP)  
    |   |  
    |   +-- SEMANTIC OPS (require meaning)  
    |       +-- BINARY_OP / COMPARE_OP  
    |       +-- CALL_FUNCTION  
    |       +-- LOAD_ATTR  
    |       +-- CONTAINS_OP  
    |       +-- ITERATION  
    |  
    |       -> abstract.c (protocol mediator)  
    |           -> PyObject*  
    |               -> object -> type  
    |                   -> protocol table  
    |                       -> slot (function pointer)  
    |                           -> C implementation  
    |                               -> result PyObject*  
    |  
    |       +-- result pushed to stack  
    |  
    +-- CONTINUE CONTROL  
    |   +-- DISPATCH -> full loop (with checks)  
    |   +-- FAST_DISPATCH -> skip checks  
    |  
    +-- EXIT CONDITIONS  
        +-- WHY_RETURN  
        +-- WHY_EXCEPTION  
        +-- WHY_BREAK / WHY_CONTINUE  
        +-- frame ends  

==================================================  

EXCEPTION HANDLING (parallel control flow)  

Thread State holds:  
+-- curexc_type / value / traceback  
+-- exc_type / value / traceback  

When error occurs:  
+-- set exception  
+-- jump to error path  

Then:  
+-- UNWIND_BLOCK  
|   +-- pop stack entries  
|   +-- unwind control blocks  
|  
+-- UNWIND_EXCEPT_HANDLER  
|   +-- find matching except block  
|   +-- bind exception to locals  
|   +-- resume execution  
|  
+-- If handled:  
|   +-- continue eval loop  
|  
+-- If not handled:  
    +-- propagate to previous frame  
    +-- repeat upward  
    +-- if top-level: program exits  

==================================================  

RETURN PATH  

Frame finishes  
-> retval set  
-> return to caller frame  
-> resume caller eval loop  
-> continue upward until top-level  