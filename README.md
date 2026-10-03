# Optimalish

Optimalish is a hyper-optimized version of the English language, in which the length of a word is directly determined by its frequency of usage. This means that frequently used words use fewer letters and infrequently words use more.

The translation from English to Optimalish works by turning the frequency-based index of each input word into a unique sequence of letters. We can think of the resulting sequence as the frequency index converted to base-26, except the most significant digit is zero-indexed (i.e. "a"=0, "aa"=26, "ba"=52). 

For translation, we use a dataset of the 100,000 most common English words in order of frequency, sourced from [Google Ngrams](https://books.google.com/ngrams/info).

If a word is not present in the dataset, the program returns "NaN" in its place.

## Usage
Run Translate.py with 2 arguments:
1. Mode = Can be 0 or 1. When translating from English to Optimalish use 0. Otherwise use 1.
2. Input = The text to be translated as a string. Only use letters and spaces. A space can only be used between words.
### Example  
```
python Translate.py 0 "Hello world"
>lrp dn
```
```
python Translate.py 1 "emn d bq ho"
>welcome to my house
```
