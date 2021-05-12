import requests
import lxml.html as html


XPATH_LINK_TO_ARTICLE = '//h2/a/@href'
XPATH_TITLE = '//h2[@data-h]/span/text()'
XPATH_SUMMARY = ' //div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p//text()'


def run():


if __name__=='__main__':
    run()