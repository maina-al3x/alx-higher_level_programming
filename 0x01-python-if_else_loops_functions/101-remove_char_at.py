#!/usr/bin/python3

def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        to_delete = str[n]
        new_str = ""
        for char in str:
            if char == to_delete:
                char = ''
            new_str = new_str + char
        return new_str
    else:
        return str
