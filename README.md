# WPS-Plugins-wordlist
Revision 2076628 Wordpress Plugins List

Currently, as or right now, there are no wordlists on Github that are this huge to search for plugins using Wordpress. This list is directly scraped from Wordpress.org (http://plugins.svn.wordpress.org/) that contain a vast array of plugins that are non-existent on the market. The amount of lines is 80,806 (4/28/19) and there are only 55,055 plugins according to https://wordpress.org/plugins/ this is super helpful for reconnaissance.

How to scrape your own list:
1. Visit http://plugins.svn.wordpress.org/ and copy and paste the list into a text file
2. Remove all of the unwanted stuff
3. Run the command line (sed -e 's/\/$//' input.txt > output.txt) to remove the trailing forward slash
4. Then run via command line, (sed -i 's/ //g' file.txt > output2.txt) to remove the whitespace at the beginning of each line.
