def dwn_epi():

	br.get(lnk)
	sleep(5)
		
	scc="Downloded episode {}."
	c="maxbutton-{}-container mb-container"
	for i in range(7,20):
		try:
			#print(c.format(i))
			k='//*[@class="'+c.format(i)+'"]/a'	
			Episode1=br.find_element_by_xpath(k).get_attribute("href")
			br.get(Episode1)
			sleep(3)


			InstantDownload=br.find_element_by_id("editPrivacyBtn").get_attribute("onclick")
			InstantDownload=(InstantDownload.split("'"))
			br.get(InstantDownload[1])
			#sleep(7)

			x='//*[@id="status"]/div[1]/a[1]'
			Download=br.find_element_by_xpath(x).get_attribute("onclick")
			Download=(Download.split("'"))
			br.get(Download[1])

			print(scc.format(i-6))
			br.get(lnk)
			sleep(3)
		except:
			print("end")
			
a=""" 
-----____----_______------______-----
"""
from selenium import webdriver
from time import sleep


loc=".\\Driver\\chromedriver.exe"

name=input("Type a Name to find: ")
br=webdriver.Chrome(loc)
url="https://themoviesflix.io/?s="
br.get(url+name)
sleep(2)
k='//*[@class="latestPost excerpt "]/a[1]'	
item=br.find_element_by_xpath(k).get_attribute("href")
br.get(item)
sleep(1)
print("")

gd='//*[@class="maxbutton-13 maxbutton maxbutton-g-direct-1"]' #6
gd_d=br.find_elements_by_xpath(gd)
lnk_lst=[]
for co_lnk in gd_d:
	co_lnk=co_lnk.get_attribute("href")
	lnk_lst.append(co_lnk)

#print(lnk_lst)
for lnk in lnk_lst:
	print(a)
	dwn_epi()




