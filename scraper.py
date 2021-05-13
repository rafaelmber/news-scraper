import requests
import lxml.html as html
import os
import datetime


HOME_URL = 'https://www.larepublica.co/'


XPATH_LINK_TO_ARTICLE = '//text-fill/a[contains(@class,"Sect")]/@href'
XPATH_TITLE = '//text-fill/span/text()'
XPATH_SUMMARY = ' //div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p//text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed_notice = html.fromstring(notice)
            try:
                title = parsed_notice.xpath(XPATH_TITLE)[0]
                title = title.replace('\"','')
                summary = parsed_notice.xpath(XPATH_SUMMARY)[0]
                body = parsed_notice.xpath(XPATH_BODY)
            except IndexError:
                return
            file_name = title.replace('?','')
            with open(f'news/{today}/{file_name}.txt','w',encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            link_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(link_to_notices,len(link_to_notices))

            today = datetime.date.today().strftime('%Y-%m-%d')
            if not os.path.isdir(f'news/{today}'):
                os.mkdir(f'news/{today}')
            for link in link_to_notices:
                parse_notice(link,today)
        else:
            raise ValueError(f'Error : {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__=='__main__':
    run()



