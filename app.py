from flask import Flask, render_template, request, send_file
import pandas as pd
import json
import os

app = Flask(__name__)

def json_to_excel(json_file, excel_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    df.to_excel(excel_file, index=False)
    print(f"JSON data has been successfully converted to Excel format: {excel_file}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'json_file' not in request.files:
        return redirect(url_for('index'))

    json_file = request.files['json_file']
    if json_file.filename == '':
        return redirect(url_for('index'))

    if json_file:
        json_path = os.path.join('uploads', json_file.filename)
        json_file.save(json_path)

        excel_path = os.path.splitext(json_path)[0] + '.xlsx'
        json_to_excel(json_path, excel_path)

        return send_file(excel_path, as_attachment=True)

    return redirect(url_for('index'))

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True, port=8000)
