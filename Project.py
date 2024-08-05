#!/usr/bin/env python
# coding: utf-8

# # Data Importing into notebook

# In[ ]:


# amazon categories = csv
#get_ipython().system("wget -q 'https://drive.google.com/uc?export=download&id=1J4sdOZdtqWJgfVQXpbRGfgCyGpXkIUtv' -O 'src/amazon_categories.csv'")


# In[5]:


import pandas as pd

# List of chunk file names
chunk_files = [
    'chunk_1.csv', 'chunk_2.csv', 'chunk_3.csv', 'chunk_4.csv', 'chunk_5.csv',
    'chunk_6.csv', 'chunk_7.csv', 'chunk_8.csv', 'chunk_9.csv', 'chunk_10.csv',
    'chunk_11.csv', 'chunk_12.csv', 'chunk_13.csv', 'chunk_14.csv', 'chunk_15.csv'
]

# Add 'src/' prefix to each file name
chunk_files = [f'src/{file}' for file in chunk_files]

# Read each chunk and concatenate them into one DataFrame
chunks = []
for file in chunk_files:
    chunk = pd.read_csv(file)
    chunks.append(chunk)

# Concatenate all chunks
combined_data = pd.concat(chunks, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_data.to_csv('src/amazon_products.csv', index=False)

# Read the other CSV files from the src directory
df1 = pd.read_csv('src/amazon_categories.csv')
df2 = pd.read_csv('src/amazon_products.csv')

# Merge the two DataFrames based on the category_id and id columns
merged_df = pd.merge(df2, df1, left_on='category_id', right_on='id')

# If you want to save the merged DataFrame to a CSV file
merged_df.to_csv('src/merged_amazon_data.csv', index=False)


# In[ ]:


merged_df.head()


# # Data cleaning action

# In[ ]:


merged_df.drop('imgUrl', inplace=True, axis=1) # Image URL not requried
merged_df.drop('productURL' , inplace = True, axis =1)
merged_df.drop('id', inplace=True, axis=1) # as the category id and id are same
merged_df.drop('asin', inplace=True, axis=1) # not requried for our design case
merged_df = merged_df[merged_df['price'] != 0.0] # removing price == 0 (selling price can't be 0) so thought of removing the dataset
#merged_df = merged_df.sort_values(by='isBestSeller', ascending=False) # just selecting is best seller


# # Visualization:
# 

# In[ ]:


import matplotlib.pyplot as plt

threshold = 0.5  # setting a threshold value

# Group the data by category_id and count occurrences
category_counts = merged_df['category_id'].value_counts()

# Calculate percentage of entries for each category
category_percentages = category_counts / category_counts.sum() * 100

# Filter categories based on the threshold
significant_categories = category_percentages[category_percentages >= threshold]
other_category_count = category_percentages[category_percentages < threshold].sum()
significant_categories['Others'] = other_category_count

# Plotting the pie chart
plt.figure(figsize=(10, 10))  # Define the figure size
#plt.pie(significant_categories, labels=significant_categories.index, autopct='%1.1f%%', startangle=140) if you want to show the percentages
plt.pie(significant_categories, labels=significant_categories.index, startangle=140)

plt.title('Distribution of Category IDs with threshold as 0.5 %')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[ ]:


threshold = 0.5  # setting a threshold value

# Group the data by category_id and count occurrences
category_counts = merged_df['category_id'].value_counts()

# Calculate percentage of entries for each category
category_percentages = category_counts / category_counts.sum() * 100

# Filter categories based on the threshold
significant_categories = category_percentages[category_percentages >= threshold]
other_category_count = category_percentages[category_percentages < threshold].sum()
significant_categories['Others'] = other_category_count

# Plotting the pie chart
plt.figure(figsize=(10, 10))  # Define the figure size
#plt.pie(significant_categories, labels=significant_categories.index, autopct='%1.1f%%', startangle=140) if you want to show the percentages
plt.pie(significant_categories, labels=significant_categories.index, startangle=140)

plt.title('Distribution of Category IDs with threshold as 0.5 %')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[ ]:


category_counts = merged_df['category_id'].value_counts()
plt.title('Distribution of Category IDs with frequency counts on the y-axis and the category IDs on the x-axis')
plt.xlabel('category IDs')
plt.ylabel('frequency counts')
plt.hist(category_counts)
plt.show()


# In[ ]:


is_bestseller_counts = merged_df['isBestSeller'].value_counts()
plt.bar(is_bestseller_counts.index.astype(str), is_bestseller_counts)
plt.xlabel('isBestSeller')
plt.ylabel('Count')
plt.title('Distribution of isBestSeller')
plt.show()


# In[ ]:


# Filter the DataFrame to include only rows where 'isBestSeller' is True
bestseller_df = merged_df[merged_df['isBestSeller'] == True]

# Count the occurrences of each unique value in the 'category_id' column of the filtered DataFrame
bestseller_counts = bestseller_df['category_id'].value_counts()

# Plotting the bar graph
plt.bar(bestseller_counts.index, bestseller_counts)
plt.xlabel('Category ID')
plt.ylabel('Count')
plt.title('Distribution of isBestSeller with True Value')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if needed
plt.show()


# # Recommendation system:

# In[ ]:


import pandas as pd

# Define categories and their corresponding lists
categories = {
    "Electronics_and_Gadgets": ['Xbox 360 Games', 'Consoles & Accessories', "Men's Accessories", 'Televisions & Video Products',
                                 'PlayStation Vita Games', 'Consoles & Accessories', 'Wii U Games', 'Consoles & Accessories',
                                 'PlayStation 4 Games, Consoles & Accessories', 'Smart Home: Security Cameras and Systems',
                                 'Office Electronics', 'Slot Cars', 'Race Tracks & Accessories', 'Video Games',
                                 'Smart Home: Voice Assistants and Hubs', 'Toys & Games', 'Automotive Exterior Accessories',
                                 'Smart Home: Lawn and Garden', 'Tablet Replacement Parts', "Kids' Electronics",
                                 'Nintendo Switch Consoles', 'Games & Accessories', 'Accessories & Supplies', 'Electrical Equipment',
                                 'Dolls & Accessories', 'RV Parts & Accessories', 'Electronic Components', 'Mac Games & Accessories',
                                 'Computers & Tablets', 'Smart Home: Smart Locks and Entry', 'Smart Home: WiFi and Networking',
                                 'Smart Home: Lighting', 'Portable Audio & Video', 'PC Games & Accessories', 'Vehicle Electronics',
                                 'Games & Accessories', 'Virtual Reality Hardware & Accessories', 'Video Projectors', 'Camera & Photo',
                                 'eBook Readers & Accessories', 'Baby Strollers & Accessories', 'Smart Home: Other Solutions',
                                 'Smart Home - Heating & Cooling', 'Xbox One Games, Consoles & Accessories', 'Laptop Accessories',
                                 'PlayStation 3 Games, Consoles & Accessories', 'Xbox Series X & S Consoles', 'Games & Accessories',
                                 'Smart Home: Home Entertainment', "Women's Accessories", 'GPS & Navigation', 'Video Game Consoles & Accessories',
                                 'Online Video Game Services', 'PlayStation 5 Consoles', 'Games & Accessories', 'Smart Home: Plugs and Outlets',
                                 'Smart Home: Vacuums and Mops', 'Sony PSP Games', 'Consoles & Accessories', 'Boys Accessories',
                                 'Beauty Tools & Accessories', 'Cell Phones & Accessories', 'Child Safety Car Seats & Accessories',
                                 'Computer Networking', 'Home Audio & Theater Products', 'Nintendo DS Games, Consoles & Accessories',
                                 'Wii Games, Consoles & Accessories', 'Smart Home Thermostats - Compatibility Checker',
                                 'Nintendo 3DS & 2DS Consoles', 'Games & Accessories', 'Smart Home: New Smart Devices',
                                 'Automotive Performance Parts & Accessories', 'Tablet Accessories', 'Girls Accessories',
                                 'Automotive Interior Accessories', 'Travel Accessories', 'Car Electronics & Accessories'],

    "Crafts_and_Hobbies": ["Fabric Decorating", "Wall Art", "Needlework Supplies", "Sewing Products"],

    "Home_and_Lifestyle": ["Vacuum Cleaners & Floor Care", "Kids' Furniture", "Luggage", "Home Décor Products", "Furniture",
                            "Travel Duffel Bags", "Bath Products", "Security & Surveillance Equipment", "Bedding",
                            "Lighting & Ceiling Fans", "Home Appliances", "Arts, Crafts & Sewing Storage",
                            "Home Storage & Organization", "Safety & Security", "Data Storage", "Beauty & Personal Care",
                            "Home Use Medical Supplies & Equipment", "Kitchen & Bath Fixtures", "Nursery Furniture",
                            "Bedding & Décor", "Foot, Hand & Nail Care Products", "Kitchen & Dining", "Kids' Home Store",
                            "Home Lighting & Ceiling Fans", "Tools & Home Improvement", "Baby & Child Care Products",
                            "Oral Care Products", "Hair Care Products", "Health Care Products", "Baby Travel Gear",
                            "Luggage Sets", "Travel Tote Bags", "Skin Care Products", "Baby Care Products"],

    "Fashion_and_Accessories": ["Men's Clothing", "Men's Shoes", "Boys' Watches", "Girls' Clothing", "Boys' Clothing",
                                 "Girls' Jewelry", "Women's Handbags", "Beading & Jewelry Making", "Baby Girls' Clothing & Shoes",
                                 "Girls' Watches", "Girls' Shoes", "Baby Boys' Clothing & Shoes", "Men's Watches", "Boys' Jewelry",
                                 "Women's Clothing", "Women's Jewelry", "Women's Watches", "Boys' Shoes", "Women's Shoes"],

    "Automotive_and_Tools": ["Automotive Tires & Wheels", "Automotive Tools & Equipment", "Industrial Power & Hand Tools",
                              "Kids' Play Cars & Race Cars", "Cutting Tools", "Heavy Duty & Commercial Vehicle Equipment",
                              "Painting, Drawing & Art Supplies", "Automotive Enthusiast Merchandise", "Motorcycle & Powersports",
                              "Gift Cards", "Baby Safety Products", "Computer Servers", "Occupational Health & Safety Products",
                              "Retail Store Fixtures & Equipment", "Pumps & Plumbing Equipment", "Power Tools & Hand Tools",
                              "Car Care", "Automotive Paint & Paint Supplies", "Personal Care Products",
                              "Automotive Replacement Parts", "Food Service Equipment & Supplies", "Paint, Wall Treatments & Supplies"],

    "Health_and_Wellness": ["Wellness & Relaxation Products", "Sexual Wellness Products", "Health & Household", "Vision Products",
                             "Sports Nutrition Products", "Diet & Sports Nutrition"],

    "Toys_and_Games": ["Sports & Outdoor Play Toys", "Baby & Toddler Toys", "Kids' Party Supplies", "Party Decorations",
                        "Finger Toys", "Building Toys", "Novelty Toys & Amusements", "Learning & Education Toys", "Party Supplies",
                        "Puzzles", "Stuffed Animals & Plush Toys"],

    "Office_and_Stationery": ["Baby Stationery", "Gift Wrapping Supplies", "Craft & Hobby Fabric", "Arts & Crafts Supplies",
                               "Baby Gifts", "Craft Supplies & Materials", "Scrapbooking & Stamping Supplies",
                               "Stationery & Gift Wrapping Supplies"],

    "Others": ["Suitcases", "Additive Manufacturing Products", "Headphones & Earbuds", "Pregnancy & Maternity Products",
               "Shaving & Hair Removal Products", "Kids' Play Tractors", "Light Bulbs", "Kids' Play Boats", "Computer Monitors",
               "Printmaking Supplies", "Baby & Toddler Feeding Supplies", "Computers", "Wearable Technology", "Reptiles & Amphibian Supplies",
               "Horse Supplies", "Computer External Components", "Perfumes & Fragrances", "Household Cleaning Supplies", "Janitorial & Sanitation Supplies",
               "Kids' Play Buses", "Girls' School Uniforms", "Packaging & Shipping Supplies", "Kids' Dress Up & Pretend Play", "Kids' Play Trains & Trams",
               "Tricycles, Scooters & Wagons", "Science Education Supplies", "Material Handling Products", "Seasonal Décor", "Heating, Cooling & Air Quality",
               "Lab & Scientific Products", "Sports & Fitness", "Building Supplies", "Household Supplies", "Toy Figures & Playsets", "Professional Dental Supplies",
               "Computer Components", "Baby Activity & Entertainment Products", "Lights, Bulbs & Indicators", "Knitting & Crochet Supplies",
               "Commercial Door Products", "Makeup", "Baby", "Boys' School Uniforms", "Outdoor Recreation", "Sports & Outdoors", "Oils & Fluids",
               "Toilet Training Products", "Messenger Bags", "Garment Bags", "Power Transmission Products", "Dog Supplies", "Cat Supplies", "Professional Medical Supplies",
               "Toy Vehicle Playsets", "Abrasive & Finishing Products", "Ironing Products", "Baby Diapering Products", "Legacy Systems",
               "Measuring & Layout", "Kids' Play Trucks", "Laptop Bags", "Backpacks", "Test, Measure & Inspect", "Rain Umbrellas"]
}
category_dfs = {category: merged_df[merged_df['category_name'].isin(items)] for category, items in categories.items()}


# In[ ]:


# Define function to find recommended items
def test_data_finder(items):
    category_name = items["category_name"]
    if category_name is None and category_name != "":
        pass
    else:
        for category, df in category_dfs.items():
            if category_name in categories[category]:
                recommendor_logic(df, items)
                break
        else:
            recommendor_logic(category_dfs["Others"], items)

# Define logic for recommending items
def recommendor_logic(df, items):
    price = items["price"]
    price_range = 5

    filtered_df = df[(df['category_name'] != items["category_name"]) &
                     (df['price'] >= price - price_range) &
                     (df['price'] <= price + price_range)].reset_index(drop=True)

    selected_items = filtered_df.sample(n=4, random_state=42) #change the n for recommending more products

    print(selected_items)

# Example item dictionary
items = {
    "title": "AnapoliZ Cellophane Wrap Roll Gold | 100’ Ft  L...",
    "stars": 4.5,
    "reviews": 0,
    "price": 8.89,
    "listPrice": 12.95,
    "category_id": "12",
    "isBestSeller": True,
    "boughtInLastMonth": 2000,
    "category_name": "Gift Wrapping Supplies"
}

# Call the function to find recommended items
test_data_finder(items)

