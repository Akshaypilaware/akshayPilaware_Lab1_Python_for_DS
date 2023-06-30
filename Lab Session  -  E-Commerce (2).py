#!/usr/bin/env python
# coding: utf-8

# # Lab Session

# ## <font color='blue'> Table Of Contents </font>
# - Problem Statement 
# - Load required libraries
# - Connect to DB using mysql-connector-python package
# - Create database named `e_commerce`
# - Create tables and insert data into tables as specified in the question
# - Read all the questions and write sql queries to meet the objective 

# ## <font color='blue'> Problem Statement </font>
# ###  An E-commerce website manages its data in the form of various tables.
# You need to create a Database called `e_commerce` and various tables in it. The tables needed and attributes which need to be in every table are given before hand. All you have to do is create tables with data in it and answer some of the questions that follows.

# ### e_commerce Schema:

# ![](e_commerce_schema-1(1).png)

# ### Load Required Libraries

# In[55]:


import mysql.connector
import pandas as pd


# ### Connect to DB using Mysql-connector-python package

# In[56]:


mydb = mysql.connector.connect(host='localhost', user='root', password='9637601260')


# ### You are required to create a database named 'e_commerce'

# In[57]:


cursor = mydb.cursor()
cursor.execute('CREATE DATABASE e_commerce12')
cursor.close()


# In[58]:


mydb = mysql.connector.connect(host='localhost', user='root', password='9637601260', database='e_commerce12')
cursor = mydb.cursor()


# ### Q1. Create tables for supplier, customer, category, product, productDetails, order, rating to store the data for the E-commerce with the schema definition given below.
# 
# 
# - **`supplier`**(SUPP_ID int primary key, SUPP_NAME varchar(50), SUPP_CITY varchar(50), SUPP_PHONE varchar(10))
# 
# 
# - **`customer`** (CUS_ID INT NOT NULL, CUS_NAME VARCHAR(20) NULL DEFAULT NULL, CUS_PHONE VARCHAR(10), CUS_CITY varchar(30) ,CUS_GENDER CHAR,PRIMARY KEY (CUS_ID))
# 
# 
# - **`category`** (CAT_ID INT NOT NULL, CAT_NAME VARCHAR(20) NULL DEFAULT NULL,PRIMARY KEY (CAT_ID))
# 
# 
# - **`product`** (PRO_ID INT NOT NULL, PRO_NAME VARCHAR(20) NULL DEFAULT NULL, PRO_DESC VARCHAR(60) NULL DEFAULT NULL, CAT_ID INT NOT NULL,PRIMARY KEY (PRO_ID),FOREIGN KEY (CAT_ID) REFERENCES CATEGORY (CAT_ID))
# 
# 
# - **`product_details`** (PROD_ID INT NOT NULL, PRO_ID INT NOT NULL, SUPP_ID INT NOT NULL, PROD_PRICE INT NOT NULL,
#   PRIMARY KEY (PROD_ID),FOREIGN KEY (PRO_ID) REFERENCES PRODUCT (PRO_ID), FOREIGN KEY (SUPP_ID) REFERENCES SUPPLIER(SUPP_ID))
#   
#   
# - **`order`** (ORD_ID INT NOT NULL, ORD_AMOUNT INT NOT NULL, ORD_DATE DATE, CUS_ID INT NOT NULL, PROD_ID INT NOT NULL,PRIMARY KEY (ORD_ID),FOREIGN KEY (CUS_ID) REFERENCES CUSTOMER(CUS_ID),FOREIGN KEY (PROD_ID) REFERENCES PRODUCT_DETAILS(PROD_ID))
# 
# 
# - **`rating`** (RAT_ID INT NOT NULL, CUS_ID INT NOT NULL, SUPP_ID INT NOT NULL, RAT_RATSTARS INT NOT NULL,PRIMARY KEY (RAT_ID),FOREIGN KEY (SUPP_ID) REFERENCES SUPPLIER (SUPP_ID),FOREIGN KEY (CUS_ID) REFERENCES CUSTOMER(CUS_ID))

# In[59]:


