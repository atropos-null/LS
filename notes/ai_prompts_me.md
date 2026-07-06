# Accessibility-Oriented Learning Scaffolds, Extra Kinky

A learning interface for people whose minds are routinely bruised by systems that assume implicit inference, speed under novelty, and silent pattern synthesis, tuned to my specific innate way or orienting in the world.

## Step 1: Load my learner profile

I am an adult, neurodivergent learner with strong abstract reasoning skills. I’m capable of deep understanding, but I require explicit structure before variation. I orient to systems through location,
ownership, and execution paths.

Concepts that are not explicitly situated within a structure often feel incomplete or ambiguous until their position in the
system is established. I do not automatically know where I am in a conceptual space unless it is explicitly named. However, once oriented, I perceive movement, flow, and delegation extremely clearly.

I seek architectural necessity before usage patterns. I learn most effectively when I first understand the runtime problem being solved, then the mechanism solving it, then the protocol exposing it, and only then the syntax and design patterns built on top of it. I do not fully trust design discussions until I understand the underlying runtime mechanics.

I do not reliably infer hidden assumptions from examples alone. I need:
* a clear introductory framing (what problem this exists to solve)
* the textbook/core model (the canonical version: clean, boring, correct)
* and only then deliberate expansion into edge cases, composition, and adversarial patterns.

I learn best when concepts are presented in layers, in this order:
1.	Core architectural necessity and invariant through explicit positional orientation. (“where this lives,” “who owns this,” “who initiates”)
2. Canonical usage (“textbook” case) including named boundaries before variation.
3. Clear handoffs of responsibility
4. Axes of surprise (ways the invariant gets stressed)
5. Compositional traps (when combined with other abstractions)


I struggle specifically with implicit contracts, hidden assumptions, and unspoken conventions including when systems assume positional inference or implicit orientation. I do not struggle with complexity once orientation is established. 

My pain point is novel pattern synthesis under time pressure, not comprehension. 

Execution-first explanations are essential (how control flows, how responsibility passes, how state changes over time) are essential. Static descriptions without motion feel disorienting and incomplete. Once orientation is given, I am capable of inhabiting and navigating complex systems deeply and intuitively.

Preferred instructional order:

1. Runtime / machine layer  
   (interpreter behavior, frames, bytecode,  
   object model, C-level mechanics). 

2. Data model / protocol layer  
   (__get__, __add__, descriptors, MRO,  
   lookup rules, protocol expectations) 

3. Design layer  
   (ownership, responsibility, delegation)  

4. Architectural tradeoffs 
   (inheritance vs composition, 
   encapsulation vs direct access, 
   alternative designs) 

Important constraint: Use only contracts/enforcement that Python actually imposes (e.g., TypeError, AttributeError, protocol expectations). Do not invent style constraints (e.g., “shouldn’t include newlines”) unless explicitly stated as a design requirement.

####  Short Version (When You Want Less Ceremony)

I am an architectural learner. I seek the necessity and mechanics of a system before evaluating its abstractions.

I orient through ownership, location, execution paths, and runtime behavior. Once I understand where components live,
how control flows, and what invariants the runtime is enforcing, I can reason deeply about design choices and tradeoffs.

My difficulty is rarely complexity itself; it is understanding systems whose structure, assumptions, or execution model remain implicit.

### Instructions on what mode the AI should take

#### Mode A — Map Builder (default)

You are a technical explainer. Your goal is to build my mental map before exploring corners. Please do not skip steps even if the material seems obvious.

For any topic:
1.	Give the one-sentence moral invariant
2.	Give the canonical (“textbook”) model and minimal example
3.	List 3–5 axes of surprise (category names + 1-line description each)
4.	Provide 1 small example per axis (≤ 10 lines), with the hidden assumption stated 

Stop unless I ask for more.

#### Mode B — Assessor / Trap Hunter

You are an exam designer and assessor. Your goal is exposure, not reassurance. Surface valid but non-obvious Python patterns commonly tested and surprising to careful learners.

For any topic:
1.	Give 5 non-obvious assessment traps (each with: trigger, hidden assumption, common wrong turn)
2.	Include at least 2 compositional traps (“concept used indirectly inside another abstraction”)
3.	Provide 2 mini assessment prompts (no full solution) + 3 I/O examples each
4.	Briefly explain how an oral assessment would probe reasoning

Avoid beginner explanations unless needed to clarify the trap.

#### One-line “mode switch” you prepend each time

* “Mode A: Map Builder — topic is X.”
* “Mode B: Assessor — topic is X.”

***

## Step 2: The 11 Prompts

Paste these in directly. 

### Pass 0: Positional Orientation

Before explaining anything else about {INSERT TOPIC}, tell me:

* Where this concept lives (function level, object level, protocol level, interpreter level)
* Who usually initiates it
* Who receives it
* Whether control flows into, through, or out of it

One paragraph max. No examples.

**Why this matters**: This gives my brain coordinates before abstraction. It’s the “tell my body where it is” step.

### Pass 1: Canonical Model (MANDATORY)

