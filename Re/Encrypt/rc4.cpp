#include<cstdio>
#include<cstring>

class rc4{
	public:
		rc4();
		void init(unsigned char *key, unsigned long len);
		void crypt(unsigned char *Data, unsigned long len);
	private:
		int box[256] = {}; // �ԳƼ����е��û��� S��
    	int s_i, s_j;
};

rc4::rc4(){
	s_i = 0;
	s_j = 0;
}

void rc4::init(unsigned char *key, unsigned long len){
	int i, j = 0;
	unsigned char temp;
	for(i = 0;i < 256;i++)
		box[i] = i;
	for(i = 0;i < 256;i++){
		j = (j + box[i] + key[i % len]) % 256;
		temp = box[i];
		box[i] = box[j];
		box[j] = temp;
	}
}

void rc4::crypt(unsigned char *Data, unsigned long len){
	unsigned char temp;
	for(unsigned long k = 0;k < len;k++){
		s_i = (s_i + 1) % 256;
		s_j = (s_j + box[s_i]) % 256;
		temp = box[s_i];
		box[s_i] = box[s_j];
		box[s_j] = temp;
		int r = (box[s_i] + box[s_j]) % 256;
		Data[k] ^= box[r];
	}
}

int main(){
	unsigned char c[12] = {};
	unsigned char key[] = "";
	unsigned int kleng = strlen((char*)key);
	rc4 R;
	R.init(key,kleng);
	R.crypt(c,12);
	printf("%s",c);
}
