import csv
import json
import requests

# Zadaci radjeni u obliku simulacije, za stvarni prikaz bi samo ovo otvorili iz fajla i onda upisali u fajl


def function_loop():
    while True:
        key = input("Input 'y' to continue and 'n' to exit the program: ")
        if key == 'y' or key == 'n':
            return key
        else:
            continue


def search_by_title(file, name):
    for article in file['data']['articles']:
        if name == article['title']:
            print('\n''--------------------------------------------------------------------------------------------------------> Result''\n')
            print(article)
            print('\n''--------------------------------------------------------------------------------------------------------> End of the output!''\n')
            return article
    print("error 404 article not found")
    return 404


def add_comment(file, name, comment_name, description, author):
    for article in file['data']['articles']:
        if name == article['title']:
            if author == '':
                author = 'anonim'
            article['comments'].append(
                {"title": comment_name, "author": author, "description": description})
            print('\n''--------------------------------------------------------------------------------------------------------> Comment added''\n')
            print(article)
            print('\n''--------------------------------------------------------------------------------------------------------> End of the output!''\n')


def delete_article(file, comment_name):
    for ind, article in enumerate(file['data']['articles']):
        for comment in article['comments']:
            if comment_name == comment['title']:
                print('\n''--------------------------------------------------------------------------------------------------------> Article deleted successfully''\n')
                print(file['data']['articles'].pop(ind))
                print('\n''--------------------------------------------------------------------------------------------------------> Data looks like this now''\n')
                print(file['data']['articles'])
                print('\n''--------------------------------------------------------------------------------------------------------> End of the output!''\n')
                return file
    print("error 404 article not found")
    return


def find_comment_by_title(file, article, title):
    for article in file['data']['articles']:
        for comment in article['comments']:
            if title == comment['title']:
                print('\n''--------------------------------------------------------------------------------------------------------> Result''\n')
                print(comment)
                print('\n''--------------------------------------------------------------------------------------------------------> End of the output!''\n')
                return comment
    print("error 404 comment not found")
    return 404


def find_comment_by_author_name(file, author):
    comments = []
    for article in file['data']['articles']:
        for comment in article['comments']:
            if author == comment['author']:
                comments.append(comment)
                print('\n''--------------------------------------------------------------------------------------------------------> Result''\n')
                print(comment)
                print('\n''--------------------------------------------------------------------------------------------------------> End of the output!''\n')

    return comments if comments else print("error 404 no comments found")


def find_all_articles_by_author_name(file, author):
    articles = []
    for article in file['data']['articles']:
        if author == article['author']:
            articles.append(article)
    print('\n''--------------------------------------------------------------------------------------------------------> Result''\n')
    for article in articles:
        print(article, "\n")
    print('\n''--------------------------------------------------------------------------------------------------------> End of the output!''\n')

    return articles if articles else print("error 404 articles not found")


data = requests.get('https://jsonblob.com/api/1226162686332362752').json()


while (True):
    try:
        program = input(
            """Choose an option:
    1. Search articles by name
    2. Add comment to an article
    3. Delete an article
    4. Search for comments by comment title
    5. Search for comments by author's name
    6. Search articles by author's name
    7. Write articles to csv (searched by author's name and sorted by number of comments)
    8. Write articles to JSON file (searched by author's name and sorted by number of views)
    9. Exit \n""")
        if int(program) == 1:
            title = input("Input the title of the article: ")
            search_by_title(data, title)
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 2:
            title = input("Input the title of the article: ")
            if search_by_title(data, title) != 404:
                add_comment(data, title, input("Input title of the comment: "), input(
                    "Input comment description: "), input('Input author name (optional, press enter to leave it blank): '))
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 3:
            title = input("Input the title of the comment: ")
            delete_article(data, title)
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 4:
            article = input("Input the title of the article: ")
            comment = input("Input the title of the comment: ")
            find_comment_by_title(data, article, comment)
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 5:
            author = input("Input author's name: ")
            find_comment_by_author_name(data, author)
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 6:
            find_all_articles_by_author_name(
                data, input('Input author\'s name: '))
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 7:
            to_csv = sorted(find_all_articles_by_author_name(
                data, input('Input author\'s name: ')), key=lambda a: len(a['comments']))

            keys = to_csv[0].keys()

            with open(r'DomaciZadaci\peti_domaci\zad3\articles.csv', 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(to_csv)
                print("Articles writen to csv file")

            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 8:
            to_json = sorted(find_all_articles_by_author_name(
                data, input('Input author\'s name: ')), key=lambda a: a['views'], reverse=True)
            out_file = open(
                r'DomaciZadaci\peti_domaci\zad3\articles.json', 'w')
            json.dump(to_json, out_file, indent=True)
            out_file.close()
            print("Articles writen to json file")
            key = function_loop()
            if key == 'y':
                continue
            else:
                break
        elif int(program) == 9:
            break
        else:
            print("You must choose one of the listed options!")
    except Exception:
        print("You must choose one of the listed options!")
