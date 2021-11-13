# SHA256("CPEN 442 Coin" + "2021" + hash_of_preceding_coin + coin_blob + id_of_miner)

import hashlib
import requests
import base64

NONCE_LIMIT = 1000000000000

def SHA256(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def mine(id_of_miner, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for coin_blob in range(0, NONCE_LIMIT):
        text = "CPEN 442 Coin" + "2021" + previous_hash + str(coin_blob) + id_of_miner
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            return new_hash, str(coin_blob)
    return new_hash, str(coin_blob)

if __name__ == "__main__":
    id_of_miner = "91616862"
    previous_hash = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
    prefix_zeros = 8
    new_hash, coin_blob = mine(id_of_miner, previous_hash, prefix_zeros)
    coin_blob = base64.b64encode(coin_blob.encode()).decode()
    print("Coin Blob: " + coin_blob)
    print("Hash: " + new_hash)
    r = requests.post("http://cpen442coin.ece.ubc.ca/verify_example_coin", 
                      json={"coin_blob": coin_blob, "id_of_miner": id_of_miner})
    if(r.status_code == 200):
        print("Success!")
    else:
        print(r.status_code)
        print("Failure!")

        




