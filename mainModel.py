import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

city_to_country = {
        'zagreb': 'croatia',
        'berlin': 'germany',
        'poznan': 'poland',
        'warszaw': 'poland',
        'gdynia': 'poland',
        'gdansk': 'poland',
        'sopot': 'poland',
        'krakow': 'poland',
        'wroclaw': 'poland',
        'malmo': 'sweden',
        'gothenburg': 'sweden',
        'vasteras': 'sweden',
        'stockholm': 'sweden',
        'copenhagen': 'denmark',
        'prague': 'czechia',
        'bergamo': 'italy',
        'milano': 'italy',
        }

country_to_currency = {
        'croatia': 'HRK',
        'poland': 'PLN',
        'italy': 'EUR',
        'germany': 'EUR',
        'sweden': 'SEK',
        'denmark': 'DKK',
        'czechia': 'CZK',
        }

rates = {
        ('PLN', 'HRK'): 1.73,
        ('EUR', 'HRK'): 7.43,
        ('CZK', 'HRK'): 0.29,
        ('HRK', 'EUR'): 0.13,
    }

def get_rate(fromc, toc, date):
    if fromc==toc:
        return 1
    return rates[fromc, toc]

def transform_row(r):
    if len(r.date) == 6:
        r.date += '2018.'
    d = r.date[:-1].split('.')
    r.date = date(*map(int, d[::-1]))
    r.country = city_to_country[r.city]
    r.currency = country_to_currency[r.country]
    if np.isnan(r.hrk):
        r.hrk = r.lcy * get_rate(r.currency, 'HRK', r.date)
    r.eur = r.hrk * get_rate('HRK', 'EUR', r.date)
    return r

df = pd.read_csv('./expenses.csv')
df = df.apply(transform_row, axis=1)

def percentageOfMoneyGraph(sentence_text):
    category_sum = []
    for category, rows in df.groupby(['category'])['eur']:
        category_sum.append((sum(rows.values), category))
    sums, labels = zip(*sorted(category_sum, reverse=True)[:11])
    explode = [0.1]*len(sums)

    fig1, ax1 = plt.subplots()
    ax1.pie(sums, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')
    plt.title('percentage of money spend on each category')
    plt.savefig('test332.png', bbox_inches='tight')
    return 'test332.jpeg'