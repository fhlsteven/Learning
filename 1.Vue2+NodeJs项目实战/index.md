
# Vue2.0+NodeJS项目实战

## 1 课程介绍

### 1.1导学

* Vue框架对比
  1. [Vue](https://cn.vuejs.org)和[React](https://reactjs.org)目前都使用了Virtual DOM
  2. Vue
    * [github](https://github.com/vuejs/vue)
    * 模板和渲染函数的弹性选择
    * 简单的语法及项目创建
    * 更快的渲染速度和更小的体积
  3. React
    * [github](https://github.com/facebook/react)
    * 更适用于大型应用和更好的可测试性
    * 同时适用于Web端和原生App
    * 更大的生态圈带来的更多支持和工具
  4. Vue和React相同点
   * 利用虚拟DOM实现快速渲染
   * 轻量级
   * 响应式组件
   * 服务器端渲染
   * 易于集成路由工具，打包工具以及状态管理工具
   * 优秀的支持和社区

### 1.2前端框架回顾
   * [DOJO](https://github.com/dojo)![dojo](source/1/dojo-logo.svg)
   * [SpineJS](http://spinejs.com/)
   * [EmberJS](https://emberjs.com)![EmberJS](source/1/ember-logo.svg)
   * [prototype](http://prototypejs.org)
   * [backbone.js](https://www.backbonejs.com.cn)
   * [React](https://react.docschina.org)
   * [Vue](https://vuejs.org)

   + 模块化的开发框架  require.js 异步加载JS
   + 基于DOM操作的函数库 JQuery
   + 基于MVC模式的Spine框架
      - Model和View解耦
      - Controller控制DOM
      - 完全照搬MVC模式
   + 基于MV*模式的Vue框架
     - Model绑定View
     - 没有控制器概念
     - 数据驱动，状态管理

### 1.3 Vue概括核心思想
Vue本身并不是一个框架
Vue结合周边生态构成一个灵活的、**渐进式**的框架
声明式渲染(Declarative Rendering)-->组件系统(Component System)-->客户端路由(Client-Side Routing)-->大规模状态管理(Large Scale State Management)-->构建工具(Build System)

核心思想
* 数据驱动：数据绑定，不需要关注Dom操作
* 组件化

通过MVVM的数据绑定实现自动同步</br>
View(DOM)  ViewModel(Vue)   Model(POJO:原生JS对象) 

Vue组件化

Vue组件树

Vue如何实现双向数据绑定？ Object.defineProperty()

### 1.4 Vue的优点对比
  
 * 前端
   + 视图层：商品列表 购物车 地址列表 商品结算 订单成功
   + Vue.js - MVVM(公共组件；Vue-Router；Axios；Vuex；Util；依赖)
   + 工具支持 （vue-cli webpack）
 * 后端 (Node Express)
 * 数据库 (MongoDB)

 前置知识：**Html/CSS/JS** ;**Vue** ; **ES6**; **Node** ; **Npm** ; **Webpack**

---

## 2 Vue基础

### 2-1 nodeJS和Npm的安装和环境搭建
 * Webpack:代码模块化构建打包工具
 * Glup:基于流的自动化管理工具
 * Grunt: JavaScript世界的构建工具
 * Babel：使用最新的规范来编写js
 * Vue： 构建数据屈工的Web界面的渐进式框架
 * Express：基于node.js平台，快速、开放、极简的web开发框架

[Nodejs Download](https://nodejs.org/en/download)

cnpm是npm的一个淘宝镜像，主要是为了更快（-g 是全局安装）
```bat
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

npm 升级

`npm install -g npm`

cnpm安装Vue模块

`cnpm i vue --save` or `cnpm install vue --save`

cnpm 查看引用的包

`cnpm list`

### 2-2 Vue环境搭建以及vue-cli使用

Vue多页面应用文件引用
  * 官网拷贝：`<script src="https://unpkg.com/vue/dist/vue.js"></script>`
  * npm安装  `npm i vue --save`
    页面引用`<script src="node_modules/vue/dist/vue.min.js"></script>`

vue-cli构建SPA应用
  * npm install -g vue-cli
  * vue init webpack-simple learnOne
  * vue init webpack learnT


[Vue 官网](https://vuejs.org/v2/guide/installation.html)

安装Vue Client 脚手架  `cnpm i -g vue-cli`

初始化 简单的webpack的简单项目 `vue init webpack-simple Demo5` 
`vue init webpack Demo6demo`



[mustcache语法](https://zhuanlan.zhihu.com/p/36572041)一些解释

  ```
  Mustache是一个logic-less（轻逻辑）模板解析引擎，

它是为了使用户界面与业务数据（内容）分离而产生的，

它可以生成特定格式的文档，通常是标准的HTML文档。

比如小程序的wxml中的代码

{{userInfo.nickName}}，这里的{{ }}就是Mustache的语法。
Mustache的模板语法很简单，就那么几个：

{{keyName}}
{{{keyName}}}
{{#keyName}} {{/keyName}}
{{^keyName}} {{/keyName}}
{{.}}
{{!comments}}
{{>partials}}
1、{{keyName}}简单的变量替换。

2、{{#keyName}} {{/keyName}}以#开始、以/结束表示区块，它会根据当前上下文中的键值来对区块进行一次或多次渲染。它的功能很强大，有类似if、foreach的功能。

3、{{^keyName}} {{/keyName}}该语法与{{#keyName}} {{/keyName}}类似，不同在于它是当keyName值为null, undefined, false时才渲染输出该区块内容。

4、{{.}} {{.}}表示枚举，可以循环输出整个数组

5、{{! }}表示注释

6、{{>partials}}以>开始表示子模块，当结构比较复杂时，我们可以使用该语法将复杂的结构拆分成几个小的子模块。
  ```

### 2-3 Vue配置介绍

webpack 项目

1. build  -- 打包的配置文件
   * build.js  -- 打生产的包
   * check-versions.js  
   * utils.js
   * vue-loader.conf.js
   * webpack.base.conf.js  -- 重点关注
   * webpack.dev.conf.js
   * webpack.prod.conf.js
2. config -- 打包的配置，webpack对应的配置
   * dev.env.js
   * index.js   -- 重点关注
   * prod.env.js
3. src   -- 开发项目的源码
   * assets
   * components
   * router
   * App.vue  -- 入口组件
   * main.js  -- 项目入口文件
4. static  -- 放静态资源，图片等
5. .babelrc  -- ES6解析配置
6. .editorconfig  -- 编辑器配置
7. .postcssrc.js  -- HTML 添加前缀的一个配置
8. index.html     -- 单页面应用程序入口 SPA
9. package.json   -- 基础配置
10. README.md     

Vue 不同版本的规范 veu.js;vue.common.js;vue.esm.js


### 2.4 Vue基础语法介绍
 模板语法
 * Mustache语法：`{{ msg }}`
 * Html赋值：`v-html=""`
 * 绑定属性：`v-bind:id=""`
 * 使用表达式：`{{ ok ？'YES':'NO'}}`
 * 文本赋值：`v-text=""`
 * 指令：`v-if=""`
 * 过滤器：`{{ message | capitalize }}`和`v-bind:id="rawId | formatId"`

Class和Style绑定
* 对象语法： `v-bind:class="{ active:isActive,'text-danger':{hasError }">`
* 数组语法：
 ```html
 <div v-bind:class="{activeClass,errorClass}">
 data:{
   activeClass:'active',
   errorClass:'text-danger'
 }
 ```
 * style绑定-对象语法：`v-bind:style="{color:activeColor,fontSize:fontSize+'px'}"` 