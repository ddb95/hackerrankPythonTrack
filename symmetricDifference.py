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
    main_list = lst + lst1
    main_list = sorted(main_list)
    for i in range(len(main_list)):
        print(main_list[i])


