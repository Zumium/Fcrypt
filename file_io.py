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
