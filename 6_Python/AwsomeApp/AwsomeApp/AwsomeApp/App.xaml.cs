using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace AwsomeApp
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();            
            // 单页面程序
            MainPage = new NavigationPage(new MainPage()) { };
        }

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
        }
    }
}
