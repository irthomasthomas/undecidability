**Prompt:**
Continue this list, adding queries for many popular forums like hackernews, and shopping sites like ebay.com, ebay.co.uk, amazon.co.uk, amazon.com and lots more.\n\n\n# Tags and attributes to search for in the HTML response to find the article title
TITLE_QUERIES = [
    ("title", {}),
    ("h1", {"class": "story-body__h1"}),
    ("h1", {"class": "story-body__h1"}),
    ("h1", {"class": "entry-title"}),
    ("h1", {"class": "post-title"}),
    ("h1", {"class": "blog-post-title"}),
    ("h1", {"class": "article-title"}),
    ("h1", {"class": "entry-title"}),
    ("h1", {"class": "post-title"}),
    ("h1", {"class": "blog-post-title"}),
    ("h1", {"class": "article-title"}),
    ("h1", {"class": "entry-title"}),

**Response:**
("a", {"class": "story-link"}),
    ("a", {"class": "headline"}),
]

# Tags and attributes to search for in the HTML response to find the article url
URL_QUERIES = [
    ("a", {"class": "story-link"}),
    ("a", {"class": "headline"}),
    ("a", {"class": "title"}),
    ("a", {"class": "entry-title"}),
    ("a", {"class": "post-title"}),
    ("a", {"class": "blog-post-title"}),
    ("a", {"class": "article-title"}),
    ("a", {"class": "entry-title"}),
    ("a", {"class": "post-title"}),
    ("a", {"class": "blog-post-title"}),
    ("a", {"class": "article-title"}),
    ("a", {"class": "entry-title"}),
    ("a", {"class": "review-title"}),
]

# Tags and attributes to search for in the HTML response to find the article description
DESCRIPTION_QUERIES = [
    ("p", {"class": "story-description"}),
    ("p", {"class": "story-body__intro"}),
    ("p", {"class": "entry-summary"}),
    ("p", {"class": "post-summary"}),
    ("p", {"class": "blog-post-summary"}),
    ("p", {"class": "article-summary"}),
    ("p", {"class": "entry-summary"}),
    ("p", {"class": "post-summary"}),
    ("p", {"class": "blog-post-summary"}),
    ("p", {"class": "article-summary"}),
    ("p", {"class": "entry-summary"}),
    ("p", {"class": "post-summary"}),
    ("p", {"class": "blog-post-summary"}),
    ("p", {"class": "article-summary"}),
    ("p", {"class": "review-summary"}),
]

# Tags and attributes to search for in the HTML response to find the article publication date
DATE_QUERIES = [
    ("meta", {"property": "article:published_time"}),
    ("meta", {"name": "date"}),
    ("meta", {"name": "pubdate"}),
    ("time", {"class": "published"}),
    ("time", {"class": "entry-date"}),
    ("time", {"class": "post-date"}),
    ("time", {"class": "published"}),
    ("time", {"class": "entry-date"}),
    ("time", {"class": "post-date"}),
    ("time", {"class": "published"}),
    ("time", {"class": "entry-date"}),
    ("time", {"class": "post-date"}),
    ("time", {"class": "published"}),
    ("time", {"class": "entry-date"}),
    ("time", {"class": "post-date"}),
    ("time", {"class": "review-date"}),
]

# Tags and attributes to search for in the HTML response to find the article author
AUTHOR_QUERIES = [
    ("meta", {"name": "author"}),
    ("span", {"class": "author"}),
    ("span", {"class": "byline"}),
    ("span", {"class": "post-author"}),
    ("span", {"class": "blog-author"}),
    ("span", {"class": "article-author"}),
    ("span", {"class": "entry-author"}),
    ("span", {"class": "post-author"}),
    ("span", {"class": "blog-author"}),
    ("span", {"class": "article-author"}),
    ("span", {"class": "entry-author"}),
    ("span", {"class": "post-author"}),
    ("span", {"class": "blog-author"}),
    ("span", {"class": "article-author"}),
    ("span", {"class": "entry-author"}),
    ("span", {"class": "review-author"}),
]

<details><summary>Metadata</summary>

- Duration: 55271 ms
- Datetime: 2023-09-06T19:14:53.556164
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

