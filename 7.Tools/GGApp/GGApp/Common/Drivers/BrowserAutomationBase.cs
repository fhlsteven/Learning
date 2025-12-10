using OpenQA.Selenium.Interactions;
using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace GGApp.Common.Drivers
{
    public abstract class BrowserAutomationBase : IBrowserAutomation
    {
        protected IWebDriver _driver;
        protected Actions _actions;

        public bool IsReady => _driver != null;

        public abstract string Init();

        public string Navigate(string url)
        {
            try
            {
                _driver.Navigate().GoToUrl(url);
                return url;
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }
        }

        public string Click(int x, int y, bool leftClick = true)
        {
            try
            {
                /*var body = _driver.FindElement(By.TagName("body"));
                _actions.MoveToElement(body, x, y);

                if (leftClick)
                    _actions.Click();
                else
                    _actions.ContextClick();

                _actions.Perform();*/

                _actions.MoveByOffset(x, y);
                if (leftClick)
                    _actions.Click();
                else
                    _actions.ContextClick();
                _actions.Perform();
                _actions.MoveByOffset(-x, -y).Perform();
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }

            return $"x:{x};y:{y}";
        }

        public string Screenshot(string savePath)
        {
            try
            {
                var img = ((ITakesScreenshot)_driver).GetScreenshot();
                img.SaveAsFile(savePath);
                return savePath;
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }
        }

        public string Quit()
        {
            try
            {
                _driver?.Quit();
                _driver?.Dispose();
                _driver = null;
                _actions = null;
                return "OK";
            }
            catch (Exception ex)
            {
                return ex.ToString();
            }
        }

        public void SetWindow(int width, int height, int x, int y)
        {
            var m = _driver.Manage().Window;
            m.Size = new Size(width, height);
            m.Position = new Point(x, y);
        }
    }

}
