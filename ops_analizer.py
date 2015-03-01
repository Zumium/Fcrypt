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
	if '-h' in sys.argv:
		show_help()
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
	elif '-a' not in sys.argv:
		print('Must input the option:  encrypt or decrypt')
		exit()
##########################################################
##	Format:
##	input filename,operation,password,output filename
##########################################################

	op_details=[]
	for index in range(0,len(sys.argv)) :
		if sys.argv[index]=='-f' :
			op_details.insert(0,sys.argv[index+1])
		elif sys.argv[index]=='-a' :
			op_details.insert(1,sys.argv[index+1])
		elif sys.argv[index]=='-k' :
			op_details.insert(2,sys.argv[index+1])
		elif sys.argv[index]=='-o' :
			op_details.insert(3,sys.argv[index+1])
		elif sys.argv[index]=='-r' :
			op_details.insert(4,'True')
	if len(op_details)==4 :
		op_details.insert(4,'False')
	return op_details
 
def show_help():
	print("fcrypt----A Simple file encrypt/decrypt tool which is just for fun!\n\
options:\n\
-k\tpassword\n\
-f\tinput file name\n\
-o\toutput file name\n\
-a\toptions:encrypt or decrypt\n\
-r\tdelete the source file")
