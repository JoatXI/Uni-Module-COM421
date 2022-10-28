class HashTable:
    def __init__(self, nbuckets):
        self.nbuckets = nbuckets

        self.bucket_list = [[] for i in range(self.nbuckets)]

    def __str__(self):
        return self.bucket_list.__str__()

    def get(self, key):
        hash_code = self.calc_hash_code(key)
        bucket_index = hash_code % self.nbuckets

        matching_bucket = self.bucket_list[bucket_index]
        for entry in matching_bucket:
            print(entry)

    def put(self, key, value):
        hash_code = self.calc_hash_code(key)
        bucket_index = hash_code % self.nbuckets

    # Creating a TUPLE containing the key and the value
        key_val_tuple = (key, value)

    # Adding the TUPLE to the appropriate bucket
        self.bucket_list[bucket_index].append(key_val_tuple)


    def calc_hash_code(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code


hashtable = HashTable(10)

hashtable.put("cat", "A furry 4 leg animal that goes Meow!")
print(hashtable)

print(hashtable.get("cat"))