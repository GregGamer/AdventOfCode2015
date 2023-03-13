# Get number of the new Day
$days = ls Day*
$lastday = ($days[-1].Name -split "_")[1]
$lastday = [int]$lastday
$daynumber = $lastday+1
$daynumber = '{0:d2}' -f $daynumber
$newday = 'Day_' + $daynumber

# Create Folder Structure
New-Item $newday -ItemType Directory
cd $newday
$temp = "day_"+$daynumber+"a.py"
New-Item $temp -ItemType File
$temp = "day_"+$daynumber+"b.py"
New-Item $temp -ItemType File
New-Item 'input.in' -ItemType File
