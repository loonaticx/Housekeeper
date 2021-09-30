"""
runHousekeeper.py

By default, Housekeeper will just convert non-po2 images and any images with embedded icc/color profile
With the --optimize argument, Housekeeper will go through *every* single target image file it can find and optimize them.
Note that by running --optimize, the process will take much, much, longer to complete.
You cannot have both --dryrun and --optimize enabled at the same time. Dryrun is used to print out all files that would be
affected without actually converting anything.

"""

import argparse
import os, sys
import housekeep

allFiles = []

parser = argparse.ArgumentParser()
parser.add_argument('--selected_phases', '--phase', action='extend', nargs='+', type=str, metavar='3 3.5 4',
                    help='List phase files folders to convert.')
parser.add_argument('--optimize', '-o', action='store_true',
                    help='Will comb through all files and reexport them with PIL including the optimize arg.')
parser.add_argument('--dryrun', '-dr', action='store_true',
                    help='Will comb through the listed files and print out improper files, but will not convert any of them')

# parser.add_argument('--png', action='store_true', help='Convert PNG files (Default)')
# parser.add_argument('--jpg', action='store_true', help='Convert JPG files')
# parser.add_argument('--all-phases', '--all_phases', action='store_true', help='Convert all phase files folders. (3 to 14)')
args = parser.parse_args()

verbose = True  # set to False if you dont wanna see the Adding messages
all_phases = True  # just by default
if all_phases:
    args.selected_phases = ['3', '3.5', '4', '5', '5.5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
selectedPhases = args.selected_phases
opt = args.optimize
dryrun = args.dryrun
if opt and dryrun:
    print("You cannot have both optimize and dryrun setting enabled!")
    sys.exit()

if opt:
    print("Notice: Optimization mode enabled. This will take some time to complete.")

inputFile = (".png", ".jpg")

for phase in selectedPhases:
    if not os.path.exists('phase_%s' % phase):
        continue
    for root, _, files in os.walk('phase_%s' % phase):
        for file in files:
            if not (file.endswith(inputFile[0]) or file.endswith(inputFile[1])):  # Input file
                continue
            if verbose:
                print("Adding %s" % file)
            file = os.path.join(root, file)
            allFiles.append(file)

Housekeep = housekeep
Housekeep.Housekeep(allFiles, opt, dryrun)
print("Done")
