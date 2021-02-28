#Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 