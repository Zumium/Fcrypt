##
#    fcrypt.py - the main file of this program
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

#! /usr/bin/env python3

import ops_analizer
import ciphers
import file_io
import os

def main() :
	options=ops_analizer.anal_options()
	if options[1]=='encrypt' :
		ci=ciphers.gene_cipher(options[2])
		ne_data=file_io.read_co_file(options[0])
		ne_data_filled,real_length=ciphers.fill_data(ne_data)
		en_data=ciphers.do_encrypt(ci,ne_data_filled)
		file_io.write_en_file(options[3],real_length,en_data)
		print('Encryption Completed')
	elif options[1]=='decrypt' :
		ci=ciphers.gene_cipher(options[2])
		real_length,en_data=file_io.read_en_file(options[0])
		ne_data=ciphers.do_decrypt(ci,en_data)
		ne_data=ne_data[:real_length]
		file_io.write_co_file(options[3],ne_data)
		print('Decrypt Completed')
	if options[4]=='True' :
		os.remove(options[0])

if __name__=='__main__' :
	main()
