<!--
 * @Author: mokevip
 * @Date: 2020-09-14 13:54:03
 * @LastEditors: mokevip
 * @LastEditTime: 2020-09-14 14:26:26
 * @Description: 
-->
# 爱艹题

一个由爱刷题魔改的无数据库的刷题H5应用

~~别问我为什么起这么生草的名字。我也想不出更好的名字了（捂脸）~~

---

### 原作者的话
迫于最近需要考试，平时碎片化时间较多，并不能合理利用碎片化时间。便想着可以用类似于```驾考宝典```的应用帮助自己充分利用碎片化时间。

于是将试卷WORD整理出来，导入了一些刷题网站（如```刷刷题```、```考试宝```等），发现，都是需要收费的，可能一周就要10元。

逐到GITHUB搜索，可能因为姿势不正确，并没有找到合适的仓库。
被逼无奈，只好自己上手。做好了之后也可以分享给大家，共同学习共同努力。

### zhengfan2014的修改
 - 改MDUI主题，适配电脑端和手机端

### 特色内容
 - 无后端、无数据库轻量化部署简单
 - 使用JSON作为题库存储，层次清晰，结构简单易懂
 - 有配套的word模板和模板到JSON转换工具
 - 四种刷题模式：顺序刷题、乱序刷题、错题模式、背题模式


### 主要结构
 - index.html      主页，显示题库列表
 - type.html       刷题模式选择页面，可选四种模式
 - timu.html      刷题页面
 - **json/*.json**    存储题库
 - js/public.js     js数组对应JSON题库的文件路径和描述信息ID等
 - py-timuToJson    转换JSON的模板和脚本


**注：下载后双击index.html是无法直接食用的，需要配合web服务（如静态资源服务器或live-server等）食用**

### 效果预览

演示站：[https://zhengfan2014.github.io/aishuati/](https://zhengfan2014.github.io/aishuati/)


效果图：
![](https://github.com/zhengfan2014/aishuati/raw/master/docs/img/1.png)
![](https://github.com/zhengfan2014/aishuati/raw/master/docs/img/2.png)
![](https://github.com/zhengfan2014/aishuati/raw/master/docs/img/3.png)
![](https://github.com/zhengfan2014/aishuati/raw/master/docs/img/4.png)
![](https://github.com/zhengfan2014/aishuati/raw/master/docs/img/5.png)
![](https://github.com/zhengfan2014/aishuati/raw/master/docs/img/6.png)