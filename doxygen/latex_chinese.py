#-*- coding:utf-8 -*-    

##
# @file latex_chinese.py
# @brief 用于修改doxygen产生的latex源码，以避免中文乱码
# @author wangwei, wangwei15@baidu.com
# @version 1
# @date 2012-04-26

import os
import sys
import re
import time

def rewrite_file(filepath, stext, rtext):
    """根据指定条件 修改文件内容 """
    if(os.path.exists(filepath)):
        data = open(filepath).read()
        data = re.sub(stext, rtext, data) #stext替换为rtext
        #print data

        # test
        #tRes = re.search(stext,data); 
        #print tRes;

        open(filepath, 'wb').write(data)
        print filepath,"was rewrite!"
    else:
        print "error: ",filepath," is not exists!";
    
if(__name__=="__main__"):

    """
1. make.bat中3处有
pdflatex refman 部分改成 
xelatex refman
    """
    batfile="latex/make.bat";
    rewrite_file(batfile,r"pdflatex",r"xelatex");

    """
2. 在refman.tex 文件的\usepackage{doxygen}之后添加
\usepackage{ctex}
    """
    texfile="latex/refman.tex";
    rewrite_file(texfile,r"(\usepackage{doxygen})","\g<1>\n\r\\usepackage{ctex}");

    time.sleep(3);
