import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint
import collections

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_wine_file_to_dict(file_path):
    excel_data_df = pandas.read_excel(file_path, keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records')
    return wines


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    age = datetime.datetime.now().year - 1921
    wines = read_wine_file_to_dict('wine2.xlsx')
    wines_categories = collections.defaultdict(list)
    for wine in wines:
        wines_categories[wine['Категория']].append(wine)

    pprint(wines_categories)

    rendered_page = template.render(age=age, wines=wines)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
