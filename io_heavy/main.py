# Copyright (c) 2022 Belmont Technology Inc. All rights reserved.
import time
import lorem
import os
import tempfile

def write_disk(num_sentences: int=10000):
    start = time.time()

    if num_sentences > 1000000:
        raise AssertionError("Please reduce the num_sentences to < 1,000,000")

    sentences = [lorem.sentence() for _ in range(num_sentences)]

    with tempfile.TemporaryDirectory() as td:
        f_name = os.path.join(td, 'test')
        with open(f_name, 'w') as fh:
            fh.writelines(sentences)

        print("Execution time : ", time.time() - start)

        return "File Size: " + str(os.path.getsize(f_name))
