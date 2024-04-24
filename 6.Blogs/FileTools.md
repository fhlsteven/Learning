# 处理文件的小工具

## 背景

在实际工作中，我们经常需要处理一些文件，比如过滤一些log，找到一批文件中的特定数据等。为了提高工作效率以及灵活性，编写一个小工具来简化这些操作。主要针对程序员，自己可以动态调整方法，这里是一个框架，记录一下，省的以后用的时候找不到了。

## 实现

利用委托 delegate 实现处理每一行的数据，使用 StringBuilder 记录想要的结果，最终保存到一个目录。

```cs
using System.Text;

class Program
{
    delegate void ProcessMethod(string line, StringBuilder sb);

    static void Main(string[] args)
    {
        ProcessTest();
    }

    static void ProcessTest()
    {
        MainProcess(@"E:\WorkSpace\WorkContent\Project\2024\Payment", nameof(ProcessTest), (line, sb) => {
            //Console.WriteLine(line);
            /*
            特殊处理的方法
            */            
        });
    }

    static void MainProcess(string filePath,string saveName,ProcessMethod processMethod)
    {
        string result = "";
        if (Directory.Exists(filePath))
        {           
            string[] filePaths = Directory.GetFiles(filePath); // 获取文件夹下所有文件的路径
            foreach (string fp in filePaths.Reverse().ToArray())
            {
                result += MainProcessFile(fp, processMethod);
            }
        }
        else
        {
            result = MainProcessFile(filePath, processMethod);            
        }
        File.WriteAllText($"..\\{saveName}_{DateTime.UtcNow:yyyyMMdd_HHmmss}.txt", result);
    }

    static string MainProcessFile(string filePath, ProcessMethod processMethod)
    {
        string[] lines = File.ReadAllLines(filePath); // 读取当前文件的所有行
        StringBuilder sb = new StringBuilder();
        Console.WriteLine(filePath);
        foreach (string line in lines)
        {
            processMethod(line, sb);
        }
        return sb.ToString();
    }
}
```
