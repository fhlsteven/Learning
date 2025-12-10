namespace GGApp.Common
{
    public interface IBrowserAutomation
    {
        bool IsReady { get; }

        string Init();
        string Navigate(string url);
        string Click(int x, int y, bool leftClick = true);
        //void ClickElement(By selector);
        //void SendKeys(By selector, string text);
        string Screenshot(string savePath);
        string Quit();
        void SetWindow(int width, int height, int x, int y);
    }
}