"""Launch only the reviewed runner with a newly exclusive-created console log."""
import argparse
import os
from pathlib import Path
import sys

def open_new_log(path):
 path=Path(path)
 fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 try:
  directory=os.open(str(path.parent),os.O_RDONLY)
  try:os.fsync(directory)
  finally:os.close(directory)
 except BaseException:
  os.close(fd);raise
 return fd

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--log',required=True);parser.add_argument('--output',default='confirmation_v1');args=parser.parse_args()
 fd=open_new_log(args.log)
 os.dup2(fd,1);os.dup2(fd,2)
 if fd not in (1,2):os.close(fd)
 env=os.environ.copy();env['CONFIRMATION_EXCLUSIVE_LOG']='1'
 os.execve(sys.executable,[sys.executable,'-u',str(Path(__file__).resolve().parent/'experiment.py'),'run','--output',args.output],env)

if __name__=='__main__':main()
