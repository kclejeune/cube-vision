# Cube Vision

## Installing Dependencies

To install the python deps, run the following command from the project root:

```
pip3 install -r requirements.txt
```

## Running Project

To see the options allowed run:
```
python3 main.py -h
```

### Generating Solutions

We have provided 3 image sets (or Series) of scrambled cubes. Series 2 is the most effective - it can be run from the project root with

```
python3 main.py -s 2
```

## Additional Image Generation

To generate the orb image as seen in the report, run the following commands:

```
cd extensions
python3 features.py
```
