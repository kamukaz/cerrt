
import sys
import os
import time
import hashlib
import binascii
import multiprocessing
from multiprocessing import Process, Queue
from multiprocessing.pool import ThreadPool
import threading
import base58
import ecdsa
import requests
 
if 1==1:
   file = open("found.txt","a")
   file.write("address: " + "\n" +
                   "private key: " + "\n" +
                   "WIF private key: "  + "\n" +
                   "public key: "  + "\n" +
                   "balance: "  + "\n")
