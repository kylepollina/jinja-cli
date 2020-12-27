#!/usr/bin/env python3

'''
main module;
'''

import os
from os.path import basename, dirname
import sys

import jinja2
from jinja2 import DictLoader, Environment, FileSystemLoader

from .loader import load_data
from .parse_args import parse_args


class RelEnvironment(jinja2.Environment):
    """Override join_path() to enable relative template paths."""
    def join_path(self, template, parent):
        return os.path.join(os.path.dirname(parent), template)


def main():
    '''
    main function;
    '''

    #  parse args;
    args = parse_args()

    #  load template;
    if args.template is None or args.template == '-':
        env = RelEnvironment(
            loader=DictLoader({'-': sys.stdin.read()}),
            keep_trailing_newline=True,
        )
        template = env.get_template('-')
    else:
        env = RelEnvironment(
            loader=FileSystemLoader(dirname(args.template)),
            keep_trailing_newline=True,
        )
        template = env.get_template(basename(args.template))

    #  load data;
    data = load_data(args.data, args.format, args.define)

    #  render template with data;
    rendered = template.render(data)

    #  write to output;
    if args.output is None or args.output == '-':
        fout = sys.stdout
    else:
        fout = open(args.output, 'wt')
    try:
        fout.write(rendered)
    finally:
        fout.close()


if __name__ == '__main__':
    main()
