from splinter import Browser
import pandas as pd
import time
from random import randint

b = Browser()  # open a firefox browser

df = pd.read_csv('30_under_30.csv')
website_target = 'linkedin.com/in' # change with twitter/instagram, etc

def google_search(website_target, founder_name,founder_company_and_role):
    x = str("https://duckduckgo.com/?q=" + str(website_target) + "+" + str(founder_name) + "+" + str(founder_company_and_role)) #Here we create the string that we will use to search in duckduckgo
    b.visit(x) # this tells the browser to visit the link

    linkedin_profiles = (b.find_by_css('.result__a')) #get all results
    linkedin_profile = linkedin_profiles[0].outer_html #extract just the first result

    linkedin_name = (b.find_by_css('#r1-0 .result__a')).value #Extract the first result name

    return linkedin_name,linkedin_profile #return 2 variables

df['linkedin_profile'] = "dummy"
df['linkedin_name'] = "dummy"

# df_slice = df.ix[7:10] # debug - uncomment this to get only some the rows
# df = df_slice #debug
for index, row in df.iterrows():

    print (df.ix[int(index), 1])
    founder_age_country = (df.ix[int(index), 1]) #Extract the age and the country
    founder_company_and_role = (df.ix[int(index), 2]) #Extract the company and the role
    founder_name = founder_age_country.split(',', 1)[0]  # Extract just the name of the user
    print (founder_name) #print to the console the founder name
    print (founder_company_and_role) #print to the console the company and the role of the person
    # here we perform a google search, and return the name and the link that we get from the first result in google
    results = (google_search(website_target, founder_name, founder_company_and_role))

    try :
        linkedin_name = (results[0])  # return name from google search
        linkedin_profile = (results[1])  # return link from google search
    except:
        linkedin_name = "failed_to_download"
        linkedin_profile = "failed_to_download"

    print (linkedin_name,linkedin_profile) # print to the console the 2 variables

    df['linkedin_profile'][index] = linkedin_profile # Here we append to the new rows created earlier,with the results that we had got from google
    df['linkedin_name'][index] = linkedin_name # Here we append to the new rows created earlier,with the results that we had got from google

    # We are breaking google TOS, so we will sleep between 14 and 25 seconds after every search to not get the IP banned by google
    time.sleep(randint(1, 3))

df.to_csv("30_under_30_europe_2018_linkedin_info.csv", mode='a', header=False)  # export to csv

print ("finish")
