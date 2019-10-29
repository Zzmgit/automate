# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zhangzheming
@Version        :  
------------------------------------
@File           :  gitHub.py
@Description    :  
@CreateTime     :  2019/10/28 16:34
------------------------------------
@ModifyTime     :  
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class GitHub(object):
    def __init__(self):
        chrome_driver = r'D:\spaces\chromedriver_77_3865_10.exe'
        self.browser = webdriver.Chrome(executable_path=chrome_driver)
        self.path = '../report'
        self.current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.save_time = time.strftime("%Y-%m-%d~%H", time.localtime(time.time()))
        self.directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.save_path = '{}'.format(self.path)

    def login(self, url, username, password):
        self.browser.get(url=url)
        self.browser.find_element_by_id('login_field').send_keys(username)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_name('commit').click()

    def search(self, url, keyword):
        self.browser.get(url)
        ele_input = self.browser.find_element_by_name('q')
        ele_input.send_keys(Keys.BACK_SPACE)
        ele_input.send_keys(keyword)
        ele_input.send_keys(Keys.ENTER)

    def data_path(self):
        try:
            isExists = os.path.exists(self.save_path)
            if not isExists:
                os.makedirs(self.save_path)
                print(self.save_path + ': 创建成功')
            else:
                print(self.save_path + ': 目录已存在')
        except BaseException as e:
            print('新建目录失败: %s' % e)

    def data_file(self):
        path = self.save_path
        if not os.path.exists(path):
            os.makedirs(path)
        info_file = '{}/{}h.txt'.format(path, self.save_time)
        return info_file

    def write_url(self, search_url):
        a_val = self.browser.find_elements_by_xpath('//a[@class="v-align-middle"]')
        for val in a_val:
            if val.text is not '':
                with open(self.data_file(), 'a', encoding='utf-8') as f:
                    f.write('Time: {}    Repository: {}{}\n'.format(self.current_time, search_url, val.text))

    def write_title(self, keyword):
        with open(self.data_file(), 'a', encoding='utf-8') as f:
            f.write('\nSearch keywords: ***{}***\n'.format(keyword))

    def is_element_exist(self, by):
        try:
            self.browser.find_element_by_xpath(by)
        except NoSuchElementException:
            return False
        else:
            return True

    def save_data(self, keyword, search_url):
        if self.is_element_exist('//div[@class="paginate-container codesearch-pagination-container"]'):
            page_num = self.browser.find_element_by_class_name('current').get_attribute('data-total-pages')
            self.write_title(keyword)
            self.write_url(search_url)
            time.sleep(1)
            for i in range(0, int(page_num) - 1):
                self.browser.find_element_by_class_name('next_page').click()
                time.sleep(2)
                self.write_url(search_url)
        else:
            self.write_title(keyword)
            self.write_url(search_url)
        self.browser.quit()
