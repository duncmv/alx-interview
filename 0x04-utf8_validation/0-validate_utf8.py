#!/usr/bin/python3
"""Validate utf8"""


def validUTF8(data):
    """validates dats for utf-8"""
    try:
        bytes(data)
        return True
    except Exception as e:
        return False
