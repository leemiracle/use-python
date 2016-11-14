"""

火狐 Sqlite3 数据库
火狐存储这些数据库的默认目录为 C:\Documents and Settings\<USER>\Application Data\Mozilla\Firefox\Profiles\<profile folder>\,
"""

# downloads.sqlite
#   缺少密码或者是用户认证的电子邮件:进入 cookies,由于 HTTP 西意缺乏状态设计,网站利用 cookies 来维护状态。
#   火狐存储了这些 cookies 在 cookies. sqlite 数据库中。


def printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        c = conn.cursor()
        c.execute('SELECT host, name, value FROM moz_cookies')
        print('\n[*] -- Found Cookies --')
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            print('[+] Host: ' + host + ', Cookie: ' + name + ', Value: ' +
            value)
    except Exception as e:
        if 'encrypted' in str(e):
            print('\n[*] Error reading your cookies database.')
            print('[*] Upgrade your Python-Sqlite3 Library')


#   列举浏览历史,火狐存储这些数据在 places.sqlite 数据库中

def printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
        print('\n[*] -- Found History --')
        for row in c:
            url = str(row[0])
            date = str(row[1])
        print('[+] ' + date + ' - Visited: ' + url)
    except Exception as e:
        if 'encrypted' in str(e):
            print('\n[*] Error reading your places database.')
            print('[*] Upgrade your Python-Sqlite3 Library')
            exit(0)

# 打印 Google 搜索查询历史
import sqlite3, re


def printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, 'unixepoch')from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    print('\n[*] -- Found Google --')
    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&', url)
        if r:
            search = r[0].split('&')[0]
        search = search.replace('q=', '').replace('+', ' ')
        print('[+] ' + date + ' - Searched For: ' + search)

