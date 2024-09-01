from typing import List

def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    length_of_original_array: int = len(original)
    if length_of_original_array / m != n:
        return []
    result_array: List[List[int]] = [[0]*n for i in range(m)]
    f = 0
    for i in range(m):
        for j in range(n):
            result_array[i][j] = original[f]
            f += 1
    return result_array

def print2DArray(array: List[List[int]]) -> None:
    for row in array:
        for element in row:
            print(element, end=" ")
        print()
        
def main() -> None:
    array: List[int] = [1,2,3,4]
    array_2d: List[List[int]] = construct2DArray(original=array, m=2, n=2)
    print(array_2d)
    print2DArray(array=array_2d)
    
    array: List[int] = [1,2,3]
    array_2d: List[List[int]] = construct2DArray(original=array, m=1, n=3)
    print(array_2d)
    print2DArray(array=array_2d)
    
    array: List[int] = [1,2]
    array_2d: List[List[int]] = construct2DArray(original=array, m=1, n=1)
    print(array_2d)
    print2DArray(array=array_2d)

    array: List[int] = [1,3,3,5]
    array_2d: List[List[int]] = construct2DArray(original=array, m=3, n=1)
    print(array_2d)
    print2DArray(array=array_2d)

if __name__ == "__main__":
    main()