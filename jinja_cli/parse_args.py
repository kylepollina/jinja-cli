#!/usr/bin/env python3

'''
Argument Parser
'''

import argparse

import argparse_ext

#  program name;
prog = 'jinja'


def parse_args():
    '''
    parse command line arguments;
    '''

    #  init arg parser;
    parser = argparse.ArgumentParser(
        prog=prog,
        description='a command line interface to jinja;',
        formatter_class=argparse_ext.HelpFormatter,
        add_help=False,
    )

    #  add arg;
    parser.add_argument(
        '-h', '--help',
        action='help',
        help='display help message;',
    )

    #  add arg;
    parser.add_argument(
        '-D', '--define',
        action='append',
        nargs=2,
        type=str,
        metavar=('key', 'value'),
        help='define data;',
    )

    #  add arg;
    parser.add_argument(
        '-d', '--data',
        type=str,
        metavar='file',
        help='data file;',
    )

    #  add arg;
    parser.add_argument(
        '-f', '--format',
        type=str,
        metavar='format',
        help='data format;',
    )

    #  add arg;
    parser.add_argument(
        '-o', '--output',
        type=str,
        metavar='file',
        help='output file;',
    )

    #  add arg;
    parser.add_argument(
        'template',
        nargs='?',
        type=str,
        metavar='template',
        help='template file;',
    )

    #  parse args;
    args = parser.parse_args()

    return args