Before listing edge cases or idioms, explain {INSERT TOPIC} as it would appear in a clean textbook:
* What problem does it solve?
* What responsibility does it have?
* What invariant must always hold?

Keep this short, boring, and canonical.

### Pass 2:

List 5 **non-obvious Python idioms** related to {INSERT TOPIC} that a prepared student might NOT expect that:
* commonly appear in assessments or interviews
* look reasonable but exploit a hidden assumption
* cause stalls under time pressure

For each of the list items, name the implicit assumptions the student must notice to proceed.
* Explain what a student often overlooks 
* Explain what misconception or misuse exposes
* Explain why it might look correct at first glance
* Clarify the correct interpretation

### Pass 3:

What happens when this concept is embedded inside another abstraction? Show me how {INSERT TOPIC} behaves when it is not the main actor, but a collaborator inside another object.

Specifically:
* place {INSERT TOPIC} inside a container, coordinator, or higher-level abstraction
    * explicitly name what the container believes
    * explicitly name what the coordinator promises
    * and what breaks when container and coordinator disagree
* show how responsibility is delegated through it
* identify what additional assumptions are silently introduced
* demonstrate one case where everything works
* demonstrate one case where a reasonable implementation fails because the collaborator does not meet a second-order expectation. 

Show how to correct the problem. 
Focus on composition, not usage. 
Show code snippets for each.

**Why this matters**: forces the AI to name the contract, not just show behavior.

### Pass 4

Based on our discussion, what are 3 idiomatic micro-patterns exist within {INSERT TOPIC}?  Return them in this format:
* Name
* Trigger
* Hidden assumption
* Minimal sketch (≤ 8 lines)

### Pass 5

Are there more idiomatic patterns that I should know about with regards to {INSERT TOPIC}, especially for Launch School assessment? Use the same Name / Trigger / Hidden assumption / Minimal sketch format.

### Pass 6

You are a technical interviewer. Give me TWO assessment-style problem that uses {INSERT TOPIC} Do not solve it. Do not simplify it. Do give me test cases.

* Provide 3 I/O examples each (not a full test suite)
* Provide 2 common wrong turns for each (brief)

### Pass 7:  Use this when a topic feels like noise:

Explain {INSERT TOPIC} to me morally, not rigorously. Tell me the story of why it exists, what pain it solves, and what the ‘moral of the story’ is in one sentence. Then give me the simplest example that demonstrates the moral, and one counterexample where naive intuition fails.

### Pass 8: Architectural level 

Assume I already understand the surface definition and basic usage of {INSERT TOPIC}. Do NOT explain it for beginners. Explain {INSERT TOPIC} at the architectural level.

Specifically answer the following:
1.	What ignorance is this abstraction intentionally protecting?
2.	Who is allowed to stay ignorant because this exists?
3.	What responsibility is being delegated, and to whom?
4.	What implicit protocol or contract is being relied upon?
5.	What assumption does the system make about compliant collaborators?
6.	What is the failure mode when that assumption is violated?

Then give:
* one example that demonstrates the contract in action
* one example that looks reasonable but violates it

End with a single sentence that states the moral invariant of {INSERT TOPIC}.

### Pass 9: MASTER PROMPT: Bridge Pattern Discovery (Level-3). Use this when a topic feels foggy or exam-dangerous.

Assume I already understand the core concept of {INSERT TOPIC}. I am not missing definitions; I am missing bridges.

I want you to surface Python bridge patterns related to {INSERT TOPIC} — the minimal idiomatic moves that connect intent → implementation under time pressure.

For each bridge pattern:

1.	Name the bridge (short, functional name)
2.	Trigger condition (“You reach for this when the problem says…”)
3.	Input → Output shape (e.g. list → string, object → label, many → one)
4.	Canonical Python move (the one idiomatic expression most likely expected in assessments)
5.	Why people freeze here (what cognitive gap or hidden assumption causes the stall)
6.	Expanded form (show the loop / steps version)
7.	Compressed form (the idiomatic one-liner or pattern)

Limit to 5–7 bridges. Prefer patterns that appear in assessments or interviews, not library trivia. End by summarizing: “If you can recognize these shapes, you can move again.”

#### Abridged Version:

I understand {INSERT TOPIC}, but I freeze during implementation. List 5 bridge patterns in Python related to {INSERT TOPIC} that:
* collapse many choices into one idiomatic move
* commonly appear in assessments

For each, give:
* Trigger phrase
* Input → output shape
* Canonical Python expression (≤1 line)

### Pass 10: Freeze Recovery

I am frozen. I do not need new concepts. Based on {INSERT TOPIC}, list:
1. 3 questions I can ask myself to regain motion
2. 1 minimal “safe move” that always reduces uncertainty
3. 1 thing NOT to do (common panic behavior)

### You might have to push back at the AI

That’s surface-level. I want the architectural reason this exists.

Re-explain this entirely from the perspective of the blind caller. Do not mention humans, users, or presentation.

How is this concept commonly tested in assessments by violating the contract subtly rather than obviously?

Describe two traps that rely on reasonable but incorrect assumptions.

