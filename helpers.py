FNV_PRIME=16777619
FNV_OFFSET_BASIS=2166136261

def fnv1a(bytes_to_hash):
    hashed=FNV_OFFSET_BASIS
    for byte in bytes_to_hash:
        hashed^=byte
        hashed*=FNV_PRIME
        hashed&=0xffffffff
    return hashed.to_bytes(4, "big")

HASH_NAME=fnv1a(b"pymodoro")

TEXT_CMD=["status", "next_phase"]

BYTE_CMD={}
for key in TEXT_CMD:
    BYTE_CMD[key]=fnv1a(key.encode())
