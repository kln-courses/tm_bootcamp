#!/bin/bash

for f in *.pdf
do
  echo "converting: - $f"
  pdftotext $f $f.txt
done
