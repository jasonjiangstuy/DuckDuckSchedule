my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
print(type(my_str_as_bytes)) # ensure it is byte representation
my_decoded_str = my_str_as_bytes.decode()
print(type(my_decoded_str) )# ensure it is string representation