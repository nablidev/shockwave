from hashlib import sha256


def update_hash(*args):
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return update_hash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return f"Block#: {self.number}\n" \
               f"Hash: {self.hash()}\n" \
               f"Previous: {self.previous_hash}\n" \
               f"Data: {self.data}\n" \
               f"Nonce: {self.nonce}\n"


class Blockchain():
    difficulty = 4

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append({
            'hash': block.hash(),
            'previous': block.previous_hash,
            'number': block.number,
            'data': block.data,
            'nonce': block.nonce
        })


def main():
    block = Block("hello world", 1)
    #print(f"{update_hash('helloworld', 'hello')}")
    print(block)

if __name__ == '__main__':
    main()
