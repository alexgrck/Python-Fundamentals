alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]

def to_chunks(list_, chunk_length):
    how_many_chunks = len(list_) // chunk_length

    if len(list_) % chunk_length: how_many_chunks += 1

    chunks = []
    draft_list = list_
    idx = 0
    while idx < how_many_chunks:
        chunks.append(draft_list[:chunk_length])
        del draft_list[:chunk_length]
        idx += 1
    
    return chunks

