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
