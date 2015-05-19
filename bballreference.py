'''
Script to pull and store all data in basketball reference

'''

import string
from bs4 import BeautifulSoup
import urllib2

def getData():
	base_url = "http://www.basketball-reference.com/leagues/NBA_XX_totals.html"
	start_year = 1976
	end_year = 2015
	for i in range(start_year,end_year+1):
		year = str(i)
		url = string.replace(base_url, 'XX', year)
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page, "html5lib")
		rows = soup.findAll("tr", { "class" : "full_table" })
		print year
		for row in rows:
			#player = {}
			#player[name] = 
			cells = row.findAll("td")
			player = [t.text for t in cells]
			# Structure of playeR: Rk	Player	Pos	Age	Tm	G	GS	MP	FG	FGA	FG%	3P	3PA	3P%	2P	2PA	2P%	eFG%	FT	FTA	FT%	ORB	DRB	TRB	AST	STL	BLK	TOV	PF	PTS



if __name__=='__main__': 
	#print getData(genURLs())
	print getData()