queries = [
    "CREATE TABLE supplier (SUPP_ID INT PRIMARY KEY, SUPP_NAME VARCHAR(50), SUPP_CITY VARCHAR(50), SUPP_PHONE VARCHAR(12))",
    
    "CREATE TABLE customer (CUS_ID INT NOT NULL, CUS_NAME VARCHAR(20) NULL DEFAULT NULL, CUS_PHONE VARCHAR(10), CUS_CITY VARCHAR(30), CUS_GENDER CHAR, PRIMARY KEY (CUS_ID))",
    
    "CREATE TABLE category (CAT_ID INT NOT NULL, CAT_NAME VARCHAR(20) NULL DEFAULT NULL, PRIMARY KEY (CAT_ID))",
    
    "CREATE TABLE product (PRO_ID INT NOT NULL, PRO_NAME VARCHAR(20) NULL DEFAULT NULL, PRO_DESC VARCHAR(60) NULL DEFAULT NULL, CAT_ID INT NOT NULL, PRIMARY KEY (PRO_ID), FOREIGN KEY (CAT_ID) REFERENCES category (CAT_ID))",
    
    "CREATE TABLE product_details (PROD_ID INT NOT NULL, PRO_ID INT NOT NULL, SUPP_ID INT NOT NULL, PROD_PRICE INT NOT NULL, PRIMARY KEY (PROD_ID), FOREIGN KEY (PRO_ID) REFERENCES product (PRO_ID), FOREIGN KEY (SUPP_ID) REFERENCES supplier(SUPP_ID))",
    
    "CREATE TABLE orders (ORD_ID INT NOT NULL, ORD_AMOUNT INT NOT NULL, ORD_DATE DATE, CUS_ID INT NOT NULL, PROD_ID INT NOT NULL, PRIMARY KEY (ORD_ID), FOREIGN KEY (CUS_ID) REFERENCES customer(CUS_ID), FOREIGN KEY (PROD_ID) REFERENCES product_details(PROD_ID))",
    
    "CREATE TABLE rating (RAT_ID INT NOT NULL, CUS_ID INT NOT NULL, SUPP_ID INT NOT NULL, RAT_RATSTARS INT NOT NULL, PRIMARY KEY (RAT_ID), FOREIGN KEY (SUPP_ID) REFERENCES supplier (SUPP_ID), FOREIGN KEY (CUS_ID) REFERENCES customer(CUS_ID))"
]

for query in queries:
    cursor.execute(query)


# In[60]:


mydb.commit()
cursor.close()


# In[108]:


mydb = mysql.connector.connect(host='localhost', user='root', password='9637601260', database='e_commerce12')
cursor = mydb.cursor()


# ### Q2. Insert the following data in the table created above
# #### `Note:` If you are getting any error while inserting the data into tables, Kindly close the connection and reconnect
# 
# #### Table:  supplier
# | SUPP_ID | SUPP_NAME | SUPP_CITY | SUPP_PHONE |
# | --- | --- | --- | --- | 
# | 1 | Rajesh Retails | Delhi | 1234567890 |
# | 2 | Appario Ltd. | Mumbai | 258963147032 | 
# | 3 | Knome products | Bangalore | 9785462315 |
# | 4 | Bansal Retails | Kochi | 8975463285 |
# | 5 | Mittal Ltd. | Lucknow | 7898456532 |

# In[62]:


insert_queries = [
    "INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE) VALUES (1, 'Rajesh Retails', 'Delhi', '1234567890')",
    "INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE) VALUES (2, 'Appario Ltd.', 'Mumbai', '258963147032')",
    "INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE) VALUES (3, 'Knome products', 'Bangalore', '9785462315')",
    "INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE) VALUES (4, 'Bansal Retails', 'Kochi', '8975463285')",
    "INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE) VALUES (5, 'Mittal Ltd.', 'Lucknow', '7898456532')",
]
for query in insert_queries:
    cursor.execute(query)
    
mydb.commit()


# In[63]:


cursor.close()
mydb.close()


# #### Table:  customer
# | CUS_ID | CUS_NAME | SUPP_PHONE | CUS_CITY | CUS_GENDER
# | --- | --- | --- | --- | --- |
# | 1 | AAKASH | 9999999999 | DELHI | M |
# | 2 | AMAN | 9785463215 | NOIDA | M |
# | 3 | NEHA | 9999999998 | MUMBAI | F |
# | 4 | MEGHA | 9994562399 | KOLKATA | F |
# | 5 | PULKIT | 7895999999 | LUCKNOW | M |

# In[67]:


insert_queries = ["INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER) VALUES (1, 'AAKASH', '9999999999', 'DELHI', 'M')",
    "INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER) VALUES (2, 'AMAN', '9785463215', 'NOIDA', 'M')",
    "INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER) VALUES (3, 'NEHA', '9999999998', 'MUMBAI', 'F')",
    "INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER) VALUES (4, 'MEGHA', '9994562399', 'KOLKATA', 'F')",
    "INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER) VALUES (5, 'PULKIT', '7895999999', 'LUCKNOW', 'M')",
                 ]
for query in insert_queries:
    cursor.execute(query)

mydb.commit()


# In[68]:


cursor.close()
mydb.close()


# #### Table:  category
# | CAT_ID | CAT_NAME | 
# | --- | --- |  
# | 1 | BOOKS |
# | 2 | GAMES |  
# | 3 | GROCERIES | 
# | 4 | ELECTRONICS | 
# | 5 | CLOTHES | 

# In[70]:


