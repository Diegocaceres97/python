import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    # Guarda el hash del bloque previo haciendolo inmutable
    # timestamp lo utilizamos para sincronizar toda la blockchain
    timestamp = datetime.datetime.now()

# Creamos un bloque y guardamos los datos
    def __init__(self, data):
        self.data = data


# calculamos el hash del bloque
            # para calcular el hash actual debemos incluir el hash del previo bloque
    def hash(self):
        h = hashlib.sha256()
        h.update(
            # formato de codificación de caracteres Unicode e ISO 10646
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        # obtenemos el hash
        return h.hexdigest()

# Imprimimos el bloque en pantalla
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

# Generamos 10 bloques random's en un loop que estara continuamente minando
class Blockchain:
# dificultad
    diff = 20
    # bits maximo que recibira los bloques
    maxNonce = 2**32
    # rango aceptable de minado y de bloque
    target = 2 ** (256-diff)

    block = Block("Genesis")
    # referencia primera del bloque genesis (creador)
    dummy = head = block

    def add(self, block):
# con esto referimos al bloque previo
# con esta linea agregamos los bloques al final de la lista
# entonces al bloque actual le añadiremos 1 al ser el actual
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                # seguimiento de minado
                block.nonce += 1

blockchain = Blockchain()

for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next