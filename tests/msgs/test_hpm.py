#!/usr/bin/env python

from array import array

from nose.tools import eq_, raises

import pyipmi.msgs.hpm

from pyipmi.errors import DecodingError, EncodingError
from pyipmi.msgs import encode_message
from pyipmi.msgs import decode_message


def test_decode_valid_req():
    m = pyipmi.msgs.hpm.ActivateFirmwareReq()
    decode_message(m, '\x00\x01')
    eq_(m.picmg_identifier, 0)
    eq_(m.rollback_override_policy, 1)

def test_encode_valid_req():
    m = pyipmi.msgs.hpm.ActivateFirmwareReq()
    m.picmg_identifier = 0
    m.rollback_override_policy = 0x1
    data = encode_message(m)
    eq_(data, '\x00\x01')

def test_decode_valid_req_wo_optional():
    m = pyipmi.msgs.hpm.ActivateFirmwareReq()
    decode_message(m, '\x00')
    eq_(m.picmg_identifier, 0)
    eq_(m.rollback_override_policy, None)

def test_encode_valid_req_wo_optional():
    m = pyipmi.msgs.hpm.ActivateFirmwareReq()
    m.picmg_identifier = 0
    m.rollback_override_policy = None
    data = encode_message(m)
    eq_(data, '\x00')