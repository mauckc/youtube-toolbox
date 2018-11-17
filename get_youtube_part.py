import subprocess
from subprocess import call
import os
import argparse
import time

formatter = lambda prog: argparse.HelpFormatter(prog,
                                                max_help_position=36)
desc = '''
grabs youtube video by start_timestamp and duration
'''
parser = argparse.ArgumentParser(description=desc,
                                 formatter_class=formatter)

parser.add_argument('-vf', '--input-video',
                    help='input video',
                    metavar='<file>',
                    default='https://www.youtube.com/watch?v=izTaPcZZAXs')

parser.add_argument('-o', '--output_path',
                    help='output location',
                    default='./',
                    metavar='<path>')

parser.add_argument('-ss', '--start',
                    help='specify a start timestamp',
                    default='00:00:05')#,
                    #metavar='<path>')

parser.add_argument('-t', '--duration',
                    help='encoding duration',
                    default='00:00:10')#,
                    #metavar='<path>')

args = vars(parser.parse_args())

if not args['input_video']:
    parser.error("must specify -vf youtube link between quotes")

myvidpath = args['input_video']
start_timestamp = args['start']
duration = args['duration']
output_path = args['output_path']

output_prefix = "processed-out-"
out_prefix = "out-"

myvidpath_s = str(myvidpath)

out_grab = subprocess.Popen(["youtube-dl", "-g", myvidpath_s],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)

stdout,stderr = out_grab.communicate()
print((stdout,stderr))

nextData = stdout.split()[0]

now_time = time.time()
out_time = str(now_time).replace('.','-')

sample_call = "".join(("ffmpeg ","-i ", nextData ," -ss ",start_timestamp," -t ",duration, " ",output_path ,out_prefix, out_time,".mp4"))
sample_call_list = sample_call.split()
out_process = subprocess.Popen(sample_call_list)
