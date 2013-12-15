#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Emanuele Bertoldi'
__version__ = '0.0.3'

from djangoerp.core.backends import ObjectPermissionBackend
from djangoerp.core.cache import LoggedInUserCache

ob = ObjectPermissionBackend()
logged_cache = LoggedInUserCache()

class FakeRequest(object):
    def __init__(self):
        self.META = {'HTTP_HOST': "myhost.com", 'HTTP_REFERER': "http://myhost.com/bookmarks/"}
