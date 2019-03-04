#!/home/alex/anaconda3/bin python3
# coding: utf-8

import mannography as mnn
import fire

def main():
    builder = mnn.Builder()
    fire.Fire(builder.find_file)

if __name__ == "__main__":
    main()