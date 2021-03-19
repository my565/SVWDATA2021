# -*- coding: utf-8 -*- 
# @Time: 2021/3/16 10:31
# @Author: BB-Driver
# @File: word_cloud.py
# @Software: PyCharm

from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize



def main():
    # 数据加载
    data = './Market_Basket_Optimisation.csv'
    data = pd.read_csv(data, header=None)
    # 生成词云
    create_word_cloud(data)


def clear_nan(data):
    """
    去除nan的数据

    Parameters:
        data (DataFrame): 原始数据
    Returns:
        transactions(list): 无nan的数组
    """
    transactions = []
    for i in range(0, data.shape[0]):
        temp = []
        for j in range(0, 20):
            if str(data.values[i, j]) != 'nan':
                temp.append(str(data.values[i, j]))
        transactions.append(temp)
    return transactions


def create_word_cloud(transactions):
    """
    生成词云
    Parameters:
        data (DataFrame): 原始数据
    Returns:
        wordcloud(jpg): 词云图片
    """
    print('根据词频，开始生成词云!')
    transactions = clear_nan(transactions)  # 清除nan的数据
    all_word = ' '.join('%s' % item for item in transactions)  # 遍历数组
    cut_text = word_tokenize(all_word)  # 分词
    # print(cut_text)
    cut_text = " ".join(cut_text)
    wc = WordCloud(
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    main()