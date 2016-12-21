"""
Banks interest rate
Copyright (C) 2016 Hoàng Ân

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import requests
from bs4 import BeautifulSoup
from flask import render_template, request, jsonify, Response
from htmlmin.minify import html_minify

from wsgi import app


@app.route('/')
def index():
    bank = request.args.get('bank')
    if bank == 'vcb':
        r = requests.get('https://www.vietcombank.com.vn/InterestRates/default.aspx')
        soup = BeautifulSoup(r.text, 'html.parser')
        tbody = soup.tbody

        m1 = tbody.select_one('tr:nth-of-type(6) td:nth-of-type(2)')
        data = {'m1': m1.string}

        m3 = tbody.select_one('tr:nth-of-type(8) td:nth-of-type(2)')
        data['m3'] = m3.string

        m6 = tbody.select_one('tr:nth-of-type(9) td:nth-of-type(2)')
        data['m6'] = m6.string

        m9 = tbody.select_one('tr:nth-of-type(10) td:nth-of-type(2)')
        data['m9'] = m9.string

        m12 = tbody.select_one('tr:nth-of-type(11) td:nth-of-type(2)')
        data['m12'] = m12.string

        return jsonify(data)
    elif bank == 'bidv':
        r = requests.get('http://bidv.com.vn/Tra-cuu-lai-suat.aspx')
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.select_one(
            '#plcRoot_Layout_zoneMenu_PagePlaceholder_PagePlaceholder_Layout_zoneContent_LSTGMore_dgLSTG')

        m1 = table.select_one('tr:nth-of-type(3) td:nth-of-type(4)')
        data = {'m1': m1.string}

        m3 = table.select_one('tr:nth-of-type(3) td:nth-of-type(6)')
        data['m3'] = m3.string

        m6 = table.select_one('tr:nth-of-type(3) td:nth-of-type(7)')
        data['m6'] = m6.string

        m9 = table.select_one('tr:nth-of-type(3) td:nth-of-type(8)')
        data['m9'] = m9.string

        m12 = table.select_one('tr:nth-of-type(3) td:nth-of-type(10)')
        data['m12'] = m12.string

        return jsonify(data)
    elif bank == 'ctg':
        r = requests.get('https://www.vietinbank.vn/web/home/vn/lai-suat/')
        soup = BeautifulSoup(r.text, 'html.parser')
        tbody = soup.tbody

        m1 = tbody.select_one('tr:nth-of-type(6) td:nth-of-type(2)')
        data = {'m1': m1.string}

        m3 = tbody.select_one('tr:nth-of-type(8) td:nth-of-type(2)')
        data['m3'] = m3.string

        m6 = tbody.select_one('tr:nth-of-type(11) td:nth-of-type(2)')
        data['m6'] = m6.string

        m9 = tbody.select_one('tr:nth-of-type(14) td:nth-of-type(2)')
        data['m9'] = m9.string

        m12 = tbody.select_one('tr:nth-of-type(17) td:nth-of-type(2)')
        data['m12'] = m12.string

        return jsonify(data)
    elif bank == 'abb':
        r = requests.get('https://www.abbank.vn/lai-suat-tiet-kiem-vnd-p3132r9.html')
        soup = BeautifulSoup(r.text, 'html.parser')
        tbody = soup.tbody

        m1 = tbody.select_one('tr:nth-of-type(6) td:nth-of-type(2)')
        data = {'m1': m1.string}

        m3 = tbody.select_one('tr:nth-of-type(8) td:nth-of-type(2)')
        data['m3'] = m3.string

        m6 = tbody.select_one('tr:nth-of-type(11) td:nth-of-type(2)')
        data['m6'] = m6.string

        m9 = tbody.select_one('tr:nth-of-type(14) td:nth-of-type(2)')
        data['m9'] = m9.string

        m12 = tbody.select_one('tr:nth-of-type(17) td:nth-of-type(2)')
        data['m12'] = m12.string

        return jsonify(data)
    elif bank == 'stb':
        r = requests.get('https://www.sacombank.com.vn/canhan/Documents/LaiSuat/Niem%20yet%20tai%20quay_HCMVAHN.pdf')
        return Response(r.content, mimetype='application/pdf')
    elif bank == 'acb':
        r = requests.get('http://www.acb.com.vn/vn/interest/personal/tai-khoan-tien-gui/khac/lai-suat')
        soup = BeautifulSoup(r.text, 'html.parser')
        main = soup.select_one('div#main')

        a = main.select_one('a.breadcrumb')
        r = requests.get('http://www.acb.com.vn' + a['href'])
        return Response(r.content, mimetype='application/pdf')
    elif bank == 'tcb':
        r = requests.get('https://www.techcombank.com.vn/cong-cu-tien-ich/lai-suat')
        soup = BeautifulSoup(r.text, 'html.parser')
        rates = soup.select_one('ul.interest-rates')
        li = rates.ul.select_one('li:nth-of-type(5)')

        a = li.a
        r = requests.get('https://www.techcombank.com.vn' + a['href'])
        return Response(r.content, mimetype='application/pdf')
    elif bank == 'tpb':
        r = requests.get('https://tpb.vn/financial-toolkit/lai-suat')
        soup = BeautifulSoup(r.text, 'html.parser')
        parent = soup.select_one('div#block-views-deposit-interest-list-block-1')
        div = parent.select_one('div.deposit-interest-link')

        a = div.a
        r = requests.get(a['href'])
        return Response(r.content, mimetype='application/pdf')
    else:
        render = render_template('index.html')
        return html_minify(render)
