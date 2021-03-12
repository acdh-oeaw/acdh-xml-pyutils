#!/usr/bin/env python

"""Tests for `acdh_xml_pyutils` package."""
import os

import pytest


# from acdh_xml_pyutils import acdh_xml_pyutils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests
    return requests.get('https://github.com/torvalds/linux')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
