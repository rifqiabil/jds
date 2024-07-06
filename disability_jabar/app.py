from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from models import db, Disability
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import dash
from dash import dcc, html

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Koneksi ke database dan mengambil data
DATABASE_URI = SQLALCHEMY_DATABASE_URI
engine = create_engine(DATABASE_URI)
query = 'SELECT * FROM disability_data'
df = pd.read_sql(query, engine)

# Membuat semua chart menggunakan Plotly
fig1 = px.bar(df, x='jenis_disabilitas', y='jumlah_disabilitas', title='Jumlah Disabilitas Berdasarkan Jenis')
fig2 = px.bar(df, x='bps_desa_kelurahan', y='jumlah_disabilitas', title='Jumlah Disabilitas Berdasarkan Kelurahan')
fig3 = px.line(df, x='tahun', y='jumlah_disabilitas', title='Tren Jumlah Disabilitas Berdasarkan Tahun')

# Inisialisasi aplikasi Dash
app_dash = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')
app_dash.layout = html.Div(children=[
    html.H1(children='Dashboard Disabilitas'),
    dcc.Graph(id='chart1', figure=fig1),
    dcc.Graph(id='chart2', figure=fig2),
    dcc.Graph(id='chart3', figure=fig3)
])

# Endpoint untuk menampilkan chart 1: Jumlah Disabilitas Berdasarkan Jenis
@app.route('/api/disability/chart1', methods=['GET'])
def get_chart1():
    return jsonify(fig1.to_dict())

# Endpoint untuk menampilkan chart 2: Jumlah Disabilitas Berdasarkan Kelurahan
@app.route('/api/disability/chart2', methods=['GET'])
def get_chart2():
    return jsonify(fig2.to_dict())

# Endpoint untuk menampilkan chart 3: Tren Jumlah Disabilitas Berdasarkan Tahun
@app.route('/api/disability/chart3', methods=['GET'])
def get_chart3():
    return jsonify(fig3.to_dict())

# Endpoint untuk menampilkan chart tertentu, misalnya chart 3
@app.route('/api/disability/chart/<chart_id>', methods=['GET'])
def get_specific_chart(chart_id):
    if chart_id == 'chart1':
        return jsonify(fig1.to_dict())
    elif chart_id == 'chart2':
        return jsonify(fig2.to_dict())
    elif chart_id == 'chart3':
        return jsonify(fig3.to_dict())
    else:
        return jsonify({'message': 'Chart not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ini akan membuat tabel jika belum ada
    app.run(debug=True)