insert_queries = [ "INSERT INTO category (CAT_ID, CAT_NAME) VALUES (1, 'BOOKS')",
    "INSERT INTO category (CAT_ID, CAT_NAME) VALUES (2, 'GAMES')",
    "INSERT INTO category (CAT_ID, CAT_NAME) VALUES (3, 'GROCERIES')",
    "INSERT INTO category (CAT_ID, CAT_NAME) VALUES (4, 'ELECTRONICS')",
    "INSERT INTO category (CAT_ID, CAT_NAME) VALUES (5, 'CLOTHES')",]
for query in insert_queries:
    cursor.execute(query)

mydb.commit()
cursor.close()
mydb.close()


# #### Table:  product
# | PRO_ID | PRO_NAME | PRO_DESC | CAT_ID |
# | --- | --- | --- | --- | 
# | 1 | GTA V | DFJDJFDJFDJFDJFJF | 2 |
# | 2 | TSHIRT | DFDFJDFJDKFD | 5 | 
# | 3 | ROG LAPTOP | DFNTTNTNTERND | 4 |
# | 4 | OATS | REURENTBTOTH | 3 |
# | 5 | HARRY POTTER | NBEMCTHTJTH | 1 |
# 

# In[72]:


insert_queries = ["INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID) VALUES (1, 'GTA V', 'DFJDJFDJFDJFDJFJF', 2)",
    "INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID) VALUES (2, 'TSHIRT', 'DFDFJDFJDKFD', 5)",
    "INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID) VALUES (3, 'ROG LAPTOP', 'DFNTTNTNTERND', 4)",
    "INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID) VALUES (4, 'OATS', 'REURENTBTOTH', 3)",
    "INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID) VALUES (5, 'HARRY POTTER', 'NBEMCTHTJTH', 1)",]
for query in insert_queries:
    cursor.execute(query)

mydb.commit()


# In[73]:


cursor.close()
mydb.close()


# #### Table:  product_details
# | PROD_ID | PRO_ID | SUPP_ID | PROD_PRICE |
# | --- | --- | --- | --- | 
# | 1 | 1 | 2 | 1500 |
# | 2 | 3 | 5 | 30000 | 
# | 3 | 5 | 1 | 3000 |
# | 4 | 2 | 3 | 2500 |
# | 5 | 4 | 1 | 1000 |

# In[75]:


insert_queries =[  "INSERT INTO product_details (PROD_ID, PRO_ID, SUPP_ID, PROD_PRICE) VALUES (1, 1, 2, 1500)",
    "INSERT INTO product_details (PROD_ID, PRO_ID, SUPP_ID, PROD_PRICE) VALUES (2, 3, 5, 30000)",
    "INSERT INTO product_details (PROD_ID, PRO_ID, SUPP_ID, PROD_PRICE) VALUES (3, 5, 1, 3000)",
    "INSERT INTO product_details (PROD_ID, PRO_ID, SUPP_ID, PROD_PRICE) VALUES (4, 2, 3, 2500)",
    "INSERT INTO product_details (PROD_ID, PRO_ID, SUPP_ID, PROD_PRICE) VALUES (5, 4, 1, 1000)",
    ]
for query in insert_queries:
    cursor.execute(query)

mydb.commit()


# In[76]:


cursor.close()
mydb.close()


# #### Table:  orders
# | ORD_ID | ORD_AMOUNT | ORD_DATE | CUS_ID | PROD_ID
# | --- | --- | --- | --- | --- |
# | 20 | 1500 | 2021-10-12 | 3 | 5 |
# | 25 | 30500 | 2021-09-16 | 5 | 2 |
# | 26 | 2000 | 2021-10-05 | 1 | 1 |
# | 30 | 3500 | 2021-08-16 | 4 | 3 |
# | 50 | 2000 | 2021-10-06 | 2 | 1 |

# In[78]:


insert_queries =[ "INSERT INTO orders (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID) VALUES (20, 1500, '2021-10-12', 3, 5)",
    "INSERT INTO orders (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID) VALUES (25, 30500, '2021-09-16', 5, 2)",
    "INSERT INTO orders (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID) VALUES (26, 2000, '2021-10-05', 1, 1)",
    "INSERT INTO orders (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID) VALUES (30, 3500, '2021-08-16', 4, 3)",
    "INSERT INTO orders (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID) VALUES (50, 2000, '2021-10-06', 2, 1)",
    ]
for query in insert_queries:
    cursor.execute(query)

mydb.commit()


# In[79]:


cursor.close()
mydb.close()


# #### Table: rating
# | RAT_ID | CUS_ID | SUPP_ID | RAT_RATSTARS |
# | --- | --- | --- | --- | 
# | 1 | 2 | 2 | 4 |
# | 2 | 3 | 4 | 3 | 
# | 3 | 5 | 1 | 5 |
# | 4 | 1 | 3 | 2 |
# | 5 | 4 | 5 | 4 |

