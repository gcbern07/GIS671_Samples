##code sample for extracting suffix from file name
#assumptions: file name will contain only one period, the period preceding the file suffix

#assign name of file to variable named filename
filename = 'buildings.dbf'

#Find the location of the period in the file name. This index number will be
#assigned to the variable named start
start = filename.find('.')

#string indexing is used to extract everything after the period
#and assign it to the variable named suffix. 1 is added to the start position
#to begin with the character after the period (not include the period). Nothing
#is included after the colon to capture everything to the end of the value. It
#will work regardless of the suffix length (.py, .shp, .jpeg)
suffix = filename[start+1:]

#print the value of the suffix (should be dbf)
print suffix
