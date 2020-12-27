#!/usr/bin/env python3

'''
Data loader module
'''

import configparser
import json
import sys

import xmltodict
import yaml


def load_data_ini(fin):
    '''
    load data in ini format;

    ##  params

    fin:file object
    :   data file object;

    ##  return

    :dict
    :   data;
    '''

    cp = configparser.ConfigParser()
    cp.read_file(fin)
    return {s: dict(cp.defaults(), **cp[s]) for s in cp.sections()}


def load_data_json(fin):

    '''
    load data in json format;

    ##  params

    fin:file object
    :   data file object;

    ##  return

    :dict
    :   data;
    '''

    return json.load(fin)


def load_data_xml(fin):

    '''
    load data in xml format;

    ##  params

    fin:file object
    :   data file object;

    ##  return

    :dict
    :   data;
    '''

    return xmltodict.parse(fin.read())


def load_data_yaml(fin):

    '''
    load data in yaml format;

    ##  params

    fin:file object
    :   data file object;

    ##  return

    :dict
    :   data;
    '''

    return yaml.safe_load(fin)


def load_data(fname, fmt, defines):

    '''
    load data;

    ##  params

    fname:str
    :   data file name;
    fmt:str
    :   data format;
    defines:list
    :   data defined as command line arguments;

    ##  return

    :dict
    :   data;
    '''

    data = {}

    if fname is not None:
        #  get input file object;
        if fname == '-':
            fin = sys.stdin
        else:
            fin = open(fname, 'rt')

        try:
            #  detect data format;
            if fmt is None:
                if fname.endswith('.ini'):
                    fmt = 'ini'
                elif fname.endswith('.json'):
                    fmt = 'json'
                elif fname.endswith('.xml'):
                    fmt = 'xml'
                elif fname.endswith('.yaml'):
                    fmt = 'yaml'
                else:
                    raise Exception('no data format;')

            #  load data;
            if fmt == 'ini':
                data = load_data_ini(fin)
            elif fmt == 'json':
                data = load_data_json(fin)
            elif fmt == 'xml':
                data = load_data_xml(fin)
            elif fmt == 'yaml':
                data = load_data_yaml(fin)
            else:
                raise Exception('invalid data format: {};'.format(fmt))

        finally:
            fin.close()

    #  merge in command line data;
    if defines is not None:
        data.update(defines)

    return data
