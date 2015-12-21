Title: 为网站选择JavaScript和CSS的静态资源服务器
Date: 2015-12-21 20:14
Slug: choose-a-cdn-service-for-js-and-css
Authors: David Xie

web开发中, 很重要的一步就是使用CDN服务. 选择一个好的CDN服务, 网站响应速度可以提升很多.

很多大公司或者大网站, 由于不差钱, 可以选择很多商业的解决方案, 但是开源网站和小的创业项目, 就没那么多钱投资这个了. 所以选择也少了很多.

国内提供公有CDN服务的网站也不多, 比较出名的就是七牛了. 可惜它的HTTPS证书实在是太坑人了, 居然是12306的证书. 尽管速度很快, 但是https下的资源完全不可用, 没有办法, 只能放弃了.

于是代码段选择了国外的一个CDN服务商, 也就是大名鼎鼎的cdnjs了. 具体网址是[https://cdnjs.cloudflare.com/](https://cdnjs.cloudflare.com/).

访问上面的网站, 搜索自己想要的javascript或者css库, 把得到的`http`或者`https`拷贝下来即可. 这里有一个小技巧就是去掉地址里的`http:`或者`https:`, 可以让浏览器根据你的网站来选择是使用`http`还是`https`链接. 比如说, twitter-bootstrap的css地址是`https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css`, 我们把`https:`去掉, 得到`//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css`, 放进`link`标签的`href`属性里即可.

完整的例子:
```
<link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
```
