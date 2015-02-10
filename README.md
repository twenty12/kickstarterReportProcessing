Job Notes and Documentation for Public Radio
--------------------------------------------

**Problem:** There are an unknown number of backers who have misunderstood the operating conditions of Public Radio. These backers have requested radios tuned to stations far outside their area of reception.

**Delivered Solution:** 

 - A program that estimates a backers received signal strength based on
   data from KickStarter and the FCC. Definitions and material from this

 - Sorted lists of backers
-- */reports/international.csv* List of backers without shipping address or with international shipping addresses.

   --*/reports/problem.csv* List of backers with station call letters that can not be found or do not match the frequency they entered.   
   
   --*/reports/all_cleaned.csv* List of backers for with the following appended columns Confirmed radio station and call number Backer geo
   coordinates Station geo coordinates Distance between backer and
   station Estimated signal strength between backer and station  
   
   --*/reports/in_range.csv* Backers within 75 miles of station requested  /reports/out_range.csv Backers farther than 75 miles from station

**About the base directory:**
	All the code from this project is inside the /public_radio/ directory. Each script is setup to run in that directory on any system. 

**About */get.py*:**
	This script is the workhorse of this project, it executes all the definitions written in /defs.py. It pulls all the backer names from the files inside the /backer_reports(raw)/ directory. Before processing the backer information it checks all against all backers in the /reports/ directory. 

**About */sort.py:***
This script sorts all the entries in /reports/all_cleaned.csv into two files; /reports/in_range.csv and /reports/out_range.csv. The cut off is set to 75 Kilometers. This is adjustable and could switched to use the signal strength metric. 

**About */write_files.py*:**
This script writes the files that are later inputted to. Running these will delete the existing files and replace them with empty .cvs files. 

**Minimizing backers unprocessable call letters:**
There is a significant list of backers for whom call numbers where not found on the FM station list. Many of these are do to simple errors and could be easily correct by hand. Making those corrections would involve the following:
Find and correct backer info on the original file in /backer_reports(raw)/ directory.
Use a text editor for this. Do not use Excel to save the file (this will cause a formatting problem).
Delete the entries from */reports/problem.csv*
Run  */get.py*  


**Monitoring progress:**
	Everything is run by executing the /get.py script. Each entry takes a minimum of  6 seconds to process. To monitor the progress of the script a variety of outputs are printed during each of the process. 

**Note 1:**
	The Google maps API is not reliable enough for high volume requesting. Both the Google maps API and Bing maps API are used to retrieve data. 

**Note 2:**
	PO Box addresses are processed with geo coordinates from the associated city. 

The Google maps API is needed for processing PO box entries and other less formally formatted addresses (Apt numbers etc). Occasionally the Google API becomes completely unresponsive with an address that is unprocessable by the Bing API. Restarting the script reestablishes the connection with Google and will fix the problem.

**Note 4:**
	Equation for distance between points on a sphere are. 
d = acos( sin φ1 ⋅ sin φ2 + cos φ1 ⋅ cos φ2 ⋅ cos Δλ ) ⋅ R

**Future developments:**
	Minimizing the number of unprocessable call numbers requires more refined use of regular expressions and conditional statements. Extensive time spent building a robust system for processing that information was not in the scope the original project outline. 
 
**For the web:**
	Researching, designing, and building this system into the web is a different project which will use elements of this project. 
![alt tag](http://danielgladstone.com/media/uploads/public_radio_updated.png)
