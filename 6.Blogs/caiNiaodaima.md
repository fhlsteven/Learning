# 代码优化

## 背景

最近遇到线上的一个问题，问题描述是：当用户在某些场景点击按钮的时候没有反应，问题反应过来了，那就开查吧。

## 场景复现

按照提的问题，在开发环境走了一遍完美复现，发现js报错了，如下图：

![err1](./resources/err1.png)

![err2](./resources/err2.png)

## 报错代码

以下是定位到的报错js代码：

```js
var orderidstr = "";
var outstrArr = [];
for (i = 0; i < result.length; i++) {
    if (i == 0) {
        orderidstr = result[i].OrderId;
    } else {
        orderidstr = orderidstr + ',' + result[i].OrderId
        console.log(orderidstr)
    }
}

outstrArr = orderidstr.split(',');

for (let i = 0; i < outstrArr.length; i++) {
    for (let j = i + 1; j < outstrArr.length; j++) {
        if (outstrArr[i] == outstrArr[j]) {
            outstrArr.splice(j, 1);
            j--;
        }
    }
}
```

这个代码是我们前端(UI转的)写的，分析之后，发现当订单只有一个时候才会有问题，多个时候没有问题，这次需求正好是要更改多个订单。原因是当只有一个时候这段代码`orderidstr = result[i].OrderId;`最终不会是string，所以不会有`split`方法，要是写个`+=`也不会有这种问题。找到了原因之后就准备改代码。看了一下逻辑之后更是无语，大家自己看着体会，以下是优化后的代码。

```js
var outstrArr = [];
for (var i = 0; i < result.length; i++) {
    var orderId = result[i].OrderId;
    if (outstrArr.indexOf(orderId) === -1) {
        outstrArr.push(orderId);
    }
}
```

所以说代码写得多了出bug的概率就高了，前人果不欺我！！！

## ChatGPT 助力

在优化代码之前，我先用ChatGPT帮我优化了一下代码，以下是优化的过程：

**Me**： 优化一下

**ChatGpt**：

你的 JavaScript 代码主要用于将订单的 OrderId 字段合并并去重。以下是稍作优化的代码：

```js
const uniqueOrderIds = Array.from(new Set(result.map(item => item.OrderId)));
const orderidstr = uniqueOrderIds.join(',');

console.log(orderidstr);
```

此代码优化的主要点包括：

1. 使用 `Set` 数据结构来实现数组去重，避免了手动循环去重的操作。
2. 使用 `map` 函数从原始结果中提取订单号。
3. 使用 `join` 方法将唯一订单号数组合并为逗号分隔的字符串。

这样的写法更为简洁，减少了重复代码，同时更容易理解。

**Me**： 通用一点的优化 这个有些低版本不支持

**ChatGpt**：

确实，如果要考虑低版本浏览器的支持，可以使用一些通用的 JavaScript 代码。以下是一个更通用的实现：

```js
var uniqueOrderIds = [];
for (var i = 0; i < result.length; i++) {
    var orderId = result[i].OrderId;
    if (uniqueOrderIds.indexOf(orderId) === -1) {
        uniqueOrderIds.push(orderId);
    }
}

var orderidstr = uniqueOrderIds.join(',');

console.log(orderidstr);
```

这里使用了 `indexOf` 来检查数组中是否已存在相同的订单号，如果不存在，则将其添加到数组中。虽然这种实现相对简单，但在低版本浏览器中仍然能够正常运行。

## 总结

1. 代码尽量精简一点；代码写多了，出bug的概率就高了。
2. 测试场景不能只测本次需求，还需要多覆盖点。
3. 可以借助一些工具，比如GPT提高工作效率。
