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
            InitializeComponent();
            _restService = new RestService();
        }

        private async void Button_Clicked(object sender, EventArgs e)
        {
            this.blogsCV.ItemsSource = await _restService.GetBlogsData(Constants.BlogsApi);
        }

        private async void blogsCV_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if(e.CurrentSelection != null)
            {
                Blog blog = (Blog)e.CurrentSelection.FirstOrDefault();
                await Shell.Current.GoToAsync($"{nameof(BlogEntry)}?{nameof(BlogEntry.BlogName)}={blog.name}&{nameof(BlogEntry.BlogContent)}={blog.content}");
            }
        }

        
    }
}
