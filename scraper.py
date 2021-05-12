import requests
import lxml.html as html


HOME_URL = 'https://www.larepublica.co/'


XPATH_LINK_TO_ARTICLE = '//text-fill/a[contains(@class,"Sect")]/@href'
XPATH_TITLE = '//h2[@data-h]/span/text()'
XPATH_SUMMARY = ' //div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p//text()'


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            #print(home)
            parsed = html.fromstring(home)
            link_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(link_to_notices,len(link_to_notices))
        else:
            raise ValueError(f'Error : {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__=='__main__':
    run()



