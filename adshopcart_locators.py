from faker import Faker
fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
advantage_shop_cart_url= 'https://advantageonlineshopping.com/#/register'
adshop_url = 'https://advantageonlineshopping.com/#/myAccount'
new_username = fake.user_name()
email = fake.email()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name}{last_name}'
phone = fake.phone_number()
country =fake.country()
city = fake.city()
province=fake.postalcode()
address = fake.address().replace("\n", "")
description = fake.sentence(nb_words=100)




