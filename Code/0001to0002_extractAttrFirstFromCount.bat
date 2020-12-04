cd "C:\Users\beluga\Desktop\TIL\TIL"

call Scripts\activate.bat

cd "C:\Users\beluga\Desktop\TIL\MyCode"

echo ==============Start===============

echo Start Monitor 
python 0001to0010.py -in ../Data/eye_df.csv -out ../Data/eye_df_count.xlsx -n 200
echo Start RiceCooker 
python 0001to0010.py -in ../Data/lip_df.csv -out ../Data/lip_df.xlsx -n 200
echo Start TV 
python 0001to0010.py -in ../Data/ramen_df.csv -out ../Data/ramen_df.xlsx -n 200
echo Start Vacuum 
python 0001to0010.py -in ../Data/snack_df.csv -out ../Data/snack_df.xlsx -n 200

echo ==============done===============


pause

