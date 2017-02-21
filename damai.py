# -*- coding:utf-8 -*-
from splinter.browser import Browser
import time

url_login = 'https://secure.damai.cn/login.aspx'
url_ticket = 'https://piao.damai.cn/116951.html'
sms = 'https://secure.damai.cn/CheckSafety.aspx'

def login(d):
    d.visit(url_login)
    d.fill('login_email','1＊＊＊＊＊')
    d.find_by_css('.layer_text')[1].click()
    d.fill('login_pwd','＊＊＊＊＊')
    d.find_by_css('.login_btn').click()
    time.sleep(3)
    return d


def order_confirm(d):
    if d.title == '订单结算页-大麦网':
        if d.is_element_present_by_text('身份证'):
            d.fill('PapersCard','＊＊＊＊＊＊＊＊')
            time.sleep(2)
        else:
            pass
        d.find_by_id('orderConfirmSubmit').click()
        time.sleep(5)
    else:
        login(d)
        d.reload()
        d.visit(url_ticket)
        d.find_by_text('内场1355').click()
        d.find_by_id('btnBuyNow').click()
        time.sleep(5)
        order_confirm(d)

def payment(d):
    if d.title == '选择支付方式':
        d.find_by_text('支付平台付款').click()
        d.find_by_value('213').first.click()
        time.sleep(1)
        d.find_by_id('submit2').click()
    else:
        d.reload()
        order_confirm(d)
        payment(d)

d = Browser(driver_name='chrome')
login(d)
time.sleep(5)
d.visit(url_ticket)
d.find_by_text('内场1355').click()
time.sleep(4)
d.find_by_id('btnBuyNow').click()
order_confirm(d)
payment(d)
time.sleep(3)
if d.title == '支付宝 - 网上支付 安全快速！':
    print('SUCCESS!')
else:
    print('RETRY PLEASE!')