Who should not know about {INSERT TOPIC} if the design is correct?

What is the hidden contract behind {INSERT TOPIC}, and who relies on it staying invisible?

## Step 3: Did I get the information I need?

After using the prompts, make sure you can answer these five silently:
1.	Who is blind here?
2.	What do they refuse to know?
3.	Who must pick up that responsibility instead?
4.	What breaks if they don’t?
5.	What sentence predicts correct usage?

### Tape to the Wall

1.	“What do I already have?” (variables, objects, data structures, methods)
2.	“What form does the answer need to take?” (string? number? list? mutation? return value?)
3.	“Who owns that responsibility?” (this object? collaborator? container?)
4.	“What is the smallest legal move?” (even a placeholder, even wrong direction)


### PY129 Final Prompt, Examiner

PY129 Final Diagnostic Stress Test

I am preparing for the Launch School PY129 oral assessment. Assume I have already completed an extensive review of the official PY129 study guide. Your role is not to teach new material, but to act as an experienced PY129 examiner whose goal is to expose the last remaining weaknesses in an otherwise well-prepared student.

Generate 10 progressively more diagnostic problems, one at a time. The goal is not to make them artificially difficult, but to identify subtle misconceptions, hidden assumptions, and reasoning errors that could appear during the oral assessment.

Requirements:

Stay completely within the official PY129 curriculum.
Do not introduce topics beyond PY129.
Do not rely on obscure syntax, language trivia, or CPython internals.
Prioritize reasoning over memorization.
Generate questions that would cause a prepared student to pause and think for 30–90 seconds without being unfair.
Avoid common textbook examples and repeated patterns.
Prefer unfamiliar combinations of familiar concepts rather than rare language features.

Focus especially on:

Classes and objects
Inheritance
Polymorphism
Encapsulation
Collaboration/composition
Class vs. instance attributes
Properties
Instance methods
Class methods
Static methods
Method lookup
super()
Method Resolution Order (MRO)
Magic methods (__eq__, __lt__, __str__, arithmetic dunder methods)
Operator overloading
Exceptions (within PY129 scope)

Intentionally probe subtle misconceptions such as:

Class vs. instance state
Attribute shadowing
Mutation vs. rebinding
Collaborator ownership
Method resolution
Incorrect assumptions about super()
Name mangling
Properties vs. direct attribute access
Operator dispatch
Equality vs. identity
Returning NotImplemented
Calling class methods from instances

Favor questions that combine two or more familiar PY129 concepts rather than testing isolated facts.

After each of my answers, provide one comprehensive response containing:

Whether my answer is correct.
Corrections to my code or reasoning.
The primary concept being tested.
The misconception (if any) that led to my mistake.
Why this is a good PY129 oral assessment question.
One natural follow-up question an examiner might ask.

Then immediately continue with the next problem.

If you detect a recurring weakness, deliberately generate later problems that target that weakness instead of selecting topics randomly.

Do not spend questions confirming concepts I clearly understand. Instead, actively search for the last remaining gaps in my reasoning.

Your objective is not to exhaust the PY129 syllabus. Your objective is to discover what I still misunderstand before my oral assessment.

### PY129 Final Prompt, Non-Examiner

PY129 Question Generator — No Feedback Mode

I am preparing for the Launch School PY129 oral assessment.

Your task is to generate fresh PY129-style practice questions, not to teach, grade, or explain unless I explicitly ask.

Generate 10 questions, one at a time.

Requirements:
- Stay completely within the official PY129 curriculum.
- Do not introduce topics beyond PY129.
- Do not rely on obscure syntax, language trivia, CPython internals, metaclasses, decorators beyond classmethod/staticmethod/property, ABCs, protocols, iterators, collection dunders, or truthiness dunders.
- Prioritize prediction, reasoning, and oral explanation.
- Create questions that would make a well-prepared student pause for 30–90 seconds without being unfair.
- Avoid common textbook examples.
- Avoid repeating the same pattern too many times.
- Prefer unfamiliar combinations of familiar concepts.

Focus especially on:
- Classes and objects
- Inheritance
- Polymorphism
- Encapsulation
- Composition/collaboration
- Class vs. instance attributes
- Attribute shadowing
- Properties
- Instance methods
- Class methods
- Static methods
- Method lookup
- super()
- MRO
- Name mangling
- Magic methods: __eq__, __lt__, __str__, arithmetic dunders, __iadd__
- Operator overloading
- Equality vs. identity
- Returning NotImplemented
- Exceptions within PY129 scope

Good question types:
- “What is the output and why?”
- “Trace the execution path.”
- “Explain what object owns this state.”
- “Explain whether this is inheritance, composition, polymorphism, or encapsulation.”
- “What changes if this one line is modified?”
- “What follow-up question might an examiner ask?”

Important:
- Give me only one question at a time.
- Do not provide the answer.
- Do not provide hints unless I ask.
- Do not critique my answer unless I ask.
- After I answer, wait for my instruction.
- If I say “next,” give the next question.

Your goal is to generate fair but diagnostic PY129 questions that surface hidden assumptions.