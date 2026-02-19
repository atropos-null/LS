# A Lullaby

What I hum to myself when the noise rises. You can stop here and not read any further.

## The Lullaby

> I know what I have  
> Someone owns the next move  
> Something else can be ignored  
> One thing must be True

**I know what I have** -> inventory of what is present in the problem 

**Someone owns the next move**: what is the very next thing that has to be done. Only that very next thing. Which object owns it? 

**Something else can be ignored**: Only focus on the ONE thing. Tamp down the noise. Don't spiral.

**One thing must be True**: literally what has to be `True` for the thing to work.

***

### Alternative Lullabies

The following lullabies are lenses to choose to match the shape of the problem.


### Procedural Lullaby

> What do I have?  
> What must I give?  
> What changes as I move?  
> What rule lets it live?

### Algorithmic Lullaby

> What **stays** True?  
> What shrinks each step?  
> What must be True at the **end**?


### Object Collaboration Lullaby

> Who am I right now?  
> Who owns the move?  
> Who can I ask?  
> What must they prove?

### Dispatch Lullaby 

For dunder methods, operators etc

> Syntax knocks  
> Dispatch decides  
> Objects answer  
> Protocols hold

If something surprises you, ask:

> Which object was asked?


## Responsibility Transfer Signals

When reading a problem or staring at code, highlight any sentence or variable that suggests:

#### Persistence
“Keep track of…” 
“Store…” 
“Remember between rounds…” 

#### Delegation
“Let the X decide…”  
“Handled by…”  
“Uses the Y to…” 

#### Aggregation
“List of…”  
“Collection of…”  
“Multiple…”  

#### Translation
“Display…”  
“Format…” 
“Return as a string…”  

#### Coordination
“After that…”  
“Then pass…”  
“Based on the result…”. 

Every one of those phrases is a neon sign saying: *A single-line transfer is coming*.

And once you see that, you don’t solve the problem yet. You tag the site:

This is a KEEP site  
This is a GIVE site  
This is a GET site  
This is a GATHER site  
This is a SHOW site. 

You are mapping future handoffs before they happen. That’s the same thing Bill Thurston meant by “morally” understanding something. We must understand the reason movement *must* occur.

### The Responsibility Lullaby 

**Keep it — if it must persist**

> This belongs to me now.

```python
self.x = x
```

**Give it — if someone else must act**

> They know what to do with this.

```python
other.do(x)
```

**Get it — if I need what they know**

>Ask, don’t assume.

```python
y = obj.value
```

**Gather it — if there will be many**

>Track it over time.

```python
self.items.append(item)
```

**Show it — if the outside must see**

> Translate for strangers.

```python
return str(x)
```

> If it must last — Keep it   
> If they must act — Give it    
> If I must know — Get it  
> If there are many — Gather it  
> If others must see — Show it  
