using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Interactions;
using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace GGApp.Common.Drivers
{
    public class ChromeAutomation : BrowserAutomationBase
    {      
        public override string Init()
        {
            string path = "";
            try
            {
                path = DriverHelper.GetDriverPath();
                var options = new ChromeOptions();
                options.AddArgument("--disable-gpu");
                options.AddArgument("--no-sandbox");
                options.AddArgument("--mute-audio");

                _driver = new ChromeDriver(path, options);
                _actions = new Actions(_driver);
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }

            return path;
        }
    }
}
