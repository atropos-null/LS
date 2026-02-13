# Accessibility-Oriented Learning Scaffolds

A learning interface for people whose minds are routinely bruised by systems that assume implicit inference, speed under novelty, and silent pattern synthesis.

## Step 1: Load your learner profile

I am an adult, neurodivergent learner with strong abstract reasoning skills. I’m capable of deep understanding, but I require explicit structure before variation.

I do not reliably infer hidden assumptions from examples alone. I need:
* a clear introductory framing (what problem this exists to solve)
* the textbook/core model (the canonical version: clean, boring, correct)
* and only then deliberate expansion into edge cases, composition, and adversarial patterns.

I learn best when concepts are presented in layers, in this order:
1.	Core responsibility and invariant
2.	Canonical usage (“textbook” case)
3.	Axes of surprise (ways the invariant gets stressed)
4.	Compositional traps (when combined with other abstractions)

I struggle specifically with implicit contracts, hidden assumptions, and unspoken conventions. Once named, I retain them permanently and can apply them flexibly. My pain point is novel pattern synthesis under time pressure, not comprehension.

Important constraint: Use only contracts/enforcement that Python actually imposes (e.g., TypeError, AttributeError, protocol expectations). Do not invent style constraints (e.g., “shouldn’t include newlines”) unless explicitly stated as a design requirement.

#### Short Version (When You Want Less Ceremony)

I’m an advanced, neurodivergent learner who understands complex material deeply once implicit structures are named.
I need top-down, architectural explanations that surface hidden contracts, responsibility boundaries, and failure modes.
Please skip beginner explanations and focus on why this exists, who stays ignorant, and what breaks when assumptions are violated. Answer this at the architectural / moral level, not the tutorial level.

Or, even sharper:

Assume I understand the mechanics; explain the hidden contract. I learn by explicit pattern naming and invariant extraction, not by discovery or repetition. Once the invariant is stated, I integrate quickly and permanently.

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

## Step 2: The 10 Prompts

Paste these in directly. 

### Pass 0: Canonical Model (MANDATORY)

Before listing edge cases or idioms, explain {INSERT TOPIC} as it would appear in a clean textbook:
* What problem does it solve?
* What responsibility does it have?
* What invariant must always hold?

Keep this short, boring, and canonical.

### Pass 1:

List 5 **non-obvious Python idioms**  related to {INSERT TOPIC} that a prepared student might NOT expect. Focus on edge-case examples, not canonical textbook examples. For each, showing minimal code snippets:

* List the implicit assumptions the student must notice to proceed.
* Explain what a student often overlooks 
* Explain what misconception or misuse exposes
* Explain why it might look correct at first glance
* Clarify the correct interpretation

### Pass 2:

What happens when this concept is embedded inside another abstraction? Show me how {INSERT TOPIC} behaves when it is not the main actor, but a collaborator inside another object.

Specifically:
* place {INSERT TOPIC} inside a container, coordinator, or higher-level abstraction
* show how responsibility is delegated through it
* identify what additional assumptions are silently introduced
* demonstrate one case where everything works
* and one case where a reasonable implementation fails because the collaborator does not meet a second-order expectation. 

Show how to correct the problem. 

Focus on composition, not usage. 

Show code snippets for each.

### Pass 3:

How might this {INSERT TOPIC} appear in an assessment? Keep examples small. 
* Focus on assessment-style edge-case examples,
* Include at least 2 cases where Python’s behavior is counterintuitive or non-obvious
* Briefly state common incorrect assumptions.

### Pass 4:

Based on our discussion, what are 3 idiomatic micro-patterns exist within {INSERT TOPIC}?  Return them in this format:
* Name
* Trigger
* Hidden assumption
* Minimal sketch (≤ 8 lines)

### Pass 5:

Are there more idiomatic patterns that I should know about with regards to {INSERT TOPIC}, especially for Launch School assessment? Use the same Name / Trigger / Hidden assumption / Minimal sketch format.

### Pass 6:

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

Limit to 5–7 bridges.

Prefer patterns that appear in assessments or interviews, not library trivia.

End by summarizing: “If you can recognize these shapes, you can move again.”

#### Abridged Version:

I understand {INSERT TOPIC}, but I freeze during implementation. List 5 bridge patterns in Python related to {INSERT TOPIC} that:
* collapse many choices into one idiomatic move
* commonly appear in assessments

For each, give:
* Trigger phrase
* Input → output shape
* Canonical Python expression (≤1 line)

### You might have to push back at the AI

That’s surface-level. I want the architectural reason this exists.

Re-explain this entirely from the perspective of the blind caller. Do not mention humans, users, or presentation.

How is this concept commonly tested in assessments by violating the contract subtly rather than obviously?

Describe two traps that rely on reasonable but incorrect assumptions.

Who should not know about {INSERT TOPIC} if the design is correct?

What is the hidden contract behind {INSERT TOPIC}, and who relies on it staying invisible?

### Step 3: Did I get the information I need?

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



## TLDR

Explain the following Python topics to me morally, not rigorously. Tell me the story of why it exists, what pain it solves, and what the ‘moral of the story’ is in one sentence. Then give me the simplest example that demonstrates the moral, and one counterexample where naive intuition fails. After the counterexamples, explicitly state the invariant that all valid uses obey and all failures violate.

For {TOPIC}, generate 3 advanced Launch-School–style assessment prompts starting at {EXAM NUMBER}:
	1.	Predict & explain a short code snippet’s output
	2.	Debug a short snippet (state intended behavior)
	3.	Implement a small function or class with 3 I/O examples

Avoid canonical examples; prefer composition or object collaboration contexts.

Name the hidden trap each prompt is targeting.

Keep each under ~25 lines. No solutions or hints. At least one prompt must rely on a reasonable but incorrect assumption about a protocol or operator.