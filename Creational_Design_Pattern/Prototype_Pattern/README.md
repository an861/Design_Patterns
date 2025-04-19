## Prototype Design Pattern
The Prototype Pattern is used when you need to create new objects by copying an existing object (cloning) instead of creating them from scratch.

✅ When to Use?
✔ When object creation is expensive (e.g., deep copying large objects).
✔ When you need multiple variations of the same object with minor modifications.
✔ When you want to avoid subclasses for different configurations.


Sync: Works normally with copy.deepcopy().
Async: If working with async objects (e.g., DB connections), use manual copying instead of copy.deepcopy().