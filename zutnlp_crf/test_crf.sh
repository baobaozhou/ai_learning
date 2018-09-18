#!/usr/bin/env bash

LOCAL_PATH="$(cd `dirname $0`; pwd)"
# test Model Using CRF++ command
crf_test -m ${LOCAL_PATH}/crf_model ${LOCAL_PATH}/data > ${LOCAL_PATH}/datarst
# See how to predict, check the segmenter.py file under /deepnlp/segmenter.py