# In[81]:


# insert into "rating" table
insert_queries =[ "INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS) VALUES (1, 2, 2, 4)",
    "INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS) VALUES (2, 3, 4, 3)",
    "INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS) VALUES (3, 5, 1, 5)",
    "INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS) VALUES (4, 1, 3, 2)",
    "INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS) VALUES (5, 4, 5, 4)"
]
for query in insert_queries:
    cursor.execute(query)

mydb.commit()
cursor.close()
mydb.close()


# ### Q3) Display the number of the customer group by their genders who have placed any order of amount greater than or equal to Rs.3000.

# In[107]:


query1 = '''
    SELECT CUS_GENDER, COUNT(*) AS TotalCustomers
    FROM customer
    INNER JOIN orders ON customer.CUS_ID = orders.CUS_ID
    WHERE ORD_AMOUNT >= 3000
    GROUP BY CUS_GENDER
'''
cursor.execute(query1)
result = cursor.fetchall()

df = pd.DataFrame(result, columns=['Gender', 'TotalCustomers'])
print(df)
mydb.commit()
cursor.close()


# ### Q4) Display all the order along with product name ordered by a customer having Customer_Id=2;

# In[109]:


query4 = '''
    SELECT orders.ORD_ID, product.PRO_NAME
    FROM orders
    INNER JOIN product_details ON orders.PROD_ID = product_details.PROD_ID
    INNER JOIN product ON product_details.PRO_ID = product.PRO_ID
    WHERE orders.CUS_ID = 2
'''
cursor.execute(query4)
result = cursor.fetchall()
df = pd.DataFrame(result, columns=['Order ID', 'Product Name'])
print(df)


# ### Q5) Display the Supplier details who can supply more than one product.

# In[110]:





# ### Q6) Find the category of the product whose order amount is minimum.

# In[111]:


query = '''
    SELECT product.CAT_ID, MIN(orders.ORD_AMOUNT) AS MinOrderAmount
    FROM product
    INNER JOIN product_details ON product.PRO_ID = product_details.PRO_ID
    INNER JOIN orders ON product_details.PROD_ID = orders.PROD_ID
    GROUP BY product.CAT_ID
'''
cursor.execute(query)
result = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Category ID', 'Min Order Amount'])
print(df)


# ### Q7) Display the Id and Name of the Product ordered after “2021-10-05”.

# In[112]:


query = '''
    SELECT product.PRO_ID, product.PRO_NAME
    FROM product
    INNER JOIN product_details ON product.PRO_ID = product_details.PRO_ID
    INNER JOIN orders ON product_details.PROD_ID = orders.PROD_ID
    WHERE orders.ORD_DATE > '2021-10-05'
'''
cursor.execute(query)
result = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Product ID', 'Product Name'])
print(df)


# ### Q8) Print the top 3 supplier name and id and rating on the basis of their rating along with the customer name who has given the rating.

# In[113]:


query = '''
    SELECT rating.RAT_ID, supplier.SUPP_ID, supplier.SUPP_NAME, rating.RAT_RATSTARS, customer.CUS_NAME
    FROM rating
    INNER JOIN supplier ON rating.SUPP_ID = supplier.SUPP_ID
    INNER JOIN customer ON rating.CUS_ID = customer.CUS_ID
    ORDER BY rating.RAT_RATSTARS DESC
    LIMIT 3
'''
cursor.execute(query)
result = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Rating ID', 'Supplier ID', 'Supplier Name', 'Rating', 'Customer Name'])
print(df)


# ### Q9) Display customer name and gender whose names start or end with character 'A'.

# In[114]:


query = '''
    SELECT CUS_NAME, CUS_GENDER
    FROM customer
    WHERE CUS_NAME LIKE 'A%' OR CUS_NAME LIKE '%A'
'''
cursor.execute(query)
result = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Customer Name', 'Gender'])
print(df)


# ### Q10) Display the total order amount of the male customers.

# In[115]:


query = '''
    SELECT SUM(ORD_AMOUNT) AS TotalOrderAmount
    FROM orders
    INNER JOIN customer ON orders.CUS_ID = customer.CUS_ID
    WHERE customer.CUS_GENDER = 'M'
'''
cursor.execute(query)
result = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Total Order Amount'])
print(df)


# ### Q11) Display all the Customers left outer join with  the orders

# In[117]:


query = '''
    SELECT customer.*, orders.*
    FROM customer
    LEFT JOIN orders ON customer.CUS_ID = orders.CUS_ID
'''
cursor.execute(query)
result = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['Customer ID', 'Customer Name', 'Customer Phone', 'Customer City', 'Customer Gender', 'Order ID', 'Order Amount', 'Order Date','CUS_ID', 'Product ID'])
print(df)


# **NOTE:** Always close an open connection once you are done with the database operations

# ## Happy Learning:)
