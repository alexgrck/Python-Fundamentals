from random import randint

alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]


def to_chunks(list_: list):
    draft_list = list_
    result_list = []
    while draft_list:
        chunk = randint(4, 7)
        if len(draft_list) <= 14:
            if (len(draft_list) - chunk) >= 1 * 4:
                result_list.append(draft_list[:chunk])
                del draft_list[:chunk]
            elif 4 <= len(draft_list) <= 7:
                result_list.append(draft_list[: len(draft_list)])
                del draft_list[: len(draft_list)]
            continue
        else:
            result_list.append(draft_list[:chunk])
            del draft_list[:chunk]
    return result_list
