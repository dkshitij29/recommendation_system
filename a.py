from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load your dataframes
merged_df = pd.read_csv('src/merged_amazon_data.csv')

# Define categories and their corresponding lists (same as before)
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
                                 'Smart Home: Plugs and Outlets', 'Smart Home: Vacuums and Mops', 'Sony PSP Games', 'Consoles & Accessories',
                                 'Boys Accessories', 'Beauty Tools & Accessories', 'Cell Phones & Accessories', 'Child Safety Car Seats & Accessories',
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

# Create a DataFrame for each category
category_dfs = {category: merged_df[merged_df['category_name'].isin(items)] for category, items in categories.items()}

# Function to find recommended items
def test_data_finder(items):
    category_name = items["category_name"]
    if category_name is None or category_name == "":
        return []
    else:
        for category, df in category_dfs.items():
            if category_name in categories[category]:
                return recommendor_logic(df, items)
        else:
            return recommendor_logic(category_dfs["Others"], items)

# Function for recommending items
def recommendor_logic(df, items):
    price = items["price"]
    price_range = 5

    filtered_df = df[(df['category_name'] != items["category_name"]) &
                     (df['price'] >= price - price_range) &
                     (df['price'] <= price + price_range)].reset_index(drop=True)

    selected_items = filtered_df.sample(n=4, random_state=42)  # Change 'n' for more products
    return selected_items.to_dict(orient='records')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from form
        title = request.form.get('title')
        stars = float(request.form.get('stars', 0))
        reviews = int(request.form.get('reviews', 0))
        price = float(request.form.get('price', 0))
        seller = request.form.get('seller') == 'on'
        bought_in_last_month = int(request.form.get('bought_in_last_month', 0))
        category_name = request.form.get('category_name')

        # Create a dictionary of user input
        items = {
            "title": title,
            "stars": stars,
            "reviews": reviews,
            "price": price,
            "Seller": seller,
            "boughtInLastMonth": bought_in_last_month,
            "category_name": category_name
        }
        
        recommendations = test_data_finder(items)
        return render_template('index.html', recommendations=recommendations)

    # GET request, display form
    return render_template('index.html', recommendations=[])

if __name__ == '__main__':
    app.run(debug=True)
