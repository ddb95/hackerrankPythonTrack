if __name__ == '__main__':
    m = int(input())
    arr = list(map(int, input().split()))
    n = int(input())
    arr1 = list(map(int, input().split()))
    set_arr = set(arr)
    set_arr1 = set(arr1)
    set_arr_results = set_arr.difference(set_arr1)
    set_arr1_results = set_arr1.difference(set_arr)
    lst = list(set_arr_results)
    lst1 = list(set_arr1_results)
    for i in range(lst):
        print(lst[i])
        print('\n')
    for i in range(lst1):
        print(lst1[i])
        print('\n')

