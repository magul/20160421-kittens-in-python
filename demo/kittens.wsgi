# -*- coding: utf-8 -*-

from random import choice


def black_white_kitten(environ, start_response):
    """Kitten in black and white"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    with open('kitten.data') as f:
        return f.readlines()


def color_kitten(environ, start_response):
    """Kitten in colour"""
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]



application = choice((blac_white_kitten, color_kitten))

if __name__ == '__main__':
    print application({}, lambda a,b: None)
