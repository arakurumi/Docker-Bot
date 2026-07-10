#!/bin/sh
export CC=clang
apk add --no-cache --virtual BuildDependency build-base clang curl-dev
pip install --break-system-packages --no-cache-dir pycurl TgCrypto
apk del BuildDependency
