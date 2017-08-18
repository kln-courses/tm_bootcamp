## Getting Started

At the R command prompt, paste:
```
if (!require(wordVectors)) {
if (!(require(devtools))) {
install.packages("devtools")
}
devtools::install_github("bmschmidt/wordVectors")
}
library(wordVectors)
library(magrittr)
```

## Prepare Levned texts

`prep_word2vec(origin="levned",destination="levned.txt",lowercase=T,bundle_ngrams=2)`

This takes all three text files in the levned directry and combines them into a levned.txt file. It also lowercases and "glues" common bigrams together with underscores ("`new_york`")

## Train a Word Embedding model

`model = train_word2vec("levned.txt","levned_vectors.bin",vectors=200,threads=4,window=12,iter=5,negative_samples=0)`
