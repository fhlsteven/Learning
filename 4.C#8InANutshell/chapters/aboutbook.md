# C# 8.0 in a Nutshell The Definitive Reference

Joseph Albahari & Eric Johannsen

---

1. [Preface](./1_Preface.md)  
   1. Intended Audience 
   2. How This Book Is Organized
   3. What You Need to Use This Book
   4. Conventions Used in This Book
   5. Using Code Examples
   6. O'Reilly Online Learning
   7. We'd Like To Hear from You 
   8. Acknowledgments
        1. Joseph Albahari
        2. Eric Johannsen
2. Introducing C# and .NET Core
   1. Object Orientation
   2. Type Safety
   3. Memory Management
   4. Platform Support
   5. C# and the Common Language Runtime
   6. Frameworks and Base Class Libraries
   7. Legacy and Niche Frameworks
   8. Windows Runtime
   9. A Brief History of C#
      1. What's New in C# 8.0
      2. What's New in C# 7.x
      3. What's New in C# 6.0
      4. What's New in C# 5.0
      5. What's New in C# 4.0
      6. What's New in C# 3.0
      7. What's New in C# 2.0
3. C# Language Basics
   1. A First C# Program
       1. Compilation
   2. Syntax
       1. Identifiers and Keywords
       2. Literals,Punctuators,and Operators
       3. Comments
   3. Type Basics
       1. Predefined Type Examples
       2. Custom Type Examples
       3. Conversions
       4. Value Types versus Reference Types
       5. Predefined Type Taxonomy
    4. Numeric Types
       1. Numeric Literals
       2. Numeric Conversions
       3. Arithmetic Operators
       4. Increment and Decrement Operators
       5. Specialized Operations on Integral Types
       6. 8- and 16-Bit Integral Types
       7. Special Float and Double Values
       8. double Versus decimal
       9. Real-Number Rounding Errors
    5. Boolean Type and Oprators  
       1. bool Conversions  
       2. Equality and Comparison Operators  
       3. Conditional Operators  
    6. Strings and Characters  
       1. char Conversions
       2. String Type
    7. Arrays  
       1. Default Element Initialization
       2. Indices and Ranges(C# 8)
       3. Multidimensional Arrays
       4. Simplified Array Initialization Expressions
       5. Bounds Checking
    8. Variables and Parameters
       1. The Stack and the Heap
       2. Definite Assignment
       3. Default Values
       4. Parameters
       5. Ref Locals
       6. Ref Returns
       7. var —— Implicitly Typed Local Variables
    9. Expressions and Operators
       1. Primary Expressions
       2. Void Expressions
       3. Assignment Expressions
       4. Operator Precedence and Associativity
       5. Operator Table
    10. Null Operators  
       1. Null-Coalescing Operator  
       2. Null-Coalescing Assignment Operator(C# 8)  
       3. Null-Conditional Operator  
    11. Statements  
       1. Declaration Statements  
       2. Expression Statements  
       3. Selection Statements  
       4. Iteration Statements  
       5. Jump Statements  
       6. Miscellaneous Statements  
    12. Namespaces  
       1. The using Directive  
       2. using static  
       3. Rules Within a Namespace  
       4. Aliasing Types and Namespaces  
       5. Advanced Namespace Features  
4. Creating Types in C#  
   1. Classes  
       1. Fields  
       2. Constants  
       3. Methods  
       4. Instance Constructors
       5. Deconstructors
       6. Object Initializers
       7. The this Reference  
       8. Properties  
       9. Indexers  
       10. Static Constructors  
       11. Static Classes  
       12. Finalizers  
       13. Partial Types and Methods  
       14. The nameof operator  
   2. Inheritance  
       1. Polymorphism  
       2. Casting and Reference Conversions
       3. Virtual Function Members  
       4. Abstract Classes and Abstract Members  
       5. Hiding Inherited Members  
       6. Sealing Functions and Classes
       7. The base Keyword  
       8. Constructors and Inheritance  
       9. Overloading and Resolution  
   3. The object Type  
       1. Boxing and Unboxing  
       2. Static and Runtime Type Checking  
       3. The GetType Method and typeof Operator  
       4. The ToString Method  
       5. Object Member Listing  
   4. Structs  
       1. Struct Construction Semantics
       2. Read-only Structs and Functions  
       3. Ref Structs  
   5.  Access Modifiers 
       1. Examples  
       2. Friend Assemblies
       3. Accessibility Capping
       4. Restrictions on Access Modifiers
   6. Interfaces  
       1. Extending an Interface  
       2. Explicit Interface Implementation 
       3. Implementing Interface Members Virtually  
       4. Reimplementing an Interface in a Subclass 
       5. Interfaces and Boxing  
       6. Default Interface Members(C# 8)
   7. Enums  
       1. Enum Conversions  
       2. Flags Enums  
       3. Enum Operators  
       4. Type-Safety Issues
   8. Nested Types
   9. Generics
       1. Generic Types
       2. Why Generics Exist
       3. Generic Methods
       4. Declaring Type Parameters
       5. typeof and Unbound Generic Types
       6. The default Generic Value
       7. Generic Constraints  
       8. Subclassing Generic Types 
       9. Self-Referencing Generic Declarations
       10. Static Data
       11. Type Parameters and Conversions
       12. Covariance
       13. Contravariance
       14. C# Generics Versus C++ Templates
5. Advanced C#
   1. Delegates
       1. Writing Plug-in Methods with Delegates
       2. Multicast Delegates
       3. Instance Versus Static Method Targets
       4. Generic Delegate Types
       5. The Func and Action Delegates
       6. Delegates Versus Interfaces
       7. Delegates Compatibility
   2. Events 
       1. Standard Event Pattern
       2. Event Accessors
       3. Event Modifiers
   3. Lambda Expressions
       1. Explicitly Specifying Lambda Parameter Types  
       2. Capturing Outer Variables
       3. Lambda Expressions Versus Local Methods
   4. Anonymous Methods
   5. try Statements and Exceptions
       1. The catch Clause
       2. The finally Block
       3. Throwing Exceptions
       4. Key Properties of System.Exception
       5. Common Exception Types
       6. The Try XXX Method Pattern
       7. Alternatices to Exceptions
   6. Enumeration and Iterators
       1. Enumeration 
       2. Collection Initializers
       3. Iterators
       4. Iterator Semantics
       5. Composing Sequences
   7. Nullable Value Types
       1. Nullable<T> Struct
       2. Implicit and Explicit Nullable Conversions
       3. Boxing and Unboxing Nullable Values
       4. Operator Lifting
       5. bool? with & and | Operators
       6. Nullable Value Types & Null Operators
       7. Scenarios for Nullable Value Types
       8. Alternaticves to Nullable Value Types
   8. Nullable Reference Types(C# 8)
       1. The Null-Forgiving Operator
       2. Separating the Annotation and Warning Contexts
       3. Treating Nullable Warnings as Errors
   9. Extension Methods 
       1. Extension Method Chaining
       2. Ambiguity and Resolution
   10. Anonymous Types
   11. Tuples
       1. Naming Tuple Elements
       2. 
        
        

    
