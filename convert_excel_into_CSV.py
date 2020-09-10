import pandas as pd
import os 
 
#查找符合文件类型的文件
def file_name(file_dir,source_type):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == source_type:  
                L.append(os.path.splitext(file)[0])  
    return L 
 
#将excel文档转为csv文档 
def excel_to_csv(file,to_file):
    #read_excel中sheetname含义
    #default 0 返回多表使用sheetname=[0,1],若sheetname=None是返回全表 
    
    #read_excel中header含义
    #default 0 指定列名行，默认0，即取第一行，数据为列名行以下的数据 ，若数据不含列名，则设定 header = None
    file_excel=pd.read_excel(file,sheetname=0)
    file_excel.to_csv(to_file,index=False)
    
if __name__=='__main__':
    #原文档所在目录
    source_path='E:\\test'
    #转换文档存储目录
    object_path='E:\\test1'
    #原文档格式类型
    source_type='.xls'
    #转换格式类型
    object_type='.csv' 
    file_list=file_name(source_path,source_type)
    for i in file_list:
        file=source_path+'\\'+i+source_type
        to_file=object_path+'\\'+i+object_type
        excel_to_csv(file,to_file)
