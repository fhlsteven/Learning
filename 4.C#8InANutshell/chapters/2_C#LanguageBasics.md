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