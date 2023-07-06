#!/bin/sh
cd ../builds/ ; find . -name "*.uf2" -execdir zip '{}.zip' '{}' \;

