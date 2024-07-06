from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disability(db.Model):
    __tablename__ = 'disability_data'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kode_provinsi = db.Column(db.Integer)
    nama_provinsi = db.Column(db.String(255))
    bps_kode_kabupaten_kota = db.Column(db.Integer)
    bps_nama_kabupaten_kota = db.Column(db.String(255))
    bps_kode_kecamatan = db.Column(db.Integer)
    bps_nama_kecamatan = db.Column(db.String(255))
    bps_kode_desa_kelurahan = db.Column(db.Integer)
    bps_desa_kelurahan = db.Column(db.String(255))
    kemendagri_kode_kecamatan = db.Column(db.String(50))
    kemendagri_nama_kecamatan = db.Column(db.String(255))
    kemendagri_kode_desa_kelurahan = db.Column(db.String(50))
    kemendagri_nama_desa_kelurahan = db.Column(db.String(255))
    jenis_disabilitas = db.Column(db.String(255))
    jumlah_disabilitas = db.Column(db.Integer)
    satuan = db.Column(db.String(50))
    tahun = db.Column(db.Integer)
