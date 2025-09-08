from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    if preference:
        customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

print(customer_preferences)

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"]) 
    })

print(converted_products)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    count = 0
    for tag in product_tags:
        if tag in customer_tags:
            count += 1
    return count

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        recommendations.append({
            "name": product["name"],
            "matches": matches
        })
    
    
    recommendations.sort(key=lambda x: x["matches"], reverse=True)
    return recommendations

# TODO: Step 7 - Call your function and print the results
final_recommendations = recommend_products(converted_products, customer_tags)

print("\nRecommended Products:")
for recommendation in final_recommendations:
    print(f"- {recommendation['name']} ({recommendation['matches']} match(es))")

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why? 
# In this program, I used for loops, intersections, appending, sorting, and if statements. 
# The loops were required to loop through information and apply changes to all information (like converting tags to sets) and looping and counting matching tags
# intersections, appending, and sorting were needed to manipulate my lists and sets to hold, display, and compare the correct information. 
# 2. How might this code change if you had 1,000+ products?
# If there were 1000+ products in this system, I believe all of the looping logic would still function. However, I would recommend having a searchable 
# list instead of looking through the complete products list at the beginning. 
# I would also recommend storing recent searches so that the user does not have to restate previous preferences.  
