"""Upload selected files to S3 storage"""
import argparse

from dotenv import dotenv_values
import boto3

BUCKET_NAME = 'pabd24'
YOUR_ID = '16'
CSV_PATH = ['data/raw/cian_flat_sale_1_50_moskva_14_May_2024_20_27_50_160555.csv',
            'data/raw/cian_flat_sale_1_50_moskva_14_May_2024_20_46_16_435813.csv',
            'data/raw/cian_flat_sale_1_50_moskva_14_May_2024_21_04_45_825201.csv']

config = dotenv_values(".env")
client = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=config['KEY'],
    aws_secret_access_key=config['SECRET']
)


def main(args):
    for csv_path in args.input:
        print(csv_path)
        remote_name = f'{YOUR_ID}/' + csv_path.replace('\\', '/')
        print(remote_name)
        client.download_file(BUCKET_NAME, remote_name, csv_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='+',
                        help='Remote data files to download from S3 storage',
                        default=CSV_PATH)
    args = parser.parse_args()
    main(args)
