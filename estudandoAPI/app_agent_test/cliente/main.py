import time
import threading
import loger
from codigo import app_client, executionrow,interface


def sistray():
    loger.logger.info("forming the systray")
    interface.interface()


def socket_test():
    while True:
        loger.logger.debug("doing the loop")
        loger.logger.info("sending request to server")
        app_client.run_client("config")
        executionrow.do_all()
        time.sleep(100)

threading.Thread(target=socket_test).start()
sistray()

