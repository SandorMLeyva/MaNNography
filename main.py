#!/home/alex/anaconda3/bin python3
# coding: utf-8

import mannography as mnn
import sys

def main():
    builder = mnn.Builder()
    fire.Fire(builder.find_file)

def nofire(path):
    builder = mnn.Builder()
    builder.find_file(path)

if __name__ == "__main__":
    if "--nofire" in sys.argv:
        nofire(sys.argv[2])
    else:
        import fire
        main()