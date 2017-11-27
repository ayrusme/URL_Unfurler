"""Python Script to generate a thumbnail of a webpage"""

__author__ = "Surya Raman"
__license__ = "MIT"

import sys

import requests as rq
from bs4 import BeautifulSoup
from newspaper import Article

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
    """Function to get the title from the soup object"""
    title = soup.find("meta", property="og:title")['content']
    if title == "" or title is None:
        title = soup.find("title")['content']
    return title

def get_url(soup):
    """Function to find the URL from the soup object"""
    return soup.find("meta",  property="og:site_name")['content']

def get_description(soup):
    """Function to get the description from the soup object"""
    description = soup.find('meta', property='og:description')['content'] 
    if description is None or description == "":
        description =  soup.find('meta', attrs={'name':'description'})['content']
    return description

def get_date_time(webpage_url):
    """Function to get the date and time from the webpage"""
    article = Article(webpage_url)
    article.download()
    article.parse()
    return article.publish_date.strftime('%d %B %Y')

def get_preview_image(soup):
    """Function to get the description from the soup object"""
    return soup.find('meta', property='og:image')

def get_favicon(soup):
    """Function to get the favicon from the soup object"""
    if soup.find('link', rel='shortcut icon'):
        return soup.find('link', rel='shortcut icon')['href']
    elif soup.find('link', rel='icon'):
        return soup.find('link', rel='icon')['href']