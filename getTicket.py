# -*- coding:utf-8 -*-

from splinter.browser import Browser
import time


url = 'http://www.228.com.cn/auth/login'
order_url = 'http://www.228.com.cn/ticket-225637356.html'

#login
def login(b):
    b.fill('username','18538556114')
    b.fill('password','QP19910425')
    b.find_by_id('loginsubmit').click()
    time.sleep(2)
    return b

#order
def loop(b):
    try:
        if b.title =='【票务演出票务演出订票票务网】_永乐票务_确认订单信息_立即购买':
            b.find_by_text('支付平台').click()
            b.find_by_value('2217200').first.click()
            b.find_by_id('saveOrder').click()
            print('订单已提交！')
            return b
        else:
            b.visit(order_url)
            b.find_by_xpath('//*[@id="Jprice"]/li[6]').click()
            b.find_by_xpath('/html/body/div[11]/div[2]/div[4]/div[5]/a')
            time.sleep(5)
            loop(b)
    except Exception as e:
        b.reload()
        time.sleep(1)
        loop(b)



b = Browser(driver_name='chrome')
b.visit(url)
login(b)
b.visit(order_url)
b.find_by_xpath('//*[@id="Jprice"]/li[6]').click()
b.find_by_xpath('/html/body/div[11]/div[2]/div[4]/div[5]/a').click()
time.sleep(5)
while True:
    loop(b)
    if b.title=='【五月天郑州演唱会门票】2017五月天 LIFE [ 人生无限公司 ] 巡回演唱会—郑州站-永乐票务':
        b.find_by_xpath('//*[@id="Jprice"]/li[6]').click()
        b.find_by_xpath('/html/body/div[11]/div[2]/div[4]/div[5]/a')
        time.sleep(2)
        loop(b)
    else:
        print('SUCCESS!')
        break






