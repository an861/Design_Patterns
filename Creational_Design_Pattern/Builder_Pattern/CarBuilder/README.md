Create a Car class(core class) and CarBuilder class (Builder class for config) 
and set the model, engine, color of the car.

Implement both sync and async approach.


STEPS
1. Create core class -> Parameterized constructor
2. Create Builder class -> Default constructor -> set(attributes) and build(instance of core class) methods with METHOD CHAINING(fluent interface)
3. Create instance of the Builder class

METHOD CHANING implement using FLUENT INTERFACE

Method chaining is a design pattern that allows calling multiple methods on the same object in a single statement. It improves code readability and reduces the need for temporary variables.

A fluent interface is a way of implementing method chaining where each method returns self (the same instance of the object), allowing multiple method calls in sequence.

<!-- NOTES -->
Method chaining works with sync directly and not with async directly. 
Async method chaining doesn’t work normally because of await.
To do so, Use await self (with await asyncio.sleep(0, self)) in async methods to enable method chaining. [NOT WORKING]
Go with no method chaining for async operations

✅ Use return self when using fluent interface (method chaining).
✅ Use return new object when immutability is required.