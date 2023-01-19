# Namesong

There's an idea in music to convert text (usually names obviously) into melodies. I think of this from time to time but
never try out melodies generated this way because it's a bummer. I'm hoping to make it a little less of a bummer here.

## Usage

```
kevinfarrow@Kevins-MBP namesong % ./namesong.py --help
Usage: namesong.py [OPTIONS]

Options:
  -i, --input TEXT                Input to songify
  -s, --scale [major|minor|chromatic]
                                  Scale of melody to create
  -a, --accidentals [sharps|flats]
                                  (For use with chromatic scales) Sharps or
                                  flats?  [default: sharps]
  -f, --flavor [natural|melodic]  (For use with minor scales) Which flavor
                                  minor scale?  [default: natural]
  -v, --verbose                   Show verbose output
  --help                          Show this message and exit.
```


## Some ideas on what to use it for

1. As a real melody, duh.
2. Goal notes (fill in and make it sound good)