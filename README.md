## Topic Modelling
If you have hundreds of documents from an archive and you wish to understand something of what the archive contains without necessarily reading every document, then topic modelling might be a good approach.

### Use case
We want to find the problems customers are facing from their customer feedback that we get at the website, or say find problems with a product from customer reviews


### Reference Material
[WIKI](https://en.wikipedia.org/wiki/Topic_model)
[101](https://www.kdnuggets.com/2016/07/text-mining-101-topic-modeling.html)
[Griffiths Book](http://psiexp.ss.uci.edu/research/papers/SteyversGriffithsLSABookFormatted.pdf)
[Mallet](https://programminghistorian.org/lessons/topic-modeling-and-mallet)

[Generative models](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/blob/master/GenerativeModels.pdf)

### Scrape the Comments - Scrapy

To scrape the walmart related comments on [consumeraffairs](https://www.consumeraffairs.com/retail/walmart.htm) wrote a small [scrapy spider](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/blob/master/walmart/comments/comments/spiders/comments.py) to fetch the comments and form a corpus of documents to be labbelled by a topic modelling tool like Mallet.
Please refer [scrapy website](https://scrapy.org/)
```bash
sudo pip install virtualenv
source bin/activate

 /Users/sur000e/workspace-mallet/walmart/brickset-scraper
virtualenv .
./bin/pip install scrapy


scrapy startproject tutorial
scrapy genspider example example.com
/Users/sur000e/workspace-mallet/walmart/brickset-scraper/tutorial
scrapy crawl quotes
/Users/sur000e/workspace-mallet/walmart/brickset-scraper/tutorial/tutorial/spiders
```
This may be blocked by the website as a trolling robot , for internal comments website for wlmart it may work or later the comments database can be directly be used.
So html parser [script](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/blob/master/walmart/parsehtml.py)  does the same work in offline models, where comments webpages are [downloaded](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/tree/master/walmart/input) and the script is used to scrape the comments and used to create the [documents corpus](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/tree/master/walmart/output)

####  VOYANT TOOLS
[voyant tools](http://voyant-tools.org/?corpus=04b67f0d9b57f9551e9e4c0673ad042d) upload of the corpus of dcouments produced the linked dashboards in the nice visualization

#### Mallet
Further references of [mallet](https://programminghistorian.org/lessons/topic-modeling-and-mallet) and [here](http://mallet.cs.umass.edu/index.php) Setting up the mallet corpus and generating the trained topics based on following
```bash
mallet import-dir --input sample-data/web/en/ --output sample.mallet --keep-sequence --remove-stopwords
mallet train-topics --input sample.mallet
mallet train-topics  --input sample.mallet  --num-topics 20 --optimize-interval 20  --output-topic-keys sample_keys.txt --output-doc-topics sample_composition.txt
```
One can open the [composition file](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/blob/master/walmart/walmart-composition.txt) in excel to see the topic which has got the highest relevance probability and the same topic can be cross-referenced from the file output of [topic-keys](https://gecgithub01.walmart.com/Logistics/wm-vaak-topic-modelling/blob/master/walmart/walmart-keys.txt)


For training the corpus collected from walmart
#### consumer affairs comments

```bash
mallet import-dir --input output --output walmart.mallet --keep-sequence --remove-stopwords
mallet train-topics --input walmart.mallet
mallet train-topics --input walmart.mallet --num-topics 5 --optimize-interval 5 --output-topic-keys walmart-keys.txt --output-doc-topics walmart-composition.txt
```

#### All the documents were taken from the customer feedback to form a document corpus. The topics thus generated were accurately depicting that these documents form a cluster of topics which are related to customer feedback on there interaction with walmart. So if these documents were not sorted topic modelling would be a good place to start so that customer feedback can be sorted . As shown by the sample data which contains documents from various sources and with various disparate topics.
# wm-mallet
