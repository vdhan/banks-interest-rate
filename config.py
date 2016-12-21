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

import os


class Base(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    HOST = '0.0.0.0'


class Dev(Base):
    SECRET_KEY = 't\x9c\x93\x82\xdd6#\xd6\x0fk\x1c\xe6\x9d(&\xb9V\\[h\x01\xc3:`'
    PORT = 10004
    DEBUG = True
