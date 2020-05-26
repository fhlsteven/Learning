
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
   * [DOJO](https://github.com/dojo)![dojo](/source/1/dojo-logo.svg)
   * [SpineJS](http://spinejs.com/)
   * [EmberJS](https://emberjs.com)![EmberJS](/source/1/ember-logo.svg)
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
Vue结合周边生态构成一个灵活的、渐进式的框架
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


## 2 Vue基础
