"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// study https://www.cnblogs.com/silenzio/p/11580267.html
const electron_1 = require("electron");
const path = require("path");
let mainWindow;
/**
 *
 */
function createWindow() {
    //  Create the browser window.
    mainWindow = new electron_1.BrowserWindow({
        height: 600,
        width: 800,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            // render.js Uncaught ReferenceError: require is not defined
            nodeIntegration: true,
            enableRemoteModule: true,
            contextIsolation: false
        }
    });
    // and load the index.html of the app.
    mainWindow.loadFile(path.join(__dirname, '../html/index.html'));
    // Open the DevTools.
    mainWindow.webContents.openDevTools({ mode: 'undocked' });
    // Emitted when the window is closed.
    mainWindow.on("close", () => {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        mainWindow = null;
    });
}
// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
electron_1.app.on('ready', createWindow);
// Quit when all windows are closed.
electron_1.app.on('window-all-closed', () => {
    // On OS X it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
        electron_1.app.quit();
    }
});
electron_1.app.on('activate', () => {
    // On OS X it"s common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (mainWindow === null) {
        createWindow();
    }
});
const httpServer = require('http-server');
// 创建一个 http 服务器， http://localhost:8080/html/
httpServer.createServer().listen(8080);
const WebSocketServer = require("ws").Server;
let wss = new WebSocketServer({ port: 12122 });
wss.on('connection', (ws) => {
    // 有客户端连接时, 打印一条日志
    console.log('client connected');
    // 并且创建'message'监听
    ws.on('message', (message) => {
        // 直接将消息打印出来
        console.log(message);
    });
});
const myChildProcess = require("child_process");
// 打开一个子进程notepad++
const mySpawn = myChildProcess.spawn('D:\\Program Files (x86)\\Notepad++\\notepad++.exe');
// In this file you can include the rest of your app"s specific main process
// code. You can also put them in separate files and require them here.
electron_1.ipcMain.on("kill-child-now", (e, appUrl) => {
    console.log(appUrl);
    mySpawn.kill();
});
//# sourceMappingURL=main.js.map