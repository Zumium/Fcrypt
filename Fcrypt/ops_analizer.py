##
#    ops_analizer.py - change the command line options into a data struct which program can easily use
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

import sys

def anal_options():
	if len(sys.argv)==1:
		show_help()
		exit()
	elif '-h' in sys.argv:
		show_help()
		exit()
	elif '-v' in sys.argv:
		show_version_info()
		exit()
	elif '-o' not in sys.argv:
		print('Must input the output file name')
		exit()
	elif '-k' not in sys.argv:
		print('Must input the password')
		exit()
	elif '-f' not in sys.argv:
		print('Must input the input file name')
		exit()
	elif '-d' not in sys.argv and '-e' not in sys.argv:
		print('Must input the option:  -e for encrypt or -d for decrypt')
		exit()
	elif '-m' not in sys.argv:
		print('Must choose encryption mode. aes-ecb or aes-cbc')
		exit()
##########################################################
##	Format:
##	input filename,operation,mode,password,output filename,is remove src
##########################################################

	input_file=''
	operation=''
	mode=''
	passwd=''
	output_file=''
	is_rm_src='False'

	for index in range(0,len(sys.argv)) :
		if sys.argv[index]=='-f' :
			input_file=sys.argv[index+1]
		elif sys.argv[index]=='-e' :
			operation='encrypt'
		elif sys.argv[index]=='-d' :
			operation='decrypt'
		elif sys.argv[index]=='-m' :
			mode=sys.argv[index+1]
		elif sys.argv[index]=='-k' :
			passwd=sys.argv[index+1]
		elif sys.argv[index]=='-o' :
			output_file=sys.argv[index+1]
		elif sys.argv[index]=='-r' :
			is_rm_src='True'
	op_details=[input_file,operation,mode,passwd,output_file,is_rm_src]
	if '' in op_details :
		print('Bad options.Please check again.')
		exit()
	return op_details
 
def show_help():
	print("fcrypt----A Simple file encrypt/decrypt tool.\n\
options:\n\
-k password\tpassword\n\
-f input_filename\tinput file name\n\
-o output_filename\toutput file name\n\
-e\tencrypt\n\
-d\tdecrypt\n\
-r\tdelete the source file\n\
-v\tshow version info")

def show_version_info():
	print("Version:1.3\n\n\
Copyright (C) 2015 Zumium\n\n\
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\n\
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\n\
You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.")
