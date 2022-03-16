# Theme: Chomsky Normal Form (__CNF__)

### Laboratory Tasks:

- Eliminate empty productions.
- Eliminate any renaming.
- Eliminate inaccessible symbols.
- Eliminate the non productive symbols.
- Obtain the Chomsky Normal Form.

## Normal forms of the context-free languages

In the case of arbitrary grammars the normal form was defined as grammars with no terminals in the
left-hand side of productions. The normal form in the case of the context-free languages will contains
some restrictions on the right-hand sides of productions.

## Variant 4

```
G = (VN, VT, P, S) VN = {S, A, B, C, D} VT = {a, b}

P = {
    1. S -> aB    6. A -> bBAB   11 B -> empty 
    2. S -> bA    7. A -> b      12 D -> AA
    3. S -> A     8. B -> b      13 C -> Ba
    4. A -> B     9. B -> bS
    5. A -> AS   10. B -> aD
}
```
