#!/usr/bin/env python

"A regression example. Mostly the same, only importing from defs_regression."

import sys
import pickle
from pprint import pprint

from hyperband import Hyperband
from defs_regression.meta import get_params, try_params

try:
	output_file = sys.argv[1]
	if not output_file.endswith( '.p' ):
		output_file += '.p'	
except IndexError:
	output_file = 'results.p'
	
print("Will save results to "+output_file)

#

hb = Hyperband( get_params, try_params )
results = hb.run( skip_last = 1 )

print("%d total, best:\n"%( len( results )))
stuffs = sorted( results, key = lambda x: x['loss'] )[:5]
for r in stuffs:
	print("loss: %.2f | %f seconds | %.1f iterations | run %d "%(r['loss'], r['seconds'], r['iterations'], r['counter'] ))
	pprint( r['params'] )

print("saving...")

with open( output_file, 'wb' ) as f:
	pickle.dump( results, f )