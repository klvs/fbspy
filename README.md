# fbspy: CS165

## Quick Start

```bash
# clone the repo and cd into it
git clone git@github.com:klvs/fbspy.git
cd ./fbspy
# start up simple python server
python -m SimpleHTTPServer 8080
```

And then point your browser at [http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html).

## Data

compressed.csv is the cleaned data. The raw data isn't included in this repo because it's some 90+ mb in size. The scripts I wrote to clean it (to it's current state) are included in the scripts directory.

The data comes from my facebook account so plz don't release it on the internet (unanonymized). You can harvest similar data yourself with [defaultnamehere/zzzzz](https://github.com/defaultnamehere/zzzzz). 

### Cleaning Steps
1. Concatenate and format the raw data into one file using scripts/format.py 
2. Using scripts/compress we compress the data by shortening the timestamp and coverting our data set from points to line segments.
3. We then remove the user ID column using excel or numbers

truncate.py -> compress.py -> fudgeIntervals.py -> classification.py