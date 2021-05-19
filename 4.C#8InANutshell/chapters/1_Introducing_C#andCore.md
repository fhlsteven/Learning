# Introducing C# and .NET Core

C# is a general-purpose, type-safe, object-oriented programming language. The goal of the language is programmer productivity. To this end, C# balances simplicity, expressiveness, and performance. The chief architect of the language since its first version is Anders Hejlsberg (creator of Turbo Pascal and architect of Delphi). The C# language is platform neutral and works with a range of platform-specific frameworks.

## Object Orientation

C# is a rich implementation of the object-orientation paradigm, which
includes *encapsulation*, *inheritance*, and *polymorphism*.
Encapsulation means creating a boundary around an object to
separate its external (public) behavior from its internal (private)
implementation details. Following are the distinctive features of C#
from an object-oriented perspective:

* Unified type system  
    The fundamental building block in C# is an encapsulated unit of data and functions called a *type*. C# has a *unified type system* in which all types ultimately share a common base type. This means that all types, whether they represent business objects or are primitive types such as numbers, share the same basicfunctionality. For example, an instance of any type can be converted to a string by calling its `ToString` method.

* Classes and interfaces  
    In a traditional object-oriented paradigm, the only kind of type is a class. In C#, there are several other kinds of types, one of which is an *interface*. An interface is like a class that cannot hold data. This means that it can define only *behavior* (and not state), which allows for multiple inheritance as well as a separation between specification and implementation.

* Properties, methods, and events  
    In the pure object-oriented paradigm, all functions are methods. In C#, methods are only one kind of *function member*, which also includes *properties* and *events* (there are others, too). Properties are function members that encapsulate a piece of an object’s state, such as a button’s color or a label’s text. Events are function members that simplify acting on object state changes.

Although C# is primarily an obejct-oriented language, it also borrows from the *functional programming* paradigm; secifically:

* Functions can be treated as values
    Using *delegates*, C# allows functions to be passed as values to and from other functions.

* C# supports patterns for purity  
    Core to functional programming is avoiding the use of variables whose values change, in favor of declarative patterns. C# has key features to help with those patterns, including the ability to write unnamed functions on the fly that "capture" variables (*lambda expressions*), and the ability to perform list or reactive programming via *query expressions*. C# also makes it easy to define read-only fields and properties for writing *immutable* (read-only) types.

## Type Safety

C# is primarily a *type-safe* language, meaning that instances of types can interact only through protocols they define, thereby ensuring each type's internal consistency. For instance, C# prevents you from interacting with a *string* type as though it were an *integer* type.

More specifically, C# supports *static typing*, meaning that the language enforces type safety at *compile time*. This is in addition to type safety being enforced at *runtime*.

Static typing eliminates a large class of errors before a program is even run. It shifts the burden away from runtime unit tests onto the compiler to verify that all the types in a program fit together correctly. This makes large programs much easier to manage, more predictable, and more robust. Furthermore, static typing allows tools such as IntelliSense in Visual Studio to help you write a program, because it knows for a given variable. Such tools can also idetify everywhere in your program that a variable, type , or method is used, allowing for reliable refactoring.

> NOTE  
> C# also allows parts of your code to be dynamically typed via the `dynamic` keyword. However, C# remains a predominantly statically typed language.

C# is also called a *strongly typed language* because its type rules are strictly enforced (whether statically or at runtime). For instance, you cannot call a function that's designed to accept an integer with a floating-point number, unless you first *explicitly* convert the floating-point number to an integer. This helps prevent mistakes.

## Memory Management

C# relies on the runtime to perform automatic memory management.
The Common Language Runtime has a garbage collector that
executes as part of your program, reclaiming memory for objects that
are no longer referenced. This frees programmers from explicitly
deallocating the memory for an object, eliminating the problem of
incorrect pointers encountered in languages such as C++.

C# does not eliminate pointers: it merely makes them unnecessary for
most programming tasks. For performance-critical hotspots and
interoperability, pointers and explicit memory allocation are
permitted in blocks that are marked `unsafe`.

## Platform Support

Historically, C# was used almost entirely for writing code to run on
Windows platforms. However, Microsoft and other companies have
since invested in other platforms:

* The *.NET Core* Framework enables web application development in Linux and macOS (as well as Windows).

* *Xamarin* enables mobile app development for iOS and Android.

* *Blazor* compiles C# to web assembly that can run in a browser.

And on the Windows platform:

* *.NET Core* 3 enables rich-client and web application development
on Windows 7 to 10.

* *Universal Windows Platform* (UWP) supports Windows 10
desktop and devices such as Xbox, Surface Hub, and Hololens.

## C# and the Common Language Runtime

C# depends on a *Common Language Runtime* (CLR), which provides
essential runtime services such as automatic memory management
and exception handling. (The word common refers to the fact that the
same runtime can be shared by other managed programming
languages, such as F#, Visual Basic, and Managed C++.)

## Frameworks and Base Class Libraries

## Legacy and Niche Frameworks

## Windows Runtime

## A Brief History of C\#

### What's New in C# 8.0

### What's New in C# 7.x

### What's New in C# 6.0

### What's New in C# 5.0

### What's New in C# 4.0

### What's New in C# 3.0

### What's New in C# 2.0
