first_dic = {'key1':'value1' , 'key2' :'value 2' , 'key3' : ['value3.1', 'value3.2'] , 'subdict' : {'subkey1':1 , 'subkey2' : 2}}

print(first_dic)

for i in first_dic:
    print(first_dic[i])
first_dic['new_element'] = 565
del first_dic['key1']
for i in first_dic:
    print(first_dic[i])
