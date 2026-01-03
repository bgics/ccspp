from secrets import token_bytes


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb)


def encrypt(original: str) -> tuple[int, int]:
    dummy: int = random_key(len(original))
    encrypted: int = int.from_bytes(original.encode()) ^ dummy

    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8)
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One time pad!")
    result: str = decrypt(key1, key2)
    print(result)
