# Core Concepts of Object-Oriented Programming (OOP)

## Encapsulation

**Encapsulation** is the practice of bundling data (attributes) and the methods that operate on that data into a single unit, or **class**. It's about protecting an object's internal state by preventing direct outside access. Think of it like a capsule 💊 where the medicine (data) is protected by the casing (methods).

---

## Abstraction

**Abstraction** means hiding complex implementation details and showing only the essential features of an object. It focuses on **what** an object does instead of **how** it does it. A TV remote is a perfect example: you use a simple interface (buttons) without needing to know about the complex electronics inside.

---

## Inheritance

**Inheritance** is a mechanism that allows a new class (the **child** or **subclass**) to acquire the properties and methods of an existing class (the **parent** or **superclass**). This creates an "**is-a**" relationship (e.g., a `Dog` is an `Animal`) and is a great way to reuse code.

---

## Polymorphism

**Polymorphism**, which means "many forms," is the ability of different objects to respond to the same method call in their own unique way. For example, a `Dog` object and a `Cat` object can both have a `make_sound()` method, but one will "bark" and the other will "meow."

---

## The `super()` function

The **`super()`** function is used within a child class to call methods that belong to its parent class. It's often used in the `__init__` method to ensure the parent's attributes are initialized before adding the child's specific attributes.

---

## Dunder (Magic) Methods

**Dunder methods** (short for **D**ouble **Under**score) are special Python methods with names that start and end with double underscores, like `__init__` or `__str__`. You don't call them directly; instead, they're automatically invoked by Python when you use certain syntax (like creating an object or using the `print()` function), allowing your custom objects to behave like built-in types.