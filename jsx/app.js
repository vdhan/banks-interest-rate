/*
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
*/

import React from 'react';
import ReactDOM from 'react-dom';
import Copy from './copy.js';
import {getID} from './utils.js';

class Init extends React.Component {
  componentDidMount() {
    this.makeRequest('vcb');
    this.makeRequest('bidv');
    this.makeRequest('ctg');
    this.makeRequest('abb');
    this.makePDFRequest('stb');
    this.makePDFRequest('acb');
    this.makePDFRequest('tcb');
    this.makePDFRequest('tpb');
  }

  makeRequest(param) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4) {
        var bank = getID(param);
        if (xhr.status == 200) {
          if (xhr.getResponseHeader('Content-Type') == 'application/json') {
            var data = JSON.parse(xhr.responseText);
            var keys = Object.keys(data);
            keys.forEach(function(key) {
              bank.querySelector(`[data-period=${key}]`).textContent = data[key];
            });
          }
        } else {
          bank.querySelector('[data-period="m1"]').textContent = 'Error!';
        }
      }
    };
    xhr.open('GET', `?t=${Math.random()}&bank=${param}`);
    xhr.send();
  }

  makePDFRequest(param) {
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4) {
        var bank = getID(param);
        if (xhr.status == 200) {
          if (xhr.getResponseHeader('Content-Type') == 'application/pdf') {
            var a = document.createElement('a');
            a.href = URL.createObjectURL(new Blob([xhr.response]));
            a.textContent = 'Download';
            a.download = `${param}.pdf`;
            a.classList.add('btn', 'btn-success', 'text-respond');
            bank.querySelector('[data-period="m1"]').appendChild(a);
          }
        } else {
          bank.querySelector('[data-period="m1"]').textContent = 'Error!';
        }
      }
    }
    xhr.open('GET', `?t=${Math.random()}&bank=${param}`);
    xhr.send();
  }

  render() {
    return (
      <div className="container">
        <h1 className="text-center">Lãi suất ngân hàng</h1>
        <div className="table-responsive">
          <table className="table table-bordered table-striped">
            <thead>
              <tr>
                <th>&nbsp;</th>
                <th>1 tháng</th>
                <th>3 tháng</th>
                <th>6 tháng</th>
                <th>9 tháng</th>
                <th>12 tháng</th>
              </tr>
            </thead>

            <tbody>
              <tr id="vcb">
                <td>
                  <img src="static/logo/vcb.png" alt="Vietcombank" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="bidv">
                <td>
                  <img src="static/logo/bid.png" alt="BIDV" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="ctg">
                <td>
                  <img src="static/logo/ctg.jpg" alt="Vietinbank" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="abb">
                <td>
                  <img src="static/logo/abb.jpg" alt="ABBank" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="stb">
                <td>
                  <img src="static/logo/stb.png" alt="Sacombank" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="acb">
                <td>
                  <img src="static/logo/acb.png" alt="ACB" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="tcb">
                <td>
                  <img src="static/logo/tcb.png" alt="Techcombank" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>

              <tr id="tpb">
                <td>
                  <img src="static/logo/tpb.png" alt="TBBank" className="img-thumbnail" />
                </td>
                <td data-period="m1"></td>
                <td data-period="m3"></td>
                <td data-period="m6"></td>
                <td data-period="m9"></td>
                <td data-period="m12"></td>
              </tr>
            </tbody>
          </table>
        </div>

        <Copy />
      </div>
    );
  }
}

ReactDOM.render(<Init />, getID('wrapper'));