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
    """Kitten in color"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    output = ['<pre style="font: 10px/5px monospace;">']
    with open('kitten.color') as f:
        for line in black_white_kitten(environ, lambda x, y: None):
            for c in line:
                if c == '\n':
                    output.append('\n')
                    continue
                output.append(
                    '<span style="color: #{};">{}</span>'.format(
                        f.readline()[:-1],
                        c))
        output.append('</pre>')
        return output


def application(environ, start_response):
    app = choice((black_white_kitten, color_kitten))
    return app(environ, start_response)
