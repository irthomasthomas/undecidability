**Prompt:**
Using the following instruction manual to write a bash script with helpful comments. The script should use the amazonscraper  to query amazon.co.uk for all nvme drives. Script should check that the tools are installed and either intall them or instruct user.--Features
Extract product data from the search result(by category, by country)
Extract lots of single product data by using ASIN id
Extract product reviews data by using ASIN id
Extract list of categories
Is supporting all available Amazon Marketplaces
Sort result by sponsored products only
Sorts result by discounted products only
Result can be saved to the JSON/CSV files
You can scrape up to 500 products and 1000 reviews
Product List alt text Review List alt text

Note:

Empty parameter = empty value
Possible errors

If there will be let me know
Installation
Install from NPM

$ npm i -g amazon-buddy
Install from YARN

$ yarn global add amazon-buddy
USAGE
Terminal

$ amazon-buddy --help

Usage: amazon-buddy <command> [options]

Commands:
  amazon-buddy products      collect products by using keyword
  amazon-buddy reviews [id]  collect reviews from product by using ASIN id
  amazon-buddy asin [id]     single product details
  amazon-buddy categories    get list of categories
  amazon-buddy countries     get list of countries

Options:
  --help, -h      help                                                 [boolean]
  --version       Show version number                                  [boolean]
  --async, -a     Number of async tasks                  [string] [default: "5"]
  --keyword, -k   Amazon search keyword ex. 'Xbox one'    [string] [default: ""]
  --number, -n    Number of products to scrape. Maximum 100 products or 300
                  reviews                                 [number] [default: 20]
  --filetype      Type of the output file where the data will be saved. 'all' -
                  save data to the 'json' and 'csv' files
                            [choices: "csv", "json", "all", ""] [default: "csv"]
  --sort          If searching for the products then the list will be sorted by
                  the higher score(number of reviews*rating). If searching for
                  the reviews then they will be sorted by the rating.
                                                      [boolean] [default: false]
  --discount, -d  Scrape only products with the discount
                                                      [boolean] [default: false]
  --sponsored     Scrape only sponsored products      [boolean] [default: false]
  --min-rating    Minimum allowed rating                   [number] [default: 1]
  --max-rating    Maximum allowed rating                   [number] [default: 5]
  --country       In ISO 3166 (Alpha-2 code) format. To get available list of
                  countries type and use (index) from the shown table as value:
                  amazon-buddy countries                [string] [default: "US"]
  --category      To get available list of categories type and use (index) from
                  the shown table as value: amazon-buddy categories
                                                       [string] [default: "aps"]
  --random-ua     Randomize user agent version. This helps to prevent request
                  blocking from the amazon side       [boolean] [default: false]
  --user-agent    Set custom user-agent                   [string] [default: ""]
  --timeout, -t   Timeout between requests. Timeout is set in mls: 1000 mls = 1


Examples:
  amazon-buddy products -k 'Xbox one'
  amazon-buddy products -k 'Xbox one' --country 'GB'
  amazon-buddy reviews B01GW3H3U8
  amazon-buddy asin B01GW3H3U8
  amazon-buddy categories
  amazon-buddy countries
Example 1
Scrape 40 products from the amazon search result by using keyword "vacuum cleaner" and save result to the CSV file

$ amazon-buddy products -k 'vacuum cleaner' -n 40 --filetype csv
Output: 1552945544582_products.csv

Example 2
Scrape 40 products from the amazon search result by using keyword "vacuum cleaner" and display raw result in the terminal

$ amazon-buddy products -k 'vacuum cleaner' -n 40 --filetype ''
Example 3
Scrape 40 products from the amazon search result by using keyword "vacuum cleaner" from the Amazon.NL(Netherlands) and display raw result in the terminal

$ amazon-buddy products -k 'vacuum cleaner' -n 40 --filetype '' --country NL
Example 4
Scrape 40 products from the amazon search result from the category "Apps & Games" by using keyword "games" from the Amazon.ES(SPAIN) and display raw result in the terminal

$ amazon-buddy products -k 'games' -n 40 --filetype '' --country ES --category mobile-apps
Example 5
Scrape 100 reviews from a product by using ASIN. NOTE: ASIN is a unique amazon product ID, it can be found in product URL or if you have scraped product list with our tool you will find it in the CSV/JSON files

$ amazon-buddy reviews B01GW3H3U8 -n 100
Output: reviews(B01GW3H3U8)_1589470878252

Example 6
Scrape 300 products from the "Xbox one" keyword with rating minimum rating 3 and maximum rating 4 and save everything to the CSV file

$ amazon-buddy products -k 'xbox one' -n 300 --min-rating 3 --max-rating 4
Output: 1552945544582_products.csv

Example 7
Show list of all available countries

$ amazon-buddy countries
Output: alt text

Example 7
Show list of all available categories from the Amazon.CO.UK

$ amazon-buddy categories --country GB
Output: alt text

Module
Methods
.products() - product search
.reviews() - reviews search
.asin() - single product details
.categories() - available categories
Example
const amazonScraper = require('amazon-buddy');

(async () => {
    try {
        // Collect 50 products from a keyword 'xbox one'
        // Default country is US
        const products = await amazonScraper.products({ keyword: 'Xbox One', number: 50 });

        // Collect 50 products from a keyword 'xbox one' from Amazon.NL
        const products = await amazonScraper.products({ keyword: 'Xbox One', number: 50, country: 'NL' });

        // Collect 50 products from a keyword 'xbox one' from Amazon.CO.UK
        const products = await amazonScraper.products({ keyword: 'Xbox One', number: 50, country: 'GB' });

        // Collect products that are located on page number 2
        const reviews = await amazonScraper.products({ keyword: 'Xbox One', bulk: false, page: 2 });

        // Collect 50 products from a keyword 'xbox one' with rating between 3-5 stars
        const products_rank = await amazonScraper.products({ keyword: 'Xbox One', number: 50, rating: [3, 5] });

        // Collect 50 reviews from a product ID B01GW3H3U8
        const reviews = await amazonScraper.reviews({ asin: 'B01GW3H3U8', number: 50 });

        // Collect 50 reviews from a product ID B01GW3H3U8  with rating between 1-2 stars
        const reviews_rank = await amazonScraper.reviews({ asin: 'B01GW3H3U8', number: 50, rating: [1, 2] });

        // Get single product details by using ASIN id
        const product_by_asin = await amazonScraper.asin({ asin: 'B01GW3H3U8' });

        // Get categories from amazon.COM.AU
        const categories_AU = await amazonScraper.categories({ country: 'AU' });

        // Get categories from amazon.CN
        const categories_CN = await amazonScraper.categories({ country: 'CN' });
    } catch (error) {
        console.log(error);
    }
})();

**Response:**
#!/bin/bash

# Check if amazon-buddy is installed
if ! command -v amazon-buddy &> /dev/null
then
    echo "amazon-buddy is not installed"
    echo "Please install it using one of the following methods:"
    echo "- npm i -g amazon-buddy"
    echo "- yarn global add amazon-buddy"
    exit
fi

# Use amazonscraper to query amazon.co.uk for all nvme drives
amazon-buddy products -k "nvme" --country "GB" --filetype "json" --sort --discount --sponsored --number 500

# Check if there are any errors during the execution of the command
if [ $? -ne 0 ]; then
    echo "There was an error while executing the command"
fi

<details><summary>Metadata</summary>

- Duration: 8414 ms
- Datetime: 2023-08-23T12:59:37.294662
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

