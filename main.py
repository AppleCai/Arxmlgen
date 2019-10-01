'''
@Description: Arxmlgen
@Version: V1.0
@Autor: AppleCai
@Date: 2019-09-30 21:09:53
@LastEditors: AppleCai
@LastEditTime: 2019-12-01 22:22:19
'''
import pandas as pd
from myPortInterface.PortInterfaces_api import portInterfaceXMLgen
from mySWC_xml.mySWC_api import swcXMLgen

def saveToFile(df):
	# 不需要保存df自动生成的index，所以设置为FALSE，sheet名称定义为SWC
    df.to_excel('SWC.xls',sheet_name="SWC",encoding='utf-8',index = False)

if __name__ == '__main__':
    # 获取SWC.arxml的信息
    swclist=swcXMLgen(r'mySWC_xml\mySWC.xml')
	# 获取所有Port Interface Datatype的信息。紧包括SRport
    iflist=portInterfaceXMLgen(r'myPortInterface\PortInterfaces.xml')
	# 将list转为pd，可以方便的进行数据库拼接
    dfswc = pd.DataFrame(swclist)
    dfif = pd.DataFrame(iflist)
    #del dfif['InterfaceName']
	# 左边是swc，采用内部合并不会超过swc的项
    dd = pd.merge(dfswc,dfif,how='inner')
    # 将拼接后的结果保存到文件文件中	
    saveToFile(dd)





