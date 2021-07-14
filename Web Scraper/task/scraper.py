import requests
import os
from string import punctuation

from bs4 import BeautifulSoup

if __name__ == '__main__':

    number_of_pages = int(input())
    type_of_articles = input()

    for i in range(number_of_pages):
        url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i + 1}"

        try:
            r = requests.get(url)

            if r.status_code != 200:
                print(f"The URL returned {r.status_code}!")
            else:
                os.chdir("/Users/florencethirioncaclin/PycharmProjects/Web Scraper/Web Scraper/task")
                os.mkdir(f"Page_{i + 1}")
                os.chdir(f"Page_{i + 1}")
                soup = BeautifulSoup(r.content, 'html.parser')

                articles = soup.find_all('article')

                for article in articles:
                    article_type = article.find_all('span', {'class': 'c-meta__type'})

                    if article_type[0].text == type_of_articles:
                        article_content = article.find_all('a', {'data-track-action': 'view article'})

                        title = article_content[0].text

                        processed_title = ""
                        for char in title:
                            if char == " ":
                                processed_title += "_"
                            elif char in punctuation:
                                continue
                            else:
                                processed_title += char

                        body = article.find('div', {'class': 'body'})

                        link = "https://www.nature.com" + article_content[0].get('href')
                        r_text = requests.get(link)

                        article_soup = BeautifulSoup(r_text.content, 'html.parser')
                        article_body = article_soup.find_all('div', {'class': 'c-article-body u-clearfix'})
                        if not article_body:
                            article_body = article_soup.find_all('div', {'class': 'article-item__body'})

                        my_file = open(f"{processed_title}.txt", "wb")
                        my_file.write((article_body[0].text.strip()).encode())
                        my_file.close()

        except ConnectionError:
            print("Invalid page!")

    print("Saved all articles")
