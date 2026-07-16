import sys
import time

print("===파이썬 list, tuple, dict 비교 데모 ===")

# 1. 생성 시간 비교.
def measure_creation_time():
    start = time.time()
    lst = [i for i in range(1000000)]
    list_time = time.time() - start

    start = time.time()
    tpl = tuple(i for i in range(1000000))
    tuple_time = time.time() - start

    start = time.time()
    dct = {i: i for i in range(1000000)}
    dict_time = time.time() - start

    print(f"[생성시간 비교 (100만 항목)]")
    print(f"List 생성시간  :{list_time:.6f}초")
    print(f"Tuple 생성시간 : {tuple_time:.6f}초")
    print(f"Dict 생성시간: {dict_time:.6f}초")

# 2. 메모리 사용 비교.
def measure_memory_usage():
    lst = [0] * 1000
    tpl = tuple(lst)
    dct = {i: 0 for i in range(1000)}

    print("[메모리 사용량 비교 (1000 개 항목)]")
    print(f"List 메모리: {sys.getsizeof(lst)} bytes")
    print(f"Tuple 메모리: {sys.getsizeof(tpl)} bytes")
    print(f"Dict 메모리: {sys.getsizeof(dct)} bytes")

# 3. 변경 가능 여부.
def mutability_demo():
    print("[변경 가능성(Mutablity)]")
    lst = [1, 2, 3]
    tpl = (1, 2, 3)
    dct = {'a': 1, 'b': 2}

    lst[0] = 99
    print(f"List 변경: {lst}")

    try:
        tpl[0] = 99 # 수정 불가하므로 오류 발생.
    except TypeError as e:
        print(f"Tuple 변경: {e}")

    dct['a'] = 99
    print(f"Dict 변경: {dct}")

# 4. 탐색 속도 비교
def lookup_demo():
    print("[탑색 속도 비교]")
    lst = list(range(100000))
    dict = {i: i for i in range(100000)}

    start = time.time()
    _ = 99999 in lst
    lst_lookup = time.time() - start

    start = time.time()
    _ = 99999 in dict
    dict_lookup = time.time() - start

    print(f"List 에서 값 찾기: {lst_lookup:.6f}초")
    print(f"Dict 에서 값 찾기: {dict_lookup:.6f}초")

# 실행.
measure_creation_time()
measure_memory_usage()
mutability_demo()
lookup_demo()