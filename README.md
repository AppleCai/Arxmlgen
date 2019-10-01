<!--
 * @Description: In User Settings Edit
 * @Author: your name
 * @Date: 2019-10-01 22:19:01
 * @LastEditTime: 2019-10-01 22:19:01
 * @LastEditors: your name
 -->
仅供自学，不能用于商用。
ArxmlgenV1.0功能描述

	读取vector developer生成的SWC中的port/interface/data element/date type的信息。
	此工程是我的第一版设计，所以功能有限，只是读取SR port的信息。

目录说明

	main.py是入口
	SWC.xls是生成的文件
    myXXX文件夹中的xxx.py就是generateDS自动生成的python api，让我修改了些调用函数进行的二次开发。他的函数先构造rootObj，我从rootObj中取出自己感兴趣的信息。
	
相关环境及工具链建立参考我的blog
	
	https://www.jianshu.com/p/8039cb2b54d3

