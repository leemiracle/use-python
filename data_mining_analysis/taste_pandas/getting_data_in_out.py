import pandas
import numpy
from io import BufferedReader,BytesIO


def test_read_csv():
    file_values = b'aa,bb,cc,dd\n' \
                  b'123,344,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123, ,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123,344,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123, ,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123,344,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123, ,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123,344,55,ss\n' \
                  b'123,344,55,35\n' \
                  b'123,,55,ss\n' \
                  b'3sd,zcvw,erw,35\n'
    # skipinitialspace:跳过分隔符后的空格
    pandas_file = pandas.read_csv(BufferedReader(raw=BytesIO(file_values)), dtype=numpy.object, skipinitialspace=True)