using System;

using Xamarin.Forms;

namespace AwsomeApp.Views
{
    public partial class BlogEntry : ContentPage
    {
        public BlogEntry()
        {            
            InitializeComponent();
        }

        async void OnNavigateButtonClicked(object sender, EventArgs e)
        {
            await Navigation.PopAsync();
        }
    }
}