import requests
from models import db, Disability
from app import app

def load_data():
    response = requests.get('https://opendata.bandung.go.id/api/bigdata/kecamatan_antapani/jmlh_pnyndng_dsblts_brdsrkn_klrhn_d_kcmtn_ntpn_kt_bndng')
    data = response.json()['data']

    with app.app_context():
        for item in data:
            disability = Disability(
                kode_provinsi=item['kode_provinsi'],
                nama_provinsi=item['nama_provinsi'],
                bps_kode_kabupaten_kota=item['bps_kode_kabupaten_kota'],
                bps_nama_kabupaten_kota=item['bps_nama_kabupaten_kota'],
                bps_kode_kecamatan=item['bps_kode_kecamatan'],
                bps_nama_kecamatan=item['bps_nama_kecamatan'],
                bps_kode_desa_kelurahan=item['bps_kode_desa_kelurahan'],
                bps_desa_kelurahan=item['bps_desa_kelurahan'],
                kemendagri_kode_kecamatan=item['kemendagri_kode_kecamatan'],
                kemendagri_nama_kecamatan=item['kemendagri_nama_kecamatan'],
                kemendagri_kode_desa_kelurahan=item['kemendagri_kode_desa_kelurahan'],
                kemendagri_nama_desa_kelurahan=item['kemendagri_nama_desa_kelurahan'],
                jenis_disabilitas=item['jenis_disabilitas'],
                jumlah_disabilitas=item['jumlah_disabilitas'],
                satuan=item['satuan'],
                tahun=item['tahun']
            )
            db.session.add(disability)
        db.session.commit()

if __name__ == '__main__':
    load_data()

# from app import app, db
# from models import Disability

# data = [
#     {
#         "id": 1,
#         "kode_provinsi": 32,
#         "nama_provinsi": "JAWA BARAT",
#         "bps_kode_kabupaten_kota": 3273,
#         "bps_nama_kabupaten_kota": "KOTA BANDUNG",
#         "bps_kode_kecamatan": 3273141,
#         "bps_nama_kecamatan": "ANTAPANI",
#         "bps_kode_desa_kelurahan": 3273141001,
#         "bps_desa_kelurahan": "ANTAPANI KIDUL",
#         "kemendagri_kode_kecamatan": "32.73.20",
#         "kemendagri_nama_kecamatan": "ANTAPANI",
#         "kemendagri_kode_desa_kelurahan": "32.73.20.1005",
#         "kemendagri_nama_desa_kelurahan": "ANTAPANI KIDUL",
#         "jenis_disabilitas": "AUTIS",
#         "jumlah_disabilitas": 3,
#         "satuan": "ORANG",
#         "tahun": 2018
#     }
# ]

# with app.app_context():
#     db.create_all()
#     for record in data:
#         new_entry = Disability(**record)
#         db.session.add(new_entry)
#     db.session.commit()
