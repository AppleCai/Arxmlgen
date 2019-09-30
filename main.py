'''
@Description: Arxmlgen
@Version: V1.0
@Autor: AppleCai
@Date: 2019-09-30 21:09:53
@LastEditors: AppleCai
@LastEditTime: 2019-09-30 21:09:53
'''
import pandas as pd
from myPortInterface.PortInterfaces_api import portInterfaceXMLgen
from mySWC_xml.mySWC_api import swcXMLgen

def saveToFile(df):
    df.to_excel('SWC.xls',sheet_name="SWC",encoding='utf-8',index = False)

if __name__ == '__main__':
    swclist=swcXMLgen(r'mySWC_xml\mySWC.xml')
    iflist=portInterfaceXMLgen(r'myPortInterface\PortInterfaces.xml')
    dfswc = pd.DataFrame(swclist)
    dfif = pd.DataFrame(iflist)
    #del dfif['InterfaceName']
    dd = pd.merge(dfswc,dfif,how='inner') # 左边是swc，采用内部合并不会超过swc的项
    saveToFile(dd)





