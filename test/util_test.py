#-*- coding:utf-8 -*-
##
# @file util_test.py
# @brief 辅助单元测试的一些工具
# @author 
# @version 
# @date 2012-06-17

import os

def clearLog(logger):
    """如果产生的日志存在为空，则将其清除，包括其目录log
    """
    ret = 0;

    for handler in logger.handlers:
        handler.stream.flush();
        handler.stream.close(); # 关闭才能释放文件控制
        log_path = handler.stream.name;
        logger.removeHandler(handler); # 移除以避免最后程序退出时logger调用flush找不到相应的open文件
        del handler;

        #print log_path;
        if(os.path.exists(log_path)):
            if(0==os.path.getsize(log_path)):
                os.remove(log_path);

        log_dir = os.path.dirname(log_path);
        #print log_dir;
        if(os.path.exists(log_dir)):
            os.rmdir(log_dir);

    return ret;

def clearLog_log_ana(log_anas=[]):
    """ 对 log_ana 类产生的空文件进行清理
    """
    for l in log_anas:
        clearLog(l.logger);
        if(hasattr(l,'sql_fail_log')):
            if(os.path.exists(l.sql_fail_log)):
                if(0==os.path.getsize(l.sql_fail_log)):
                    os.remove(l.sql_fail_log);
        del l;
       



