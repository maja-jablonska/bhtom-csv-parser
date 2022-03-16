from typing import Dict

import pandas as pd
import click


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-p', '--out-filename-prefix', default='out',
              help='Prefix of result filenames. Files will be saved as prefix_filter.csv')
def main(filename: str, out_filename_prefix: str):
    print(f'Splitting {filename} to filters...')
    df: pd.DataFrame = pd.read_csv(filename, sep=';')
    
    for filter in df.Filter.unique():
        filter_filename: str = f'{out_filename_prefix}_{filter}.csv'
        print(f'Saving filter {filter} to {filter_filename}')
        df[df.Filter==filter].to_csv(filter_filename)
        
    print('Finished!')
        
        
if __name__ == '__main__':
    main()