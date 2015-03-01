##
#    file_io.py - offer the functions of io operation designed for this program
#
#    Copyright (C) 2015, Zumium <martin007323@gmail.com>
#
#This file is part of Fcrypt.
#
#    Fcrypt is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Fcrypt is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Fcrypt.  If not, see <http://www.gnu.org/licenses/>.
##

import struct

def read_en_file(fname):
	f=open(fname,'rb')
	length_bytes=f.read(8)
	length=struct.unpack('l',length_bytes)
	length=length[0]
	data=f.read()
	f.close()
	return length,data

def write_en_file(fname,raw_length,data_encrypted):
	f=open(fname,'wb')
	f.write(struct.pack('l',raw_length))
	f.write(data_encrypted)
	f.close()

def read_co_file(fname) :
	f=open(fname,'rb')
	data=f.read()
	f.close()
	return data

def write_co_file(fname,data) :
	f=open(fname,'wb')
	f.write(data)
	f.close()
