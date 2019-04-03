# Purchase-Analytics

## Approach to the Problem

I used a dictionary whose entries consisted of the `Product IDs`, and the associated values contained the number of times that
product has been ordered and the number of time the product has been ordered for the first time. I gather this information by parsing `order_products.csv`.
I then iterate over `products.csv` to get the `Department IDs` to which these products belong and store it in the dictionary. Finally, I group this data by department by going through the dictionary, and calculate the `percentage`.
This result is then saved in `report.csv`.


## Trade-Offs

I decided to use a dictionary for the following reasons :-

* Accessing items in a dictionary takes constant (O(1)) time. Since we needed to iterate over all the rows of the CSVs to gather the counts,
a dictionary would be the most efficient way to access a product as it came.
* It is also easy to sort the dictionary based on its key values, which in this case would be according to the `Department IDs`


## Pre-Requisites

* Python 3


## Tests

* test_1 : Default Test
* test_2 : Decimal Values as instead of Integers
* test_3 : Values enclosed in inverted commas. Eg: "15"
* test_4 : Missing values

Passed all test cases