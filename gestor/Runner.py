import argparse
import subprocess

if __name__ == '__main__':
     feature_tag = '-t generar_cookies'

     command = f'behave -k {feature_tag} --no-capture '

     rs = subprocess.run(f'{command}', shell=True)
