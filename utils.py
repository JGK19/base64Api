import base64

def binary_to_base64(binary_string):
    binary_bytes = binary_string.encode('utf-8')
    base64_bytes = base64.b64encode(int(binary_bytes, 2).to_bytes((len(binary_bytes) + 7) // 8, byteorder='big'))
    return base64_bytes.decode('utf-8')

def base64_to_binary(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    binary_bytes = bin(int.from_bytes(base64.b64decode(base64_bytes), byteorder='big'))[2:]
    binary_string = binary_bytes.zfill(8 * ((len(binary_bytes) + 7) // 8))
    return binary_string

def base16_to_base2(base16):
  output = int(base16, 16)
  output = bin(output)
  return str(output)

def base2_to_base16(base2):
  output = int(base2, 2)
  output = hex(output)
  return str(output)
