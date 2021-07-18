# Chapter 2 C# Language Basics

In this chapter, we introduce the basics of the C# language.

> NOTE
>> All programs and code snippets in this and the following two chapters are available as interactive samples in LINQPad. Working through these samples in conjunction with the book accelerates learning in that you can edit the samples and instantly see the results without needing to set up projects and solutions in Visual Studio.

>> To download them in *LINQPad*, click the Samples tab, and then click "Download more samples."

## A First C# Program

Following is a program that multiplies 12 by 30 and prints the result, 360, to the screen. The double forward slash indicates that the remainder of a line is a *comment*:

```C#
using System;           // Importing namespace

class Test              // Class declaration
{
    static void Main()  // Method declaration
    {
        int x = 12 * 30;        // Statement 1
        Console.WriteLine(x);   // Statement 2
    }                           // End of method
}                               // End of class
```

At the heart of this program lie two *statements*:

```C#
    int x = 12 * 30;
    Console.WriteLine(x);
```

Statements in C# execute sequentially and are terminated by a semicolon (or a `code block`, as you’ll see later). The first statement computes the expression `12 * 30` and stores the result in a *local variable*, named `x`, which is an integer type. The second statement calls the `Console` class’s `WriteLine` *method*, to print the variable `x` to a text window on the screen.

A method performs an action in a series of statements, called a *statement block*—a pair of braces containing zero or more statements. We defined a single method named `Main`:

```C#
static void Main()
{
    ...
}
```

Writing higher-level functions that call upon lower-level functions simplifies a program. We can *refactor* our program with a reusable method that multiplies an integer by 12, as follows:

```C#
using System;

class Test 
{
    static void Main()
    {
        Console.WriteLine (FeetToInches (30));      // 360
        Console.WriteLine (FeetToInches (100));     // 1200
        
        static int FeetToInches(int feet)
        {
            int inches = feet * 12;
            return inches;
        }
    }
}
```

A method can receive input data from the caller by specifying parameters and output data back to the caller by specifying a return type. We defined a method called `FeetToInches` that has a parameter for inputting feet, and a return type for outputting inches:

`static int FeetToInches (int feet ) {...}`

The *literals* 30 and 100 are the arguments passed to the `FeetToInches` method. The `Main` method in our example has empty parentheses because it has no parameters; it is void because it doesn’t return any value to its caller:

`static void Main()`

C# recognizes a method called `Main` as signaling the default entry point if execution. The `Main` method can optionally return an integer (rather than `void`) in order to return a value to the execution environment (where a nonzero value typically indicates an error). The `Main` method can also optionally accept an array of strings as a parameter (that will be populated with any arguments passed to the executable); for example:

`static int Main(string[] args) { ... }`

> NOTE
>> An array(such as `string[]`) represents a fixed number of elements of a particular type. Arrays are specified by placing square brackets after the elemnt type. We describe them in "Arrays".

