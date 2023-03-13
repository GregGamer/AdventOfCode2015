# Global Variables
$YEAR = '2015'

# Get number of the new Day
$days = ls Day*
$lastday = ($days[-1].Name -split "_")[1]
$lastday = [int]$lastday
$daynumberINT = $lastday+1
$daynumber = '{0:d2}' -f $daynumberINT
$newday = 'Day_' + $daynumber

# Create Folder Structure
New-Item $newday -ItemType Directory
cd $newday
# Create File a with first Comment
$temp = "day_"+$daynumber+"a.py"
New-Item $temp -ItemType File
Set-Content -Path $temp -Value "# Challenge Link: https://adventofcode.com/$YEAR/day/$daynumberINT"
# Create File b with first Comment
$temp = "day_"+$daynumber+"b.py"
New-Item $temp -ItemType File
Set-Content -Path $temp -Value "# Challenge Link: https://adventofcode.com/$YEAR/day/$daynumberINT"
# Create input File 
New-Item 'input.in' -ItemType File
New-Item 'Jinput.in' -ItemType File
# Go out of the Folder
cd ..