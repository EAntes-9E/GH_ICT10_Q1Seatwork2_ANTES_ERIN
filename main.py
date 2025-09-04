from pyscript import display


Resto_name = 'AsKo' #String
Owner_name = 'Rin Gayle Antes' #String
Year_established = '2024' #Integer
Popular_item_price = '575' #Float
Has_delivery = False #Boolean
Product_names = 'Caeser Salad, Tomato Soup,  Truffle Cream Pasta, Steak Frites, Knafeh Ice Cream  ' #List
Business_hours = '11:00 AM - 10:00 PM' #String
Menu_prices = '250', '270', '300', '575', '400' #List
Common_allergens = ['Gluten', 'Dairy', 'Nuts'] #List
Tax_rates = 0.07 #Float


display(Resto_name, target='dive')
display(f'Owner: {Owner_name} | Since {Year_established}', target='dive2')
display(f'Business Hours: {Business_hours}', target='dive3')




