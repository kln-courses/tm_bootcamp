#!/bin/bash

for f in *.doc
do
  echo "converting: - $f"
  catdoc $f > $f.txt
done
