Dataset Overview

This dataset contains information on beauty and fragrance products, including product
names, brands, customer engagement metrics such as loves count, ratings, and the number
of reviews.



```python
import pandas as pd

df = pd.read_csv("data/product_info.csv")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>product_id</th>
      <th>product_name</th>
      <th>brand_id</th>
      <th>brand_name</th>
      <th>loves_count</th>
      <th>rating</th>
      <th>reviews</th>
      <th>size</th>
      <th>variation_type</th>
      <th>variation_value</th>
      <th>...</th>
      <th>online_only</th>
      <th>out_of_stock</th>
      <th>sephora_exclusive</th>
      <th>highlights</th>
      <th>primary_category</th>
      <th>secondary_category</th>
      <th>tertiary_category</th>
      <th>child_count</th>
      <th>child_max_price</th>
      <th>child_min_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>P473671</td>
      <td>Fragrance Discovery Set</td>
      <td>6342</td>
      <td>19-69</td>
      <td>6320</td>
      <td>3.6364</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>['Unisex/ Genderless Scent', 'Warm &amp;Spicy Scen...</td>
      <td>Fragrance</td>
      <td>Value &amp; Gift Sets</td>
      <td>Perfume Gift Sets</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>P473668</td>
      <td>La Habana Eau de Parfum</td>
      <td>6342</td>
      <td>19-69</td>
      <td>3827</td>
      <td>4.1538</td>
      <td>13.0</td>
      <td>3.4 oz/ 100 mL</td>
      <td>Size + Concentration + Formulation</td>
      <td>3.4 oz/ 100 mL</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>['Unisex/ Genderless Scent', 'Layerable Scent'...</td>
      <td>Fragrance</td>
      <td>Women</td>
      <td>Perfume</td>
      <td>2</td>
      <td>85.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>P473662</td>
      <td>Rainbow Bar Eau de Parfum</td>
      <td>6342</td>
      <td>19-69</td>
      <td>3253</td>
      <td>4.2500</td>
      <td>16.0</td>
      <td>3.4 oz/ 100 mL</td>
      <td>Size + Concentration + Formulation</td>
      <td>3.4 oz/ 100 mL</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>['Unisex/ Genderless Scent', 'Layerable Scent'...</td>
      <td>Fragrance</td>
      <td>Women</td>
      <td>Perfume</td>
      <td>2</td>
      <td>75.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>P473660</td>
      <td>Kasbah Eau de Parfum</td>
      <td>6342</td>
      <td>19-69</td>
      <td>3018</td>
      <td>4.4762</td>
      <td>21.0</td>
      <td>3.4 oz/ 100 mL</td>
      <td>Size + Concentration + Formulation</td>
      <td>3.4 oz/ 100 mL</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>['Unisex/ Genderless Scent', 'Layerable Scent'...</td>
      <td>Fragrance</td>
      <td>Women</td>
      <td>Perfume</td>
      <td>2</td>
      <td>75.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>P473658</td>
      <td>Purple Haze Eau de Parfum</td>
      <td>6342</td>
      <td>19-69</td>
      <td>2691</td>
      <td>3.2308</td>
      <td>13.0</td>
      <td>3.4 oz/ 100 mL</td>
      <td>Size + Concentration + Formulation</td>
      <td>3.4 oz/ 100 mL</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>['Unisex/ Genderless Scent', 'Layerable Scent'...</td>
      <td>Fragrance</td>
      <td>Women</td>
      <td>Perfume</td>
      <td>2</td>
      <td>75.0</td>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>




```python
df.shape, df.columns
```




    ((8494, 27),
     Index(['product_id', 'product_name', 'brand_id', 'brand_name', 'loves_count',
            'rating', 'reviews', 'size', 'variation_type', 'variation_value',
            'variation_desc', 'ingredients', 'price_usd', 'value_price_usd',
            'sale_price_usd', 'limited_edition', 'new', 'online_only',
            'out_of_stock', 'sephora_exclusive', 'highlights', 'primary_category',
            'secondary_category', 'tertiary_category', 'child_count',
            'child_max_price', 'child_min_price'],
           dtype='object'))




```python
df.info()
df.describe()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8494 entries, 0 to 8493
    Data columns (total 27 columns):
     #   Column              Non-Null Count  Dtype  
    ---  ------              --------------  -----  
     0   product_id          8494 non-null   object 
     1   product_name        8494 non-null   object 
     2   brand_id            8494 non-null   int64  
     3   brand_name          8494 non-null   object 
     4   loves_count         8494 non-null   int64  
     5   rating              8216 non-null   float64
     6   reviews             8216 non-null   float64
     7   size                6863 non-null   object 
     8   variation_type      7050 non-null   object 
     9   variation_value     6896 non-null   object 
     10  variation_desc      1250 non-null   object 
     11  ingredients         7549 non-null   object 
     12  price_usd           8494 non-null   float64
     13  value_price_usd     451 non-null    float64
     14  sale_price_usd      270 non-null    float64
     15  limited_edition     8494 non-null   int64  
     16  new                 8494 non-null   int64  
     17  online_only         8494 non-null   int64  
     18  out_of_stock        8494 non-null   int64  
     19  sephora_exclusive   8494 non-null   int64  
     20  highlights          6287 non-null   object 
     21  primary_category    8494 non-null   object 
     22  secondary_category  8486 non-null   object 
     23  tertiary_category   7504 non-null   object 
     24  child_count         8494 non-null   int64  
     25  child_max_price     2754 non-null   float64
     26  child_min_price     2754 non-null   float64
    dtypes: float64(7), int64(8), object(12)
    memory usage: 1.7+ MB
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_id</th>
      <th>loves_count</th>
      <th>rating</th>
      <th>reviews</th>
      <th>price_usd</th>
      <th>value_price_usd</th>
      <th>sale_price_usd</th>
      <th>limited_edition</th>
      <th>new</th>
      <th>online_only</th>
      <th>out_of_stock</th>
      <th>sephora_exclusive</th>
      <th>child_count</th>
      <th>child_max_price</th>
      <th>child_min_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8494.000000</td>
      <td>8.494000e+03</td>
      <td>8216.000000</td>
      <td>8216.000000</td>
      <td>8494.000000</td>
      <td>451.000000</td>
      <td>270.000000</td>
      <td>8494.000000</td>
      <td>8494.000000</td>
      <td>8494.000000</td>
      <td>8494.000000</td>
      <td>8494.000000</td>
      <td>8494.000000</td>
      <td>2754.000000</td>
      <td>2754.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5422.440546</td>
      <td>2.917957e+04</td>
      <td>4.194513</td>
      <td>448.545521</td>
      <td>51.655595</td>
      <td>91.168537</td>
      <td>20.207889</td>
      <td>0.070285</td>
      <td>0.071698</td>
      <td>0.219096</td>
      <td>0.073699</td>
      <td>0.279374</td>
      <td>1.631622</td>
      <td>53.792023</td>
      <td>39.665802</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1709.595957</td>
      <td>6.609212e+04</td>
      <td>0.516694</td>
      <td>1101.982529</td>
      <td>53.669234</td>
      <td>79.195631</td>
      <td>24.327352</td>
      <td>0.255642</td>
      <td>0.258002</td>
      <td>0.413658</td>
      <td>0.261296</td>
      <td>0.448718</td>
      <td>5.379470</td>
      <td>58.765894</td>
      <td>38.685720</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1063.000000</td>
      <td>0.000000e+00</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>1.750000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5333.000000</td>
      <td>3.758000e+03</td>
      <td>3.981725</td>
      <td>26.000000</td>
      <td>25.000000</td>
      <td>45.000000</td>
      <td>8.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>22.000000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6157.500000</td>
      <td>9.880000e+03</td>
      <td>4.289350</td>
      <td>122.000000</td>
      <td>35.000000</td>
      <td>67.000000</td>
      <td>14.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>32.000000</td>
      <td>28.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6328.000000</td>
      <td>2.684125e+04</td>
      <td>4.530525</td>
      <td>418.000000</td>
      <td>58.000000</td>
      <td>108.500000</td>
      <td>25.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>59.000000</td>
      <td>42.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>8020.000000</td>
      <td>1.401068e+06</td>
      <td>5.000000</td>
      <td>21281.000000</td>
      <td>1900.000000</td>
      <td>617.000000</td>
      <td>320.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>105.000000</td>
      <td>570.000000</td>
      <td>400.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isna().sum().sort_values(ascending=False)
