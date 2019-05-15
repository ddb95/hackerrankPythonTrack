def merge_the_tools(string, k):
    # arr = []
    # clean_str = []
    # if len(string) % k == 0:
    #     for i in range(0, len(string), k):
    #         arr.append(string[i:i + k])
    #     for i in range(0, len(arr)):
    #         clean_str.append("".join(set(arr[i])))
    #     for i in range(len(clean_str)):
    #         print(clean_str[i])
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
