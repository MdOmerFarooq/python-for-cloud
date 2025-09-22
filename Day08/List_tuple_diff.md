# Understanding Differences Between Tuples and Lists
Tuples and lists are both common data structures used in programming, but they have some fundamental differences that make them suitable for different purposes. 

## Mutable and immutable

Lists are mutable, meaning their elements can be added, removed, or modified after creation. we can use methods like append(), remove(), and pop() to change the contents of a list. whereas Tuples are immutable, and once created, their elements cannot be changed, added, or removed. we can't use methods to modify the tuple.

## syntax 

Lists are created using square brackets [ ] and tuples are created paranthesis ()

# Uses
List: Lists are used when we need a collection of elements that can change, such as a dynamic list of items or data that needs to be modified.

Tuple: Tuples are used when we need an ordered collection of elements that should not change, such as representing a point in 2D space (x, y), or when you want to ensure the integrity of the data.

# memory usage 
List: Lists generally consume more memory than tuples because they need to store additional information to support their mutability.

Tuple: Tuples consume less memory because they are immutable, and the interpreter can optimize memory usage.



