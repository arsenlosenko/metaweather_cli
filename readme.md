# Metaweather CLI

## App Setup 
```
git clone <link to repo>
cd weather_cli
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
python weather.py --query <name of the city>
python weather.py --query London

OR 

python weather.py --latt <lattitude> --long <longitude>
python weather.py --latt 36.96 --long -122.02
```