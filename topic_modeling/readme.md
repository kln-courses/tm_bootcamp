## Creating the stoplist

We use a simple set of shell commands, chained together, to produce a term frequency list of words ordered by number of uses:

`tr '[:upper:]' '[:lower:]' < brandes_lv1_1905.xml | tr -sc '[:alpha:]' '\n' | sort |  uniq -c | sort -n -r`

How many of these to use? More of an art than a science. The earliest "content-bearing" words in the list, descending from the top, are proably `Paris`, `ung` and `unge`.

## Splitting Levned into parts

We can use the “Section” structure of the XML files in Levned to chunk the text in semantic units.  We’ll do this using the unix csplit command.

There are a number of variants of csplit. They all seem to behave differently, allow different options, and even parse regular expressions differently. One that I’ve found to work well is the GNU version, available in the package “coreutilities” (through homebrew.) In the example below, ‘gcsplit’ means I’m invoking the GNU version of the tool, not the one that comes with OS X by default.

`gcsplit -z -k -f sections/brandes_lv1_1905 -b "%04d.txt" -n 4 brandes_lv1_1905.xml '/<head/' {*}`

`-z`  skip over files that would be empty.
`-k` keep all the output, even if it ends in an error.
`-f` preFix each resulting file with the directory name sections and the filename brandes_lv1_1905
`-b` Suffix the extension .txt onto the files. The other values are to inherit the right filename.
`-n 4` we expect no more than 9,999 resulting file in any one directory.  Change to -n 2 if, for example, you know the text will be cut up into under 100 chunks.
`'/<head/'` is the actual regular expression (within single quotes) that looks for a pattern specific to Levned. 


## Installing MALLET

[http://mallet.cs.umass.edu]

## Importing data into MALLET



