import textwrap


def wrap(string, max_width):
    value = string

    # Wrap this text.
    wrapper = textwrap.TextWrapper(width=max_width)

    word_list = wrapper.wrap(text=value)
    # Print each line.
    for element in range(0,len(word_list)):
        print(word_list[element])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)



