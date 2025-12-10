using Avalonia.Interactivity;
using CommunityToolkit.Mvvm.Input;
using GGApp.Common;
using GGApp.Common.Drivers;
using OpenCvSharp.Text;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace GGApp.ViewModels
{
    public partial class JiangShiViewModel : ViewModelBase
    {
        private IBrowserAutomation? _webBro;

        [RelayCommand]
        private void OpenChrome()
        {
            _webBro = new ChromeAutomation();
            _webBro.Init();
            _webBro.SetWindow(1140, 1202, 0, 0);
            _webBro.Navigate("https://www.bing.com");            
        }

        [RelayCommand]
        private void Normal() 
        {
            string re = _webBro.Screenshot(Path.Combine(AppContext.BaseDirectory, "Assets", "all.png"));            
        }
    }
}
