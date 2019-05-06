# Apify Medium

A simple Flask wrapper that scrapes and convert a medium article to json data.

### Installation

Install all requirements

    pip install -r requirements.txt
    
### Usage

Run Flask Server

    python app.py
    
By default, it runs on port 5000
    
### API calls

In your browser, open the url

     http://127.0.0.1:5000/medium?url=<link to a medium article>
     
Sample Request:

    http://127.0.0.1:5000/medium?url=https://medium.com/@sagunshrestha/analyzing-cnets-headlines-3f350bb97cd4
    
Sample Response:

```
{
    author: "Sagun Shrestha",
    author_url: "https://medium.com/@sagunshrestha",
    claps: "52",
    id: "3f350bb97cd4",
    keywords: [
        "Data Science",
        "Exploratory Data Analysis",
        "Pandas",
        "Python",
        "Data Visualization"
    ],
    modified_date: "2019-04-29T16:31:19.558Z",
    published_date: "2019-04-28T19:10:03.115Z",
    publisher: "Medium",
    publisher_url: "https://medium.com/",
    reading_time: "5 min read",
    subtitle: "Exploring the news published on CNET using Python and Pandas",
    thumbnail: "https://cdn-images-1.medium.com/max/1454/1*xf9kQuTsPcSTHdwc_Ku1gA.png",
    title: "Analyzing CNET’s Headlines",
    url: "https://medium.com/@sagunshrestha/analyzing-cnets-headlines-3f350bb97cd4"
}
```