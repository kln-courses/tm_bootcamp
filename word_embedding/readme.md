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

`prep_word2vec(origin="levned_stemmed",destination="levned.txt",lowercase=T,bundle_ngrams=2)`

This takes all three text files in the levned directry and combines them into a levned.txt file. It also lowercases and "glues" common bigrams together with underscores ("`new_york`")

## Train a Word Embedding model

`model = train_word2vec("levned.txt","levned_vectors.bin",vectors=200,threads=4,window=12,iter=5,negative_samples=0)`

## Word Similarity

`model %>% closest_to("paris")`

`model %>% closest_to("berlin")`

`model %>% closest_to("oversættelse")`

### Getting a longer list of similar words

`model %>% closest_to("kultur",40)`

### Similar terms to two or more words

`model %>% closest_to(model[[c("tyskland","berlin")]])`

## kMeans Clustering (Poor Man's Topic Model)

Imporant to understand that this is somewhat limited.  In Ben Schmidt's words,

>You can think of this as a sort of topic model, although unlike more sophisticated topic modeling algorithms like Latent Direchlet Allocation, each word must be tied to single particular topic.

To change the number of clusters, or `k`, change the number in `centers,20` to something else

```
set.seed(10)
centers = 150
clustering = kmeans(model,centers=centers,iter.max = 40)
sapply(sample(1:centers,20),function(n) {
names(clustering$cluster[clustering$cluster==n][1:10])
})
```

## Reducing space to a plane

Set up a tension or dichotomy 

`tyskland_danmark = model[[c("tyskland","danmark"),average=F]]`

Take just the most common 3,000 words

`tyskland_danmark_words = model[1:3000,] %>% cosineSimilarity(tyskland_danmark)`

Get the most "German" and most "Danish" words:

```
tyskland_danmark_words = tyskland_danmark_words[
  rank(-tyskland_danmark_words[,1])<20 |
  rank(-tyskland_danmark_words[,2])<20,
  ]
```
Plot the result:

```
plot(tyskland_danmark_words,type='n')
text(tyskland_danmark_words,labels=rownames(tyskland_danmark_words))
```

plot(sweet_and_saltiness,type='n')
text(sweet_and_saltiness,labels=rownames(sweet_and_saltiness))

## Entire model reduced to two dimensions using t-SNE:

`plot(model,perplexity=50)`
