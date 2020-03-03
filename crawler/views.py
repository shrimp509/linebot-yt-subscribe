# -*- coding: utf-8 -*-

from django.shortcuts import render

from bs4 import BeautifulSoup
import requests, time, cloudscraper
from selenium import webdriver


def crawl_subscribes_of_youtuber(name):
    base_url = "https://socialblade.com/youtube/user/" + str(name)
    print(base_url)
    agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    r = requests.get(base_url, headers=agent)
    soup = BeautifulSoup(r.text, 'html.parser')
    all = soup.select("div.YouTubeUserTopInfo span")
    print("all's size: ", len(all))

    if len(all) <= 0:
        base_url = "https://socialblade.com/youtube/search/search?query=" + str(name) + "&error=not-found"
        print("new url: ", base_url)
        new_body = cloudscraper.create_scraper().get(base_url).text

        soup = BeautifulSoup(new_body, 'html.parser')
        channel_all = soup.select("div h2 a")
        if len(channel_all) <= 0:
            return "我找不到這位 Youtuber QQ"
        else:
            subscribe_all = soup.select("div p span")
            return channel_all[0].text + " 的 訂閱數是 " + subscribe_all[1].text
    else:
        return name + " 的訂閱數是 " + all[4].text

