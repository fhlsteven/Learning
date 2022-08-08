using AwsomeApp.Models;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Threading.Tasks;

namespace AwsomeApp.Data
{
    public class RestService
    {
        HttpClient _client;

        public RestService()
        {
            _client = new HttpClient();
        }

        private async Task<string> GetDatasAsync(string uri)
        {
            string content = string.Empty;
            try
            {
                HttpResponseMessage response = await _client.GetAsync(uri);
                if (response.IsSuccessStatusCode)
                {
                    content = await response.Content.ReadAsStringAsync();
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine("\t Error " + ex.ToString());
                throw;
            }

            return content;
        }

        public async Task<List<Blog>> GetBlogsData(string uri)
        {
            List<Blog> results = null;

            try
            {
                string result = await GetDatasAsync(uri);
                if (!string.IsNullOrEmpty(result))
                {

                    BlogsResult blogsResult = JsonConvert.DeserializeObject<BlogsResult>(result);
                    return blogsResult.blogs;
                }
            }
            catch (Exception)
            {

            }
            return results;
        }
                
    }
}
