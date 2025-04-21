from typing import Any

#Tuple mutability
tuple_1 = (
    1,
    "hello",
    [2, 3],
    1
)

print("Tuple:", tuple_1)

tuple_1[2].append(5)

print("Tuple:", tuple_1)

#Tuple hashing dut to mutability
def is_hashable(python_obj: Any) -> bool:
    try:
        hash(python_obj)
    except TypeError as e:
        print(e)
        return False
    
    return True
    

if __name__ == "__main__":
    tuple_2 = (1, 2, [1, 2, 3])
    print(is_hashable(tuple_2))

    tuple_3 = (1, 2, (3, 'HELLO'), 5)
    print(is_hashable(tuple_3))

    tuple_4 = (1, 2, [3], 4, 5)
    print(is_hashable(tuple_4))