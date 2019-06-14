# WordPress-Plugins-wordlist
Revision 2076628 (4/28/19) | Wordpress Plugins wordlist

<b>Under development, manual scraping works as of right now.</b></br></br>
<b>To be used only for ethical penetration testing to help further secure vulnerabilities within the vast array of WordPress plugins.</b>

Software to be used with the list: WPScan

Currently, as of right now, there are no wordlists on Github that are this huge to search for plugins using Wordpress. This list is directly scraped from Wordpress.org (http://plugins.svn.wordpress.org/) that contain a vast array of plugins some of which are non-existent on the market. The amount of lines within the file is 80,086 (4/28/19) and there are only 55,055 plugins according to https://wordpress.org/plugins/. Ideally, this is super helpful for reconnaissance.

How to scrape your own list:
1. Visit http://plugins.svn.wordpress.org/ then copy and paste the list into a text file.
2. Remove all of the unwanted stuff.
3. Run the command line (sed -e 's/\/$//' list.txt > output.txt) to remove the trailing forward slash.
4. Then run via command line, (sed -i 's/ //g' output.txt > plugins.txt) to remove the whitespace at the beginning of each line.
