using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace GGApp.Common
{

    public class DriverHelper
    {
        public static ChromeDriver GetChromeDriver()
        {
            string driverPath = GetDriverPath();
            var options = new ChromeOptions();
            options.AddArgument("--disable-gpu");
            options.AddArgument("--no-sandbox");
            var service = ChromeDriverService.CreateDefaultService(driverPath);
            var driver = new ChromeDriver(service, options);
            return driver;
        }

        static string GetDriverPath()
        {
            string baseDir = AppContext.BaseDirectory;

            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
                return Path.Combine(baseDir, "selenium", "win");

            if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
                return Path.Combine(baseDir, "selenium", "mac");

            throw new NotSupportedException("Unsupported platform");
        }
    }

    public enum WebBType
    {
        chrome
    }

}
