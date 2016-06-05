# python ./scripts/format.py &&
python ./scripts/compress.py && 
python ./scripts/removeUID.py &&
python ./scripts/fudgeIntervals.py $1 &&
rm compressed.csv &&
rm removed_uid.csv 
# &&
# sed -i '1s/^/<added text> /' $1
# rm concat.csv
# rm raw.csv
