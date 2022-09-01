import time
import threading
import loger
from codigo import app_client, executionrow


def sistray():
    loger.logger.info("forming the systray")
    from codigo import interface

def socket_test():
    loger.logger.info("sending request to server")
    app_client.run_client("test", "morpheus")

threading.Thread(target=sistray).start()

loger.logger.debug("begining the loop")

while True:
    loger.logger.debug("doing the loop") 
    #threading.Thread(target=socket_test).start()
    
    app_client.run_client("test", "morpheus")
    executionrow.do_all()
    time.sleep(10)