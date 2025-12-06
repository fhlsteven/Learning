
from testSel import get_driver

from common import wait_time

from configs import configs
from datetime import datetime
from play_normal import PlayNormal

if __name__ == '__main__':
    print(configs.login.url)
    driver = get_driver(configs.login.url)
    wait_time(2)
    while True:
        PlayNormal(driver).playNormal()
        wait_time(2)