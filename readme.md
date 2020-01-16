# Apify Medium

A simple Flask wrapper that scrapes a Medium article and returns JSON.

Requires Python 3.6+ 

### Installation

    pip install -r requirements.txt
    
    or
    
    pip3 install -r requirements.txt
    
### Usage

Run locally

    python app.py
    
Default port for Flask is 500

Visit

    http://127.0.0.1:5000/

Response

    {
        message: "To use the API goto http://127.0.0.1:5000/medium?url=https://medium.com/@sagunshrestha/analyzing-cnets-headlines-3f350bb97cd4"
    }
    
Supply a Medium article's url

    http://127.0.0.1:5000/medium?url=https://medium.com/@sagunshrestha/analyzing-cnets-headlines-3f350bb97cd4
    
Response:

```
{
    author: "Sagun Shrestha",
    author_url: "https://towardsdatascience.com/@sagunshrestha",
    description: "I wrote a crawler to scrape the news headlines from CNET’s sitemap and decided to perform some exploratory analysis on it. In this post, I will walk you through my findings, some anomalies and some…",
    id: "3f350bb97cd4",
    image: "https://miro.medium.com/max/12000/0*cGuruaul8ki2Ou1n",
    keywords: [
        "Data Science",
        "Exploratory Data Analysis",
        "Pandas",
        "Python",
        "Data Visualization"
    ],
    modified_date: "2019-12-22T16:34:41.656Z",
    published_date: "2019-04-28T19:10:03.115Z",
    publisher: "Towards Data Science",
    publisher_url: "towardsdatascience.com",
    reading_time: "5 min read",
    subtitle: "Exploring the news published on CNET using Python and Pandas",
    title: "Analyzing CNET’s Headlines",
    url: "https://towardsdatascience.com/analyzing-cnets-headlines-3f350bb97cd4"
}
```