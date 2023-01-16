from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import base64
from io import BytesIO


# Create your views here.


def Home(request):
    return render(request, 'base.html')


def Visualisasi1(request):
    dfc = pd.read_csv('Preprocessing.csv')
    fig, ax = plt.subplots(figsize=(6, 6))
    sizes = [count for count in dfc['polarity'].value_counts()]
    labels = list(dfc['polarity'].value_counts().index)
    explode = (0.1, 0, 0)
    ax.pie(x=sizes, labels=labels, autopct='%1.1f%%',
           explode=explode, textprops={'fontsize': 14})
    ax.set_title(
        'Sentiment Polarity on Tweets Data \n (total = 23699 tweets)', fontsize=16, pad=20)
    save = plt.savefig('Image/image.png')
    plt.show()
    return render(request, 'base.html')


def Visualisasi2(request):
    dfc = pd.read_csv('Preprocessing.csv')
    by_day = pd.to_datetime(dfc['Date']).dt.to_period(
        'D').value_counts().sort_index()
    by_day.index = pd.PeriodIndex(by_day.index)
    df_day = by_day.rename_axis('day').reset_index(name='counts')

    pd.plotting.register_matplotlib_converters()

    ## plot results ##
    f = plt.figure()
    f.set_figwidth(12)
    f.set_figheight(4)
    plt.plot(df_day.index, df_day.counts)
    plt.xticks(df_day.index, df_day.day)
    plt.xticks(rotation=60)
    # plt.legend()
    plt.ylabel('# of tweets')
    plt.xlabel("time")
    plt.show()
    return render(request, 'base.html')
