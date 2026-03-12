# Pure Functional Recursive Descent Parser

A lightweight, purely functional parser for a Domain-Specific Language (DSL) written in standard Python. This project demonstrates advanced functional programming paradigms by completely eliminating procedural loops (`for`/`while`) and mutable state (`list.append`, global variables).

## Architectural Paradigms

This parser relies on two distinct functional phases:

1. **Declarative Data Pipeline (Lexical Analysis)**
   - Utilizes higher-order functions (`map` and `filter`) combined with anonymous functions (`lambda`) to clean and transform the input stream declaratively.
   - Leverages **Lazy Evaluation**. Transformations are deferred until the final pipeline is explicitly evaluated and frozen into an immutable tuple, ensuring high memory efficiency.

2. **Syntactic Analysis (Mutual Recursion)**
   - Replaces stateful iterators with **Explicit State Passing**. Every function accepts the remaining token sequence and returns a tuple of `(parsed_value, remaining_tokens)`.
   - Utilizes the **Accumulator Pattern** and strict **Immutability**. Lists are built by concatenating elements into entirely new tuples during tail-recursive calls, rather than mutating an existing data structure in memory.
   - Relies on **Mutual Recursion** between `parse_expression` and `parse_list` to traverse deeply nested tree structures without requiring a global scope.

## Usage

```python
from parser import parse_dsl

# Input string containing nested lists, mixed types, and comments
dsl_input = "[ user 101 [ role admin #internal_comment ] ]"

ast = parse_dsl(dsl_input)
print(ast)
# Output: ('user', 101, ('role', 'admin'))


<img width="2920" height="343" alt="image" src="https://github.com/user-attachments/assets/7a7e9a8a-53de-4091-ba7e-cbfa8cc0708d" />

