# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:40:06 2019

@author: Kritesh
"""

import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup
import re

def start(keyword):
    res = requests.get('https://bing.com/search?q='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #print(soup)
    links = soup.select('cite')
    #print(links)
    
    tab_counts = min(10, len(links))
    #print(tab_counts)
    for i in range(tab_counts):
        if(i== 4):
            continue;
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', str(links[i]))
        s=cleantext[:4]
        if(s!='http'):
            continue
        #print(cleantext)
        #print("  ")
        if(cleantext=='educate-yourself.org/vcd/swinefluindex.shtml'):
            continue
        link =cleantext
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # writing content of each page to a text file
        name = "paragraph" + str(i) + ".txt"
        with open("C:\\Users\\kritesh\\Desktop\\Project\\Bing\\paragraph\\" + name, 'w') as filehandle:
            for x in soup.find_all('header'):
                filehandle.write(x.get_text() + "\n")
            for x in soup.find_all('p'):
                filehandle.write(x.get_text() + "\n")


        #print(links[i])
        #print(" ")
        #webbrowser.open(str(cleantext))

start("swine flu vaccine")

import nltk

#nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')


def tagger():
    for i in range(1, 11):
        # print("2")
        name = "paragraph" + str(i) + ".txt"
        try:
            file = open("C:\\Users\\kritesh\\Desktop\\Project\\Bing\\paragraph\\" + name, 'r')
        except:
            continue
        words = []
        query_tagged = []
        while True:
            # print("3")
            query = file.readline()
            if query == "":
                break
            text = nltk.word_tokenize(query)
            list_tagged = nltk.pos_tag(text)
            # print(list_tagged)
            r = ""
            for obj in list_tagged:
                r = r + obj[0] + "_" + obj[1] + " "

            query_tagged.append(str)

            i = 0
            while i < len(list_tagged):
                # print("1")
                cur = list_tagged[i][1][0]
                wr = []
                while i < len(list_tagged) and list_tagged[i][1] == "CD":
                    wr.append(list_tagged[i][0])
                    i = i + 1
                if i >= len(list_tagged) or list_tagged[i][1][0] not in ('N', 'J', 'V'):
                    for j in range(len(wr)):
                        strt = ""
                        for k in range(j, len(wr)):
                            strt = strt + wr[k]
                            # print(strt)
                            words.append(strt)
                            strt = strt + " "
                        i = i + 1
                        continue
                else:
                    cur = list_tagged[i][1][0]
                if cur not in ('N', 'J', 'V'):
                    i = i + 1
                    continue
                while i < len(list_tagged) and (cur == list_tagged[i][1][0] or list_tagged[i][1] == "CD"):
                    wr.append(list_tagged[i][0])
                    i = i + 1
                    # print("4")
                    for j in range(len(wr)):
                        strt = ""
                        for k in range(j, len(wr)):
                            #print("5")
                            strt = strt + wr[k]
                            # print(strt)
                            words.append(strt)
                            strt = strt + " "

        with open('C:\\Users\\kritesh\\Desktop\\Project\\Bing\\paragraph tagged\\test_extended.txt', 'a') as filehandle:
            for i in words:
                filehandle.write('%s\n' % i)

        with open('C:\\Users\\kritesh\\Desktop\\Project\\Bing\\paragraph tagged\\test_tagged.txt', 'a') as filehandle:
            for i in query_tagged:
                filehandle.write('%s\n' % i)


tagger()
