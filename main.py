import collections
import datetime
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_file(file_path):
    excel_data_df = pandas.read_excel(file_path, keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records')
    wines_categories = collections.defaultdict(list)
    for wine in wines:
        wines_categories[wine['Категория']].append(wine)
    return wines_categories


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    load_dotenv()
    file_path = os.environ['FILE_PATH']

    commencement_year = 1921
    work_years_number = datetime.datetime.now().year - commencement_year
    wines_categories = read_file(file_path)

    rendered_page = template.render(age=work_years_number, wines_categories=wines_categories)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
