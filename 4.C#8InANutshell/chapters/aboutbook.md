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
2. [Introducing C# and .NET Core](./1_Introducing_C#andCore.md)
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
3. [C# Language Basics](./2_C#LanguageBasics.md)
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
   5. Access Modifiers
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
       1. Nullable\<T> Struct
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
       2. ValueTuple.Create
       3. Deconstructing Tuples
       4. Equality Comparison
       5. The System.Tuple classes
   12. Patterns
       1. Property Patterns (C# 8)
       2. Tuple Patterns (C# 8)
       3. Positional Patterns (C# 8)
       4. var Pattern
       5. Constant Pattern
   13. Attributes
       1. Attribute Classes
       2. Named and Positional Attribute Parameters
       3. Applying Attributes to Assemblies and Backing
       4. Specifying Multiple Attributes
   14. Caller Info Attributes
   15. Dynamic Binding
       1. Static Binding versus Dynamic Binding
       2. Custom Binding
       3. Language Binding
       4. RuntimeBinderException
       5. Runtime Representation of dynamic
       6. Dynamic Conversions
       7. var Versus dynamic
       8. Dynamic Expressions
       9. Dynamic Calls Without Dynamic Receivers
       10. Static Types in Dynamic Expressions
       11. Uncallable Functions
   16. Operator Overloading
       1. Operator Functions
       2. Overloading Equality and Comparison Operators
       3. Custom Implicit and Explicit Conversions
       4. Overloading true and false
   17. Unsafe Code and Pointers
       1. Pointer Basics
       2. Unsafe Code
       3. The fixed Statement
       4. The Pointer-to-Member Operator
       5. The stackalloc Keyword
       6. Fixed-Size Buffers
       7. void*
       8. Pointers to Unmanaged Code
   18. Preprocessor Directives
       1. Conditional Attributes
       2. pragma warining
   19. XML Documentation
       1. Standard XML Documentation Tags
       2. User-Defined Tags
       3. Type or Member Cross-References
6. Framework Overview
   1. .NET Standard
       1. .NET Standard 2.0
       2. .NET Standard 2.1
       3. Older .NET Standards
       4. .NET Framework and .NET Core Compatibility
   2. Framework and C# Language Versions
   3. Reference Assemblies
   4. The CLR and BCL
       1. System Types
       2. Text Processing
       3. Collections
       4. Querying
       5. XML and JSON
       6. Diagnostics
       7. Concurrency and Asynchrony
       8. Streams and I/O
       9. Networking
       10. Serialization
       11. Assemblies,Reflection,and Attributes
       12. Dynamic Programming
       13. Cryptography
       14. Advanced Threading
       15. Parallel Programming
       16. Span\<T> and Memory\<T>
       17. Native and COM Interoprability
       18. Regular Expressions
       19. The Roslyn Compiler
   5. Application Frameworks
       1. ASP.NET Core
       2. Windows Desktop
       3. UWP
       4. Xamarin
7. Framework Fundamentals
   1. String and Text Handling
       1. char
       2. string
       3. Comparing Strings
       4. StringBuilder
       5. Text Encodings and Unicode
   2. Dates and Times
       1. TimeSpan
       2. DateTime and DateTimeOffset
   3. Dates and Time Zones
       1. DateTime and Time Zones
       2. DateTimeOffset and Time Zones
       3. TimeZone and TimeZoneInfo
       4. Daylight Saving Time and DateTime
   4. Formatting and Parsing
       1. ToString and Parse
       2. Format Providers
   5. Standard Format Strings and Parsing Flags
       1. Numeric Format Strings
       2. NumberStyles
       3. Date/Time Format Strings
       4. DateTimeStyles
       5. Enum Format Strings
   6. Other Conversion Mechanisms
       1. Convert
       2. XmlConvert
       3. Type Converters
       4. BitConverter
   7. Globalization
       1. Globalization Checklist
       2. Testing
   8. Working with Numbers
       1. Conversions
       2. Math
       3. BigInteger
       4. Complex
       5. Random
   9. Enums
       1. Enum Conversions
       2. Enumerating Enum Values
       3. How Enums Work
   10. The Guid Struct
   11. Equality Comparison
       1. Value Versus Referential Equality
       2. Standard Equality Protocols
       3. Equality and Custom Types
   12. Order Comparison
       1. IComparable
       2. < and >
       3. Implementing the IComparable Interfaces
   13. Utility Classes
       1. Console
       2. Environment
       3. Process
       4. AppContext
8. Collections
   1. Enumeration
       1. IEnumerable and IEnumerator
       2. IEnumerable\<T> and IEnumerator\<T>
       3. Implementing the Enumeration Interfaces
   2. The ICollection and IList Interfaces
       1. ICollection\<T> and ICollection
       2. IList\<T> and IList
       3. IReadOnlyCollection\<T> and IReadOnlyList\<T>
   3. The Array Class
       1. Construction and Indexing
       2. Enumeration
       3. Length and Rank
       4. Searching
       5. Sorting
       6. Reversing Elements
       7. Copying
       8. Converting and Resizing
   4. Lists,Queues,Stacks,and Sets
       1. List\<T> and ArrayList
       2. LinkedList\<T>
       3. Queue\<T> and Queue
       4. Stack\<T> and Stack
       5. BitArray
       6. HashSet\<T> and SortedSet\<T>
   5. Dictionaries
       1. IDictionary\<TKey, TValue>
       2. IDictionary
       3. Dictionary\<Tkey, TValue> and Hashtable
       4. OrderedDictionary
       5. ListDictionary and HybridDictionary
       6. Sorted Dictionaries
   6. Customizable Collections
       1. Collection\<T> and CollectionBase
       2. KeyedCollection\<TKey,TItem> and DictionaryBase
       3. ReadOnlyCollection\<T>
   7. Immutable Collections
       1. Creating Immutable Collections
       2. Manipulating Immutable Collections
       3. Builders
       4. Immutable Collections and Performance
   8. Plugging in Equality and Order
       1. IEqualityComparer and EqualityComparer
       2. IComparer and Comparer
       3. StringComparer
       4. IStructuralEquatable and IStructualComparable
9. LINQ Queries
   1. Getting Started
   2. Fluent Syntax
       1. Chaining Query Operators
       2. Composing Lambda Expressions
       3. Natural Ordering
       4. Other Operators
   3. Query Expressions
       1. Range Variables
       2. Query Syntax Versus SQL Syntax
       3. Query Syntax Versus Fluent Syntax
       4. Mixed-Syntax Queries
   4. Deferred Execution
       1. Reevaluation
       2. Captured Variables
       3. How Deferred Execution Works
       4. Chaining Decorators
       5. How Queries Are Executed
   5. Subqueries
       1. Subqueries and Deferred Execution
   6. Composition Strategies
       1. Progressive Query Building
       2. The into Keyword
       3. Wrapping Queries
   7. Projection Strategies
       1. Object Initializers
       2. Anonymous Types
       3. The let Keyword
   8. Interpreted Queries
       1. How Interpreted Queries Work
       2. Combining Interpreted and Local Queries
       3. AsEnumerable
   9. EF Core
       1. EF Core Entity Classes
       2. DbContext
       3. Object Tracking
       4. Change Tracking
       5. Navigation Properties
       6. Deferred Execution
   10. Building Query Expressions
       1. Delegates Versus Expression Trees
       2. Expression Trees
10. LINQ Operators
    1. Overview
       1. Sequence → Sequence
       2. Sequence → Element or Value
       3. Void → Sequence
    2. Filtering
       1. Where
       2. Take and Skip
       3. TakeWhile and SkipWhile
       4. Distinct
    3. Projecting
       1. Select
       2. SelectMany
    4. Joining
       1. Join and GrooupJoin
       2. The Zip Operator
    5. Ordering
       1. OrderBy, OrderByDescending, ThenBy, and ThenByDescending
    6. Grouping
       1. GroupBy
    7. Set Operators
       1. Concat and Union
       2. Intersect and Except
    8. Conversion Methods
       1. OfType and Cast
       2. ToArray, ToList, ToDictionary, ToHashSet, and ToLookup
       3. AsEnumerable and AsQueryable
    9. Element Operators
       1. First, Last, and Single
       2. ElementAt
       3. DefaultIfEmpty
    10. Aggregation Methods
        1. Count and LongCount
        2. Min and Max
        3. Sum and Average
        4. Aggregate
    11. Quantifiers
        1. Contains and Any
        2. All and SequenceEqual
    12. Generation Methods
        1. Empty
        2. Range and Repeat
11. LINQ to XML
    1. Architectural Overview
       1. What is a DOM?
       2. The LINQ to XML DOM
    2. X-DOM Overview
       1. Loading and Parsing
       2. Saving and Serializing
    3. Instantiating an X-DOM
       1. Functional Construction
       2. Specifying Content
       3. Automatic Deep Cloning
    4. Navigating and Querying
       1. Child Node Navigation
       2. Parent Navigation
       3. Peer Node Navigation
       4. Attribute Navigation
    5. Updating an X-DOM
       1. Simple Value Updates
       2. Updating Child Nodes and Attributes
       3. Updating Through the Parent
    6. Working with Values
       1. Setting Values
       2. Getting Values
       3. Values and Mixed Content Nodes
       4. Automatic XText Concatenation
    7. Documents and Declarations
       1. XDocument
       2. XML Declarations
    8. Names and Namespaces
       1. Namespaces in XML
       2. Specifying Namespaces in the X-DOM
       3. The X-DOM and Default Namespaces
       4. Prefixes
    9. Annotations
    10. Projecting into an X-DOM
        1. Eliminating Empty Elements
        2. Streaming a Projection
12. Other XML and JSON Technologies
    1. XmlReader
        1. Reading Nodes
        2. Reading Elements
        3. Reading Attributes
        4. Namespaces and Prefixes
    2. XmlWriter
        1. Writing Attributes
        2. Writing Other Node Types
        3. Namespaces and Prefixes
    3. Patterns for Using XmlReader/XmlWriter
        1. Working with Hierarchical Data
        2. Mixing XmlReader/XmlWriter with an X-DOM
    4. Working with JSON
        1. Utf8JsonReader
        2. Utf8JsonWriter
        3. JsonDocument
13. Disposal and Garbage Collection
    1. IDisposable, Dispose, and Close
        1. Standard Disposal Semantics
        2. When to Dispose
        3. Clearing Fields in Disposal
        4. Anonymous Disposal
    2. Automatic Garbage Collection
        1. Roots
        2. Garbage Collection and WinRT
    3. Finalizers
        1. Calling Dispose from a Finalizer
        2. Resurrection
    4. How the GC Works
        1. Optimization Techniques
        2. Forcing Garbage Collection
        3. Tuing Garbage Collection at Runtime
        4. Memory Pressure
        5. Array Pooling
    5. Managed Memory Leaks
        1. Timers
        2. Diagnosing Memory Leaks
    6. Weak References
        1. Weak References and Caching
        2. Weak References and Events
14. Diagnostics
    1. Conditional Compilation
        1. Conditional Compilation Versus Static Variable Flags
        2. The Conditional Attribute
    2. Debug and Trace Classes
        1. Fail and Assert
        2. TraceListener
        3. Flushing and Closing Listeners
    3. Debugger Integration
        1. Attaching and Breaking
        2. Debugger Attributes
    4. Processes and Process Threads
        1. Examining Running Processes
        2. Examining Threads in a Process
    5. StackTrace and StackFrame
    6. Windows Event Logs
        1. Writing to the Event Log
        2. Reading the Event Log
        3. Monitoring the Event Log
    7. Performance Counters
        1. Enumerating the Available Counters
        2. Reading Performance Counter Data
        3. Creating Counters and Writing Performance Data
    8. The Stopwatch Class
    9. Cross-Platform Diagnostics Tools
        1. dotnet-counters
        2. dotnet-trace
        3. dotnet-dump
15. Concurrency and Asynchrony
    1. Introdcution
    2. Threading
        1. Creating a Thread
        2. Join and Sleep
        3. Blocking
        4. Local versus Shared State
        5. Locking and Thread Safety
        6. Passing Data to a Thread
        7. Exception Handling
        8. Foreground versus Background Threads
        9. Thread Priority
        10. Signaling
        11. Threading in Rich Client Applications
        12. Synchronization Contexts
        13. The Thread Pool
    3. Tasks
        1. Starting a Task
        2. Returning values
        3. Exceptions
        4. Continuations
        5. TaskCompletionSource
        6. Task.Delay
    4. Principles of Asynchrony
        1. Synchronous versus Asynchronous Operations
        2. What Is Asynchronous Programming?
        3. Asynchronous Programming and Continuations
        4. Why Language Support Is Important
    5. Asynchronous Functions in C#
        1. Awaiting
        2. Writing Asynchronous Functions
        3. Asynchronous Lambda Expressions
        4. Asynchronous Streams(C# 8)
        5. Asynchronous Methods in WinRT
        6. Asynchronous and Synchronization Contexts
        7. Optimizations
    6. Asynchronous Patterns
        1. Cancellation
        2. Progress Reporting
        3. The Task-Based Asynchronous Pattern
        4. Task Combinators
        5. Asynchronous Locking
    7. Obsolete Patterns
        1. Asynchronous Programming Model
        2. Event-Based Asynchronous Pattern
        3. BackgroundWorker
16. Streams and I/O
    1. Stream Architecture
    2. Using Streams
        1. Reading and Writing
        2. Seeking
        3. Closing and Flushing
        4. Timeouts
        5. Thread Safety
        6. Backing Store Streams
        7. FileStream
        8. MemoryStream
        9. PipeStream
        10. BufferedStream
    3. Stream Adapters
        1. Text Adapters
        2. Binary Adapters
        3. Closing and Disposing Stream Adapters
    4. Compression Streams
        1. Compressing in Memory
        2. Unix gzip File Compression
    5. Working with ZIP Files
    6. File and Directory Operations
        1. The File Class
        2. The Directory Class
        3. FileInfo and DirectoryInfo
        4. Path
        5. Special Folders
        6. Querying Volume Information
        7. Catching Filesystem Events
    7. File I/O in UWP
        1. Working with Directories
        2. Working with Files
        3. Obtaining Directories and Files
    8. OS Security
        1. Running in a Standard User Account
        2. Administrative Elevation and Virtualization
    9. Memory-Mapped Files
        1. Memory-Mapped Files and Random File I/O
        2. Memory-Mapped Files and Shared Memory(Windows)
        3. Cross-Platform Interprocess Shared Memory
        4. Working with View Accessors
17. Networking
    1. Network Architecture
    2. Addresses and Ports
    3. URIs
    4. Client-Side Classes
        1. WebClient
        2. WebRequest and WebResponse
        3. HttpClient
        4. Proxies
        5. Authentication
        6. Exception Handling
    5. Working with HTTP
        1. Headers
        2. Query Strings
        3. Uploading Form Data
        4. Cookies
    6. Writing an HTTP Server
    7. Using FTP
    8. Using DNS
    9. Sending Mail with SmtpClient
    10. Using TCP
        1. Concurrency with TCP
    11. Receiving POP3 Mail with TCP
    12. TCP in UWP
18. Serialization
    1. Serialization Concepts
        1. Serialization Engines
        2. Formatters
        3. Explicit Versus Implicit Serialization
    2. The XML Serializer
        1. Getting Started with Attribute-Based Serialization
        2. Subclasses and Child Objects
        3. Serializing Collections
        4. IXmlSerializable
    3. The JSON Serializer
        1. Getting Started
        2. Serializing Child Objects
        3. Serializing Collections
        4. Controlling Serialization with Attributes
        5. Customing Data Conversion
        6. JSON Serialization Options
    4. The Binary Serialization
        1. Getting Started
    5. Binary Serialization Attributes
        1. [NonSerialized]
        2. [OnDeserializing]
        3. [OnDeserialized]
        4. [OnSerializing] and [OnSerialized]
        5. [OptionalField] and Versioning
    6. Binary Serialization with ISerializable
        1. Subclassing Serializable Classes
19. Assemblies
    1. What's in an Assembly
        1. The Assembly Manifest
        2. The Application Manifest(Windows)
        3. Modules
        4. The Assembly Class
    2. Strong Names and Assembly Signing
        1. How to Strongly Name an Assembly
    3. Assembly Names
        1. Fully Qualified Names
        2. The AssemblyName Class
        3. Assembly Informational and File Versions
    4. Authenticode Signing
        1. How to Sign with Authenticode
    5. Resources and Satellite Assemblies
        1. Directly Embedding Resources
        2. .resources Files
        3. .resx Files
        4. Satellite Assemblies
        5. Cultures and Subcultures
    6. Loading,Resolving,and Isolating Assemblies
        1. Assembly Load Contexts
        2. The Default ALC
        3. The Current ALC
        4. Assembly.Load and Contextual ALCs
        5. Loading and Resolving Unmanaged Libraries
        6. AssemblyDependencyResolver
        7. Unloading ALCs
        8. The Legacy Loading Methods
        9. Writing a Plug-In System
20. Reflection and Metadata
    1. Reflecting and Activating Types
        1. Obtaining a Type
        2. Type Names
        3. Base Types and Interfaces
        4. Instantiating Types
        5. Generic Types
    2. Reflecting and Invoking Members
        1. Member Types
        2. C# Members versus CLR Members
        3. Generic Type Members
        4. Dynamically Invoking a Memeber
        5. Method Parameters
        6. Using Delegates for Performance
        7. Accessing Nonpublic Members
        8. Generic Methods
        9. Anonymously Calling Members of a Generic Interface
    3. Reflecting Assemblies
        1. Modules
    4. Working with Attributes
        1. Attribute Basics
        2. The AttributeUsage Attribute
        3. Defining Your Own Attribute
        4. Retrieving Attributes at Runtime
    5. Dynamic Code Generation
        1. Generating IL with DynamicMethod
        2. The Evaluation Stack
        3. Passing Arguments to a Dynamic Method
        4. Generating Local Variables
        5. Branching
        6. Instantiating Objects and Calling Instance Methods
        7. Exception Handling
    6. Emitting Assemblies and Types
        1. The Reflection.Emit Object Model
    7. Emitting Type Members
        1. Emitting Methods
        2. Emitting Fields and Properties
        3. Emitting Constructors
        4. Attaching Attributes
    8. Emitting Generic Methods and Types
        1. Defining Generic Methods
        2. Defining Generic Types
    9. Awkward Emission Targets
        1. Uncreated Closed Generics
        2. Circular Dependencies
    10. Parsing IL
        1. Writing a Disassembler
21. Dynamic Programming
    1. The Dynamic Language Runtime
    2. Numeric Type Unification
    3. Dynamic Member Overload Resolution
        1. Simplifying the Visitor Pattern
        2. Anonymously Calling Members of a Generic Type
    4. Implementing Dynamic Objects
        1. DynamicObject
        2. ExpandoObject
    5. Interoperating with Dynamic Languages
        1. Passing State Between C# and a Script
22. Cryptography
    1. Overview
    2. Windows Data Protection
    3. Hashing
        1. Hash Algorithms in .NET Core
        2. Hashing Passwords
    4. Symmetric Encryption
        1. Encrypting in Memory
        2. Chaining Encryption Streams
        3. Disposing Encryption Objects
        4. Key Management
    5. Public-Key Encryption and Signing
        1. The RSA Class
        2. Digital Signing
23. Advanced Threading
    1. Synchronization Overview
    2. Exclusive Locking
        1. The lock Statement
        2. Monitor.Enter and Monitor.Exit
        3. Choosing the Synchronization Object
        4. When to Lock
        5. Locking and Atomicity
        6. Nested Locking
        7. Deadlocks
        8. Performance
        9. Mutex
    3. Locking and Thread Safety
        1. Thread Safety and .NET Core Types
        2. Thread Safety in Application Servers
        3. Immutable Objects
    4. Nonexclusive Locking
        1. Semaphore
        2. Reader/Writer Locks
    5. Signaling with Event Wait Handles
        1. AutoResetEvent
        2. ManualResetEvent
        3. CountdownEvent
        4. Creating a Cross-Process EventWaitHandle
        5. Wait Handles and Continuations
        6. WaitAny,WaitAll,and SignalAndWait
    6. The Barrier Class
    7. Lazy Initializer
        1. Lazy<T>
        2. LazyInitializer
    8. Thread-Local Storage
        1. [ThreadStatic]
        2. ThreadLocal\<T\>
        3. GetData and SetData
        4. AsyncLocal\<T\>
    9. Timers
        1. Multithreaded Timers
        2. Single-Threaded Timers
24. Parallel Programming
    1. Why PFX?
        1. PFX Concepts
        2. PFX Components
        3. When to Use PFX
    2. PLINQ
        1. Parallel Execution Ballistics
        2. PLINQ and Ordering
        3. PLINQ Limitations
        4. Example:Parallel Spellchecker
        5. Functional Purity
        6. Setting the Degree of Parallelism
        7. Cancellation
        8. Optimizing PLINQ
    3. The Parallel Class
        1. Parallel.Invoke
        2. Parallel.For and Parallel.ForEach
    4. Task Parallelism
        1. Creating and Starting Tasks
        2. Waiting on Multiple Tasks
        3. Canceling Tasks
        4. Continuations
        5. Task Schedulers
        6. TaskFactory
    5. Working with AggregateException
        1. Flatten and Handle
    6. Concurrent Collections
        1. IProducerConsumerCollection\<T\>
        2. ConcurrentBag\<T\>
    7. BlockingCollection\<T\>
        1. Writing a Producer/Consumer Queue
25. Span\<T\> and Memory\<T\>
    1. Spans and Slicing
        1. CopyTo and TryCopyTo
        2. Working with Text
    2. Memory\<T\>
    3. Forward-Only Enumerators
    4. Working with Stack-Allocated and Unmanaged Memory
26. Native and COM Interoperability
    1. Calling into Native DLLs
    2. Type Marshaling
        1. Marshaling Common Types
        2. Marshaling Classes and Structs
        3. In and Out Marshaling
    3. Callbacks from Unmanaged Code
    4. Simulating a C Union
    5. Shared Memory
    6. Mapping a Struct to Unmanaged Memory
        1. fixed and fixed {...}
    7. COM Interoperability
        1. The Purpose of COM
        2. The Basics of the COM Type System
    8. Calling a COM Component from C#
        1. Optional Parameters and Named Arguments
        2. Implicit ref Parameters
        3. Indexers
        4. Dynamic Binding
    9. Embedding Interop Types
        1. Type Equivalence
    10. Exposing C# Objects to COM
        1. Enabling Registry-Free COM
27. Regular Expressions
    1. Regular Expression Basics
        1. Compiled Regular Expressions
        2. RegexOptions
        3. Character Escapes
        4. Character Sets
    2. Quantifiers
        1. Greedy Versus Lazy Quantifiers
    3. Zero-Width Assertions
        1. Lookahead and Lookbehind
        2. Anchors
        3. Word Boundaries
    4. Groups
        1. Named Groups
    5. Replacing and Splitting Text
        1. MatchEvaluator Delegate
        2. Splitting Text
    6. Cookbook Regular Expressions
        1. Recipes
    7. Regular Expressions Language Reference
28. The Roslyn Compiler
    1. Roslyn Architecture
        1. Workspaces
        2. Scripting
    2. Syntax Trees
        1. SyntaxTree Structure
        2. Obtaining a Syntax Tree
        3. Traversing and Searching a Tree
        4. Trivia
        5. Transforming a Syntax Tree
    3. Compilations and Semantic Models
        1. Creating a Compilation
        2. Emitting an Assembly
        3. Querying the Semantic Model
        4. Example:Renaming a Symbol
29. Index
