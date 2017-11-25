"""Python Script to generate a thumbnail of a webpage"""

import sys

import requests as rq
from bs4 import BeautifulSoup

def send_request(url):
    """Function to get the html page"""
    try:
        resp = rq.get(url)
        return resp, "success"
    except Exception as exp:
        return None, exp        

def get_soup_object(resp):
    """Function to instantitate a BeautifulSoup Object"""
    return BeautifulSoup(resp.content, "html.parser")

def get_title(soup):
    """Function to get the title of the html page"""
    title = soup.find("meta", property="og:title")['content']
    if title == "" or title is None:
        title = soup.find("title")['content']
    return title

def get_url(soup):
    """Function to find the URL of the webpage"""
    return soup.find("meta",  property="og:url")['content']
