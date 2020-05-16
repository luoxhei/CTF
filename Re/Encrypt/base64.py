# coding:utf8
import string
import base64


#table = list(string.letters) + list(string.digits) + ['+', '/']
table = list('ZXYABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/')

def my_base64_encodestring(input_str):
    # 对每一个字节取ascii数值或unicode数值，然后转换为2进制
    str_ascii_list = ['{:0>8}'.format(str(bin(ord(i))).replace('0b', '')) for i in input_str]
    output_str = ''
    # 不够3的整数倍 补齐所需要的次数
    equal_num = 0
    while str_ascii_list:
        temp_list = str_ascii_list[:3]
        if len(temp_list) != 3:
            while len(temp_list) < 3:
                equal_num += 1
                temp_list += ['0'*8]
        temp_str = ''.join(temp_list)
        # 三个8字节的二进制 转换为4个6字节的二进制
        temp_str_list = [temp_str[x:x+6] for x in [0, 6, 12, 18]]
        # 二进制转为10进制
        temp_str_list = [int(x, 2) for x in temp_str_list]
        # 判断是否为补齐的字符 做相应的处理
        if equal_num:
            temp_str_list = temp_str_list[0:4-equal_num]
        output_str += ''.join([table[x] for x in temp_str_list])
        str_ascii_list = str_ascii_list[3:]
    output_str = output_str + '=' * equal_num
    #print(output_str)
    return output_str

def my_base64_decodestring(input_str):
    # 对每一个字节取索引，然后转换为2进制
    str_ascii_list = ['{:0>6}'.format(str(bin(table.index(i))).replace('0b', ''))
                      for i in input_str if i != '=']
    output_str = ''
    equal_num = input_str.count('=')
    while str_ascii_list:
        temp_list = str_ascii_list[:4]
        temp_str = ''.join(temp_list)
        # 补够8位
        if len(temp_str) % 8 != 0:
            temp_str = temp_str[0:-1*equal_num*2]
        # 4个6字节的二进制  转换  为三个8字节的二进制 
        temp_str_list = [temp_str[x:x+8] for x in [0, 8, 16]]
        # 二进制转为10进制
        temp_str_list = [int(x, 2) for x in temp_str_list if x]
        output_str += ''.join([chr(x) for x in temp_str_list])
        str_a scii_list = str_ascii_list[4:]
    #print(output_str)
    return output_str

if __name__ == "__main__":
    input_str = ''
    print(my_base64_decodestring(input_str))