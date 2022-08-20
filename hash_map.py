"""

create the best hash-map possible

"""

# todo rewrite the hash function and the rest to accommodate the changing behaviour
#  when the hash-map's load factor becomes too great or too small


class HashMap:
    def __init__(self, name: str, initial_size: int = 13):
        self.name = name
        self.occupancy = 0
        self.array_size = initial_size
        self.array = [None for _ in range(self.array_size)]

    @property
    def load_factor(self):
        """ optimally between .6 and .75 """
        return self.occupancy/self.array_size

    @staticmethod
    def hash(key: str, count_collisions: int = 0):
        key_bytes = key.encode()

        hash_code = sum(key_bytes)

        return hash_code + count_collisions

    def compress_function(self, hash_code: int):
        return hash_code % self.array_size

    # TEST FUNCTION
    # this function serves no functional purpose
    def compress_hash(self, key, count_collisions=0):
        return self.compress_function(self.hash(key, count_collisions))

    # setter function
    def assign(self, key, value):
        hash_index = self.compress_hash(key)

        current_array_value = self.array[hash_index]

        # check if the hash-index already contains anything
        if current_array_value is None:
            self.array[hash_index] = [key, value]
            return
        # if there already is a key, value stored, but the key is the same, reassign value
        elif current_array_value[0] == key:
            self.array[hash_index] = [key, value]
            return

        num_collisions = 1

        while current_array_value[0] != key:
            new_array_index = self.compress_hash(key, num_collisions)

            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return
            elif current_array_value[0] == key:
                self.array[hash_index] = [key, value]
                return

            num_collisions += 1

        return

    # getter function
    def retrieve(self, key) -> str | None:
        array_index = self.compress_hash(key)

        current_index_k_v = self.array[array_index]

        if current_index_k_v is None:
            return None
        elif current_index_k_v[0] == key:
            return current_index_k_v[1]

        else:
            num_collisions = 1

            while current_index_k_v[0] != key:
                new_array_index = self.compress_hash(key, num_collisions)

                current_index_k_v = self.array[new_array_index]

                if current_index_k_v is None:
                    return None
                elif current_index_k_v[0] == key:
                    return current_index_k_v[1]

                num_collisions += 1

        return None

    def resize(self):
        # todo when the load factor approaches an upper or lower limit
        #   the hash-map should resize to another size.
        # somewhere I heard that you should implement a size which is a prime and a hash which is a prime


