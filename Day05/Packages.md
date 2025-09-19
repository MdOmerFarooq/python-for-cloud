### Packages

A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file , which indicates that the directory should be treated as a package.

**Example:**

Suppose you have a package structure as follows:

```
my_package/
    __init__.py
    module1.py
    module2.py
```

You can use modules from this package as follows:

```python
from my_package import module1
