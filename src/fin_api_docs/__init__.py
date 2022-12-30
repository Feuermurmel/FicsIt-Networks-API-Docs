import argparse
import logging
import sys
from argparse import Namespace
from pathlib import Path

from fin_api_docs.generator import main
from fin_api_docs.util import UserError


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=Path, default=Path('FicsIt-Networks-API-Docs'), dest='output_path')
    parser.add_argument('-c', '--clear', action='store_true')
    parser.add_argument('input_json_path', nargs='?', type=Path)

    return parser.parse_args()


def entry_point() -> None:
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    try:
        main(**vars(parse_args()))
    except UserError as e:
        logging.error(f'error: {e}')
        sys.exit(1)
    except KeyboardInterrupt:
        logging.error('Operation interrupted.')
        sys.exit(130)
