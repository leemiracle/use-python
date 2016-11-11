"""
argparse:代替optparse,命令行选项,参数和子命令的解析器
"""

import argparse

def test_argparse_interact_with_comandline():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    test_argparse_interact_with_comandline()
