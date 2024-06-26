# 移动云盘自动化任务程序操作手册

## 项目介绍



## 1.获取token变量

安卓手机：点击链接下载alook浏览器。

苹果手机：app store去下载Alook浏览器 需要8r，自行考虑。

可选择模拟器操作。

### 操作步骤

1）打开无痕模式![](images/1.png)

2）输入链接https://yun.139.com/m/#/main?linkshare=1登录移动云盘账号

3）点击中心选项

![](images/2.png)

4)找到工具箱

![](images/3.png)

5)选择开发者工具

![](images/4.png)

6）开发者工具中选择cookies，然后复制cookies

在cookies中找到：authorization，并复制其中内容

![](images/5.png)
## 2.token格式

Token格式为：

![](images/6.png)
authorization中的basic-==#所登录移动云盘账号的手机号#00
