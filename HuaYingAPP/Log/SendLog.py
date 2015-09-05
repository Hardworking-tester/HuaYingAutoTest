#encoding:utf-8
import logging
class ResultLog():
    def writeLog(self):
        log_path="E:\\testlog\\resultlog.txt"
        log=logging.getLogger("wwg")
        log.setLevel(logging.INFO)
        filehandler=logging.FileHandler(log_path)
        formatter=logging.Formatter("%(asctime)s:%(module)s- %(funcName)s-%(lineno)d %(message)s","%Y年%m月%d日 %H:%M:%S")
        filehandler.setFormatter(formatter)
        log.addHandler(filehandler)
        return log