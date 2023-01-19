#!/usr/bin/env python3


import click
import string
from numpy import unique
from output import message


alphabet = string.ascii_uppercase

scales = {
    'major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'minor': {
        'natural': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'melodic': ['A', 'B', 'C', 'D', 'E', 'F', 'G#'],
    },
    'chromatic': {
        'sharps': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
        'flats': ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
    },
}


def create_melody(input, scale):

    numbers = [ alphabet.index(x) for x in input ]
    notes = [ scale[n % len(scale)] for n in numbers ]

    return notes



@click.command()
@click.option('--input','-i',help='Input to songify',type=click.STRING)
@click.option('--scale','-s',help='Scale of melody to create',type=click.Choice(['major','minor','chromatic']))
@click.option('--accidentals','-a',help='(For use with chromatic scales) Sharps or flats?',default='sharps',show_default=True,type=click.Choice(['sharps','flats']))
@click.option('--flavor','-f',help='(For use with minor scales) Which flavor minor scale?',default='natural',show_default=True,type=click.Choice(['natural','melodic']))
@click.option('--verbose','-v',help='Show verbose output',is_flag=True)

def main(input, scale, accidentals, flavor, verbose):

    # purge non-alphabetical characters from input:
    input = [ x.upper() for x in input if x in string.ascii_letters ]
    if verbose: message(f"Purged input: {input}")

    selected_scale = scales[scale]
    if scale == 'chromatic':
        selected_scale = selected_scale[accidentals]
    elif scale == 'minor':
        selected_scale = selected_scale[flavor]
    
    if verbose:
        message(f"Selected scale ({scale}): {' '.join(selected_scale)}")

    melody = create_melody(input, selected_scale)

    message(f"Here's your melody! {' '.join(melody)}", status='green')
    message(f"And some stats:", level=1)
    message(f"Unique notes: {' '.join(unique(melody))}", level=1)
    


if __name__ == '__main__':
    main()