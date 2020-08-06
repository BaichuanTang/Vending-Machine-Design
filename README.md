##### 1. 项目描述

能量站，是集人脸识别、目标检测以及数据库等技术于一体的自动售货柜。相比于传统自动货柜，能量站运行的系统能够做到精准识别、精准投放、精准操作。CNN的人脸识别技术与目标检测技术能让售货柜“认得”用户，实现人脸登陆与自助购买。可视化数据分析、用户友好型的操作让系统能更易于上手，便于管理。基于Diagia QT5框架Pyqt5以及MySQL开发的系统也为后续功能的新增与维护带来了极大的便利。

目前可用的版本为v0.1.0，如果你想快速了解系统的运行，可以使用我们的[在线DEMO](https://free.modao.cc/app/4f5a077c754d28186207f1dab6e5074c9cde89e7)。

##### 2. 项目的基本结构

1. 自动贩卖机管理系统——包含采购、配送、仓储、售后、财务以及维护等多个子系统，实现销售管理一体化。

   - 数据库E-R图

     ![image-20200806224856329](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806224856329.png)

   - 数据流程图

     ![image-20200806225740909](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225740909.png)

     ![image-20200806225754613](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225754613.png)

   - 财务页面

     ![image-20200806224923025](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806224923025.png)

   - 采购页面

     ![image-20200806225012666](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225012666.png)

   - 配送页面

     ![image-20200806225021360](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225021360.png)

   - 维护页面

     ![image-20200806225026388](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225026388.png)

   - 客服页面

     ![image-20200806225035204](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225035204.png)

2. 消费者系统——包含人脸识别登陆账户、自动检测选购商品以及自动结算等功能。实现了无人售货柜的基本功能。

   - 购买流程

     - 购买页面

       ![image-20200806225522933](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225522933.png)

     - 选购完成页面

       ![image-20200806225535032](http://jallery.oss-cn-beijing.aliyuncs.com/energystation/image-20200806225535032.png)

##### 3. 环境配置

| 开发工具       | 版本          |
| -------------- | ------------- |
| Python         | 3.6           |
| PyQt5          | 5.13.0        |
| MySQL          | 5.7.28-winx64 |
| tensorflow     | 1.12.0        |
| opencv_python  | 3.4.0.12      |
| tensorflow_gpu | 1.4.0         |
