using AwsomeApp.Data;
using AwsomeApp.Models;
using AwsomeApp.Views;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace AwsomeApp
{
    public partial class MainPage : ContentPage
    {
        RestService _restService;

        public MainPage()
        {
            Title = "最新日志";
            NavigationPage.SetBackButtonTitle(this, Title); // 这个属性只会在ios上显示，不会在 andriod 上显示，而且不是本页面而是跳转过去的那个页面上的返回按钮
            _restService = new RestService();
            InitializeComponent();
            Load();                                  
        }

        private async void Load()
        {
            this.blogsCV.ItemsSource = await _restService.GetBlogsData(Constants.BlogsApi);
        }

        private async void blogsCV_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if(e.CurrentSelection != null)
            {
                Blog blog = (Blog)e.CurrentSelection.FirstOrDefault();
                await Navigation.PushAsync(new BlogEntry() { Title = blog.name, BindingContext = blog});
            }
        }

        
    }
}
