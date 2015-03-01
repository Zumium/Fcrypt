from Crypto.Cipher import AES,Blowfish
from Crypto import Random
from Crypto.Hash import SHA256

def gene_str(length) :
	str=''
	for x in range(0,length):
		str+='X'
	str_bytes=str.encode('UTF-16')
	return str_bytes[:length]

def gene_random_str(length) :
	return Random.new().read(length)

def gene_hash_random_str(passwd,length) :
	hasher=SHA256.new()
	hasher.update(passwd)
	hash_str=hasher.digest()
	if len(hash_str) >= length :
		return hash_str[:length]
	else :
		return None

def get_real_passwd(passwd) :
	passwd=passwd.encode('UTF-8')
	leng=len(passwd)
	if (leng%16!=0)+(leng%24!=0)+(leng%32!=0)==3 :
		if leng<16 :
			passwd+=gene_hash_random_str(passwd,16-leng)
			return passwd	
		elif leng>16 and leng<24 :
			passwd+=gene_hash_random_str(passwd,24-leng)
			return passwd
		elif leng>24 and leng<32 :
			passwd+=gene_hash_random_str(passwd,32-leng)
			return passwd
		else :
			passwd+=gene_hash_random_str(passwd,(leng//16+1)*16-leng)
			return passwd

def gene_cipher(passwd) :
	r_passwd=get_real_passwd(passwd)
	ci=AES.new(r_passwd,AES.MODE_ECB)
	return ci

def do_encrypt(cipher,data_raw):
	return cipher.encrypt(data_raw)

def do_decrypt(cipher,data_encrypted):
	return cipher.decrypt(data_encrypted)

def fill_data(raw_data):
	length_raw_data=len(raw_data)
	filled_data=raw_data
	if length_raw_data%16!=0 :
		filled_data+=gene_str((length_raw_data//16+1)*16-length_raw_data)
	return filled_data,length_raw_data
