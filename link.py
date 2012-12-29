#-*- coding:utf-8 -*-

import os  
import sys
import pythoncom  
from win32com.shell import shell  
from win32com.shell import shellcon 

#从.lnk文件中获取文件路径
def GetpathFromLink(lnkpath):  
    shortcut = pythoncom.CoCreateInstance(  
        shell.CLSID_ShellLink, None,  
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)  
    shortcut.QueryInterface( pythoncom.IID_IPersistFile ).Load(lnkpath)  
    path = shortcut.GetPath(shell.SLGP_SHORTPATH)[0]  
    return path 

#创建快捷方式
def CreateLnkpath(filename,lnkname):  
    if(not os.path.exists(filename)):
        return -1;
    shortcut = pythoncom.CoCreateInstance(  
        shell.CLSID_ShellLink, None,  
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    #filename=filename.decode('utf-8').encode('gbk');  
    #print filename
    shortcut.SetPath(filename)  
    if os.path.splitext(lnkname)[-1] != '.lnk':  
        lnkname += ".lnk"  
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname,0) 
    #print lnkname;
    return 0;

#创建url快捷方式
def CreateURLShortcut(url,name):  
    shortcut = pythoncom.CoCreateInstance(  
        shell.CLSID_InternetShortcut,None,  
        pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IUniformResourceLocator)  
    shortcut.SetURL(url)  
    if os.path.splitext(name)[-1] != '.url':  
        name += '.url'  
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(name,0) 

#从.url快捷方式获取url连接地址
def GetURLFromShortcut(url):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_InternetShortcut,None,
        pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IUniformResourceLocator)
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(url)
    url = shortcut.GetURL()
    return url

#获取桌面路径
def GetDesktoppath():  
    ilist = shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_DESKTOP)  
    dtpath = shell.SHGetPathFromIDList(ilist)  
    #dtpath = dtpath.decode('gbk')  
    return dtpath

if("__main__"==__name__):
    index_path = ''.join([os.getcwd(),'\doxygen\html\index.html']);
    print index_path 
    try:
        if(os.path.exists(index_path)):
            CreateLnkpath(index_path,os.path.basename(index_path));
        else:
            msg =''.join([index_path, '不存在，请重新生成!'])
            print msg.decode('utf-8').encode('gbk');
    except Exception, err_msg:
        print err_msg;

    #print index_path 

    import time
    time.sleep(3);
