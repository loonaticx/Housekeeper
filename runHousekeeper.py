import argparse
import os
import housekeep
allFiles = []

parser = argparse.ArgumentParser()
parser.add_argument('--all-phases', '--all_phases', action='store_true', help='Convert all phase files folders. (3 to 14)')
parser.add_argument('--selected_phases', '--phase', action='extend', nargs='+', type=str, metavar='3 3.5 4', help='List phase files folders to convert.')
parser.add_argument('--recursive', '-r', action='store_true', help='Convert all folders in the directory, recursively. Typically used if there are models outside of "phase" folders.')
args = parser.parse_args()
if args.all_phases:
    args.selected_phases = ['3', '3.5', '4', '5', '5.5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
recursive = args.recursive
selectedPhases = args.selected_phases

recursive = True
inputFile = ".png" # for now
verbose = True

if recursive: # Recursion time!
	for phase in selectedPhases:
		if not os.path.exists('phase_%s' % phase):
			continue
		for root, _, files in os.walk('phase_%s' % phase):
			for file in files:
				if not file.endswith(inputFile): # Input file
					continue
				if verbose:
					print("Adding %s" %file)
				file = os.path.join(root, file)
				allFiles.append(file)
else:
	for file in os.listdir('.'):
		if not file.endswith(inputFile):
			if verbose:
				print("Skipping %s" % file)
			continue
		if verbose:
			print("Adding in %s" % file)
		allFiles.append(file)

Housekeep = housekeep
Housekeep.Housekeep(allFiles)