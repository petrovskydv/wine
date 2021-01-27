import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_wine_file(file_path):
    excel_data_df = pandas.read_excel(file_path)
    pprint(excel_data_df)


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    age = datetime.datetime.now().year - 1921
    rendered_page = template.render(age=age)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    # main()
    read_wine_file('wine.xlsx')
