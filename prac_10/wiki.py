"""CP1404/CP5632 Practical"""
import wikipedia


def main():
    page_title = input("Enter page title: ")
    while page_title != '':
        try:
            page = wikipedia.page(page_title)
            print(page.title)
            print(page.summary)
            print(page.url)
            page_title = input("Enter page title: ")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            page_title = input("Enter page title: ")


main()
