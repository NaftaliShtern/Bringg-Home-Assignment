from status_codes import StatusCode
import genes.config as config

def read_in_chunks(file, chunk_size=1024):
#It is recommended to use chunk_size >= len(prefix + Gen) in order to handle any Gen length
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data

def is_gen_in_chunk(chunk, Gen):
    if chunk.find(Gen) != -1:
        return True
    return False

def is_gen_in_file(f, Gen):
    previous_chunk_suffix = ''
    for chunk in read_in_chunks(f):
        ret_val = is_gen_in_chunk(previous_chunk_suffix + chunk, Gen)
        if is_gen_in_chunk(previous_chunk_suffix + chunk, Gen):
            return StatusCode.GenFound
        previous_chunk_suffix = chunk[-len(Gen):]
    return StatusCode.GenNotFound

def find(data_file_path, Gen, prefix = config.GEN_PREFIX):
    if not Gen.startswith(prefix):
        return StatusCode.GenNotFromSupportedTemplate
    with open(data_file_path) as f:
        return is_gen_in_file(f, Gen)
