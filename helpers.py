import datetime

FNV_PRIME=16777619
FNV_OFFSET_BASIS=2166136261

def fnv1a(bytes_to_hash):
    hashed=FNV_OFFSET_BASIS
    for byte in bytes_to_hash:
        hashed^=byte
        hashed*=FNV_PRIME
        hashed&=0xffffffff
    return hashed.to_bytes(4, "big")

def sec_to_MS(secs):
    return datetime.datetime.fromtimestamp(secs).strftime('%M:%S')

def sec_to_HMS(secs):
    if secs>=3600:
        return datetime.datetime.fromtimestamp(secs).strftime('%H:%M:%S')
    else: return datetime.datetime.fromtimestamp(secs).strftime('%M:%S') 

HASH_NAME=fnv1a(b"pymodoro")

TEXT_CMD=["status", "next_phase", "stop", "add_time"]

MIN_UP="~/git/Pymodoro/pymodoro-cli -mu"
MIN_DOWN="~/git/Pymodoro/pymodoro-cli -md"
SEC_UP="~/git/Pymodoro/pymodoro-cli -su"
SEC_DOWN="~/git/Pymodoro/pymodoro-cli -sd"
NEXT_PHASE="~/git/Pymodoro/pymodoro-cli -n"
E_CM="%{A}"

BYTE_CMD={}
for key in TEXT_CMD:
    BYTE_CMD[key]=fnv1a(key.encode())
