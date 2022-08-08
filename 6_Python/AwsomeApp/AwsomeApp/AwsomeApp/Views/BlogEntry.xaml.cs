using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace AwsomeApp.Views
{
    [QueryProperty(nameof(BlogName), nameof(BlogName))]
    [QueryProperty(nameof(BlogContent), nameof(BlogContent))]
    public partial class BlogEntry : ContentPage
    {
        public string BlogName;
        public string BlogContent;

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