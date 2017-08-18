## Creating the stoplist

We use a simple set of shell commands, chained together, to produce a term frequency list of words ordered by number of uses:

`tr '[:upper:]' '[:lower:]' < brandes_lv1_1905.xml | tr -sc '[:alpha:]' '\n' | sort |  uniq -c | sort -n -r`

How many of these to use? More of an art than a science. The earliest "content-bearing" words in the list, descending from the top, are proably `Paris`, `ung` and `unge`. 