```




    sale_price_usd        8224
    value_price_usd       8043
    variation_desc        7244
    child_max_price       5740
    child_min_price       5740
    highlights            2207
    size                  1631
    variation_value       1598
    variation_type        1444
    tertiary_category      990
    ingredients            945
    rating                 278
    reviews                278
    secondary_category       8
    sephora_exclusive        0
    brand_id                 0
    child_count              0
    primary_category         0
    new                      0
    out_of_stock             0
    online_only              0
    limited_edition          0
    brand_name               0
    product_name             0
    price_usd                0
    loves_count              0
    product_id               0
    dtype: int64



What the data looks like
- Each row is one product/variation.
- Columns include product + brand details and customer engagement metrics (loves, rating, reviews).
- Some fields (like size/variation details) are missing for certain rows, which probably means
  those products don’t have that info available or don’t have variations listed.



```python
df["brand_name"].value_counts().head(10)
```




    brand_name
    SEPHORA COLLECTION         352
    CLINIQUE                   179
    Dior                       136
    tarte                      131
    NEST New York              115
    Bumble and bumble          110
    Kérastase                  108
    TOM FORD                   100
    Charlotte Tilbury           99
    Anastasia Beverly Hills     95
    Name: count, dtype: int64




```python
df["rating"].mean()
```




    np.float64(4.194512889483933)



Summary Observation
summary statistics:
- The majority of product ratings are above average and products are positively rated.
- Some brands are represented more than others, meaning they have more products in the dataset.
- The number of reviews and loves varies wildly, suggesting that some products are far more popular than others on the platform.


```python
df["rating"].plot(kind="hist", title="Distribution of Product Ratings")
```




    <Axes: title={'center': 'Distribution of Product Ratings'}, ylabel='Frequency'>




    
![png](output_9_1.png)
    



```python
df["brand_name"].value_counts().head(10).plot(
    kind="bar",
    title="Top 10 Brands by Number of Products"
)
```




    <Axes: title={'center': 'Top 10 Brands by Number of Products'}, xlabel='brand_name'>




    
![png](output_10_1.png)
    



```python
df.groupby("brand_name")["rating"].mean().sort_values(ascending=False).head(10).plot(
    kind="bar",
    title="Top 10 Brands by Average Rating"
)
```




    <Axes: title={'center': 'Top 10 Brands by Average Rating'}, xlabel='brand_name'>




    
![png](output_11_1.png)
    


Graph Overview

graph 1 shows the distribution of product ratings across the dataset. Most products are rated between 4.0 and 5.0, indicating that customer feedback is generally positive. Very few products have low ratings, showing that poorly rated products are less common.

graph 2 this bar chart shows the top 10 brands based on the number of products
they have in the dataset. A small number of brands account for a large portion of the products,
which suggests that the retailer carries more items from certain popular brands.

graph 3 this chart displays the top 10 brands ranked by their average product rating. Brands with higher average ratings tend to have more consistently well reviewed products. This shows that customer satisfaction may vary by brand, not just by individual product.




Insights

Overall, the dataset shows strong customer engagement with beauty products. Most products receive positive ratings, and certain brands stand out in terms of both product count and customer satisfaction. This helps find which brands and products perform well and could be useful for decisions related to marketing or product focus.

