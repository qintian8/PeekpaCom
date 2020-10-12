# Peekpa.com

欢迎大家来到皮爷撸码的Peekpa.com源代码。

### 下载源码

使用终端（Terminal），并配合`git clone`命令，可将源码下载到本地：

```shell
$ git clone https://github.com/SwyftG/PeekpaCom.git
```

### 【重要】怎样启动

如何在本地成功启动本地版的Peekpa.com，前提条件，需要在本地计算机安装docker和docker-compose。

[《如何安装docker》请看这里官方文档](https://docs.docker.com/get-docker/)

当安装完docker之后，在终端进入到目录下面，首先切换到`for_docker_image`:

```shell
$ git checkout for_docker_image   #切换到remotes/origin/for_docker_image分支
```

然后直接通过`docker-compose up`命令启动：

```shell
$ docker-compose up   # 本地化启动peekpa.com
```

停止运行，则需要输入`docker-compose down`命令：

```shell
$ docker-compose down   # 停止本地化peekpa.com运行
```


### 阿里云线上部署

想要将代码部署到阿里云服务器，可以参考以下两篇文章：

准备服务器（内含购买服务器优惠码）：

- [《用Django全栈开发——28. 部署之准备服务器》](https://mp.weixin.qq.com/s?__biz=MzU3NDgzMTM4OA==&mid=2247484505&idx=1&sn=73b69a065de0662efb9b404f0b0900e8&chksm=fd2d2a2aca5aa33cd74d8bff98619c77eb23fc677e5b7b1f8f87857b13b8b57d0fd451c55542&token=1828688355&lang=zh_CN#rd)


具体的部署操作：

- [《用Django全栈开发——29. 部署之阿里云CentOS+Nginx+uWsgi+Django(上)》](https://mp.weixin.qq.com/s?__biz=MzU3NDgzMTM4OA==&mid=2247484560&idx=1&sn=26d3f0dcff62e89c58bb4ecb0b7e7272&chksm=fd2d2ae3ca5aa3f5117506a54580d3f06942866e79d51cf26cb76eb2f50a8422b9e331797659&token=1828688355&lang=zh_CN#rd)

- [《用Django全栈开发——29. 部署之阿里云CentOS+Nginx+uWsgi+Django(下)》](https://mp.weixin.qq.com/s?__biz=MzU3NDgzMTM4OA==&mid=2247484560&idx=2&sn=952a495a30827c9d581adf3490189592&chksm=fd2d2ae3ca5aa3f5a7134eb55b8ad9b4d850c825b39078e944b68d0bf5dd0efc23b808d304fd&token=1828688355&lang=zh_CN#rd)

### 未完待续。。。

获取更多精彩信息，请关注微信公众号『皮爷撸码』，用代码将生活变得简单。

![](https://raw.githubusercontent.com/SwyftG/PeekpaComPostImage/master/z001/011.png)

