# -*- coding: utf-8 -*-
from selenium import webdriver
def a():
    err= []

    try:
        raise Exception('test')
    except Exception as e:
        err.append(e)
        print(e)
        raise
    finally:
        print(1)
        
a()