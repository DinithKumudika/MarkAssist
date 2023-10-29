from fastapi import UploadFile

import time
import lzma
import gzip
import bz2

def compress_file(file: str):
     compress_file = file.split('.')[0] + ".xz"
     start = time.time()
     with open(file, 'rb') as f_in, lzma.open(compress_file, 'wb') as f_out:
          f_out.write(f_in.read())
     end = time.time()
     return f"compressed in {end-start}"


def compress_uploaded_file(file: UploadFile):
     filename = file.filename
     compress_file = filename.split('.')[0] + ".xz"
     start = time.time()
     with open(file, 'rb') as f_in, lzma.open(compress_file, 'wb') as f_out:
          f_out.write(f_in.read())
     end = time.time()
     return f"compressed in {end-start}"


def decompress_file(file: str, ext: str):
     decompress_file = file.split('.')[0] + "." + ext
     start =  time.time()
     with lzma.open(file, 'rb') as f_in, open(decompress_file, 'wb') as f_out:
          f_out.write(f_in.read())
     end = time.time()
     return f"decompressed in {end-start}"