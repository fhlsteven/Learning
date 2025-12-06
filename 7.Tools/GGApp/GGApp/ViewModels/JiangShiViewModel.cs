using Avalonia.Interactivity;
using CommunityToolkit.Mvvm.Input;
using GGApp.Common;
using OpenQA.Selenium.Chrome;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace GGApp.ViewModels
{
    public partial class JiangShiViewModel : ViewModelBase
    {
        private ChromeDriver? _driver;

        [RelayCommand]
        private void OpenChrome()
        {
            _driver = DriverHelper.GetChromeDriver();                  
        }
    }
}
