#!/usr/bin/python3

import time
import multiprocessing
import logging
import requests

from utils import check_website
from utils import WEBSITE_LIST

NUM_WORKERS = 3

if __name__ == '__main__':
	start_time = time.time()
	
	with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
		results = pool.map_async(check_website, WEBSITE_LIST)
		results.wait()
		print(results)
		
	end_time = time.time()
	print("Time for multiprocessing: %s secs" % (end_time - start_time))

