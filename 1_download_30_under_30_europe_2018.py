from splinter import Browser
import pandas as pd
import time
#Author - Florin Badita 

url = "https://www.forbes.com/30-under-30-europe/2018/#62f813ed7eaa"
b = Browser()  # open a chrome browser
b.visit(url)  # goes to the url
list_of_links = b.find_link_by_partial_href('/30-under-30-europe/2018/') #Identify all of the links that contains this value

def create_link_list(list_of_links):
    proper_list = [] #create new empty list
    for x in list_of_links: #Iterate on every value from link_of_links
        proper_list.append(x['href']) #https://stackoverflow.com/questions/21816397/get-href-value-in-splinter
    return proper_list

def inside_page (x):
    search_results_css = '#row-2 .ng-binding' #css selector
    search_results = b.find_by_css(search_results_css)  # returns list of category elements
    scraped_data = []
    for search_result in search_results: # iterate through list of category elements
        title = search_result.text.encode('utf8')  # trust me, clean data
        category = b.title # We can extract the category from the title displayed on the page.
        link = x #not working
        print(title,category, link)
        scraped_data.append((title, category, link)) #Append data

    df = pd.DataFrame(data=scraped_data, columns=["title", "category", "link"]) # put all the data into a pandas dataframe

    df.to_csv("30_under_30.csv", mode='a', header=False)  # export to csv

for x in create_link_list(list_of_links): #Iterate on every value from list_of_links
    b.visit(x) #visit the page
    inside_page(x)
    print (x)
    time.sleep(5) #Sleep 5 seconds between seach new page

b.quit() #We close the Browser.

# Initial plan

#download html page https://www.forbes.com/30-under-30-europe/2018/#62f813ed7eaa
#get all links
#filter just the sublinks from /2018/ with https://www.forbes.com/30-under-30-europe/2018/art-culture
#save the list to 30_under_30_categories

#download html context from each link from 30_under_30_categories
#proess the html table and extract the name, age, field, company, role, html_link and save it in a list called 30_under_30_finalists
#save the 30_under_30_finalists list as a csv

#Download linkedin information for each user
#Add the results for the other participants that were not found automatically.
