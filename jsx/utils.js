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

function getID(x) {
  return document.getElementById(x);
}

function replaceEvent(target, type, current, old, capture = false) {
  target.removeEventListener(type, old, capture);
  target.addEventListener(type, current, capture);
}

export {getID, replaceEvent};