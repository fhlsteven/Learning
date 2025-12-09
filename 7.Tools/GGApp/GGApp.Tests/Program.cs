using GGApp.Common;
using OpenCvSharp;
using System.IO;

namespace GGApp.Tests
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            
            ORBTest();
        }

        public static void ORBTest()
        {
            string sourcePath = Path.Combine("imgs", "source.png"); // 原图路径
            string templatePath = Path.Combine("imgs","template.png"); // 模板保存路径（测试用） // 1. 读取原图

            using var src = Cv2.ImRead(sourcePath, ImreadModes.Color);
            if (src.Empty())
            {
                Console.WriteLine("原图读取失败");
                return;
            }

            // 2. 截取模板区域（这里截取原图中心 100x100 区域）
            // Rect roi = new Rect(src.Width / 2 - 50, src.Height / 2 - 50, 100, 100);
            // using var template = new Mat(src, roi);
            // Cv2.ImWrite(templatePath, template); // 保存模板，用于 ORBMatcher

            // 3. 调用 ORBMatcher
            var (found, region) = ORBMatcher.Match(sourcePath, templatePath);

            // 4. 显示匹配结果
            using var result = src.Clone();
            if (found)
            {
                // 绘制匹配框
                Cv2.Rectangle(result, region, Scalar.Red, 2);
                Console.WriteLine($"匹配成功: {region}");
            }
            else
            {
                Console.WriteLine("匹配失败");
            }

            // 5. 显示原图、模板、匹配结果
            Cv2.ImShow("原图", src);
            using var template = Cv2.ImRead(templatePath, ImreadModes.Color);
            Cv2.ImShow("模板", template);
            Cv2.ImShow("匹配结果", result);
            Cv2.WaitKey(0);
            Cv2.DestroyAllWindows();
        }
    }
}
