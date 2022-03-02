import hashlib

hash_object = hashlib.md5()  # 新建一个空的md5对象
hash_object.update("武沛齐".encode('utf-8'))  # 输入值，需要先编码为字节
result = hash_object.hexdigest()  # 加密
print(result)  # 17351012472429d52d0c0d23d468173d
