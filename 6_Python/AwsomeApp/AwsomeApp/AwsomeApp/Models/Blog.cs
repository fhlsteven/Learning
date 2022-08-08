using System;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;

namespace AwsomeApp.Models
{
    public class Blog
    {
        public string id { get; set; }

        public string name { get; set; }

        public string summary { get; set; }

        public string content { get; set; }

        public string user_id { get; set; }

        public string user_name { get; set; }

        public float created_at { get; set; }
    }

    public class BlogsResult
    {
        public List<Blog> blogs { get; set; } = new List<Blog>();
    }
}
