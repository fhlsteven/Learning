using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenCvSharp;

namespace GGApp.Common
{
    public class ORBMatcher
    {
        private static readonly ORB _orb = ORB.Create(nFeatures: 2000);
        private static readonly Rect EmptyRect = new Rect(0, 0, 0, 0);

        // 模板缓存：防止重复 DetectAndCompute（提升几十倍性能）
        private static readonly ConcurrentDictionary<string, (KeyPoint[] kp, Mat des, int w, int h)> _cache = new();

        /// <summary>
        /// ORB 匹配：返回是否找到 + 匹配框
        /// </summary>
        public static (bool found, Rect region) Match(string sourcePath, string templatePath)
        {
            using var src = Cv2.ImRead(sourcePath, ImreadModes.Color);
            if (src.Empty()) return (false, EmptyRect);

            // 加载模板（带缓存）
            var tplData = LoadTemplate(templatePath);
            if (tplData.des.Empty()) return (false, EmptyRect);

            // 检测源图 ORB
            KeyPoint[] kpSrc;
            Mat desSrc = new Mat();
            _orb.DetectAndCompute(src, null, out kpSrc, desSrc);
            if (desSrc.Empty()) return (false, EmptyRect);

            // Hamming 匹配
            var bf = new BFMatcher(NormTypes.Hamming);
            var matches = bf.Match(desSrc, tplData.des);

            if (matches.Length < 10)
                return (false, EmptyRect);

            // 距离过滤（增强稳定性）
            var minDist = matches.Min(m => m.Distance);
            var threshold = Math.Max(30, minDist * 3); // 动态阈值

            var good = matches.Where(m => m.Distance <= threshold).ToList();
            if (good.Count < 8)
                return (false, EmptyRect);

            // RANSAC 单应矩阵
            var srcPts = good.Select(m => kpSrc[m.QueryIdx].Pt).ToArray();
            var tplPts = good.Select(m => tplData.kp[m.TrainIdx].Pt).ToArray();

            // 转换为 InputArray
            var srcMat = InputArray.Create(srcPts);
            var tplMat = InputArray.Create(tplPts);

            var H = Cv2.FindHomography(tplMat, srcMat, HomographyMethods.Ransac, 5);
            if (H.Empty())
                return (false, EmptyRect);

            // 映射成包围盒
            var corners = new[]
            {
                new Point2f(0, 0),
                new Point2f(tplData.w, 0),
                new Point2f(tplData.w, tplData.h),
                new Point2f(0, tplData.h),
            };

            var mapped = Cv2.PerspectiveTransform(corners, H);

            float minX = mapped.Min(p => p.X);
            float minY = mapped.Min(p => p.Y);
            float maxX = mapped.Max(p => p.X);
            float maxY = mapped.Max(p => p.Y);

            return (true, new Rect(
                (int)minX, (int)minY,
                (int)(maxX - minX),
                (int)(maxY - minY)
            ));
        }

        /// <summary>
        /// 加载模板 + ORB 描述符（有缓存）
        /// </summary>
        private static (KeyPoint[] kp, Mat des, int w, int h) LoadTemplate(string path)
        {
            return _cache.GetOrAdd(path, p =>
            {
                using var tpl = Cv2.ImRead(p, ImreadModes.Color);
                if (tpl.Empty()) return (Array.Empty<KeyPoint>(), new Mat(), 0, 0);

                KeyPoint[] kpSrc;
                Mat desSrc = new Mat();
                _orb.DetectAndCompute(tpl, null, out kpSrc, desSrc);
                return (kpSrc, desSrc.Clone(), tpl.Width, tpl.Height);
            });
        }
    }
}
