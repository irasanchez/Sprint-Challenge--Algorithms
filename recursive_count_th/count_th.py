'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    global th_count
    total_th_count = 0

    # return count if word has less than 2 characters
    if len(word) < 2:
        print("len less than 2 ", total_th_count)
        return total_th_count
    # recursive case:
    else:
        # take two items off the list, make a call with those two and a call with the rest
        if word[0:2] == "th":
            total_th_count += 1
            return total_th_count + count_th(word[2:])
        else:
            return total_th_count + count_th(word[1:])
