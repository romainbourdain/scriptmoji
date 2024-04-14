import sys
from interpreter import parse
import argparse
from args import Parser


if __name__ == "__main__":
    parser = Parser()
    args = parser.parse_args()
