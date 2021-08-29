function killChildProcess() {
    // 发消息，由html的按钮调用，给主进程发消息，回调中关闭进程
    const ipcRenderer = require('electron').ipcRenderer;
    ipcRenderer.send('kill-child-now', 'get async message');
}