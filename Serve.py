from flask import Flask, render_template, request
import csv, os


app = Flask(__name__)


@app.route('/')
def index():
    with open('./crop/CSVfile/TSs.csv', 'r', encoding='utf-8-sig') as CSVfile:
        reader = csv.reader(CSVfile)
        rows = [rows for rows in reader]

    return render_template('index.html', rows=rows[0:100][0:100])

    with open('./static/WordCloud/wordclud.png') as img:
        return render_template('index.html', img)

# serve
if __name__ == '__main__':
    app.run(
        debug="True"
    )
