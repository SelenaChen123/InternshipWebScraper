# InternshipWebScraper

## Project Description:

For the final project, you will:

-   Develop a documented dataset to support looking at a particular problem
    -   To document your dataset, create metadata that outlines sources, attribution, and ethics
-   Have reproducible code for retrieval from the web, data cleaning, and final a dataset
-   Discuss the dataset, the process above, and demonstrate how it addresses the original problem statement in a separate 1-2 page summary
-   Submit your report to Moodle as one file

## Project Documentation

### Problem Statement:

As an upperclassman Computer Science major stressing over having to find internships to gain experience and give us a leg up when it comes to our job search after graduation, finding internships to apply for can be a tricky task. It’s important to weigh all of the factors that are important to us when determining which internships to apply for. One such major factor is compensation. As greedy as that sounds, the sad truth is that most college students have hefty tuition loans, expensive rent, and utility bills to pay for, so internships with higher pay are much more appealing. There are so many companies offering software engineering internships, but where should students start looking for the ones that pay the most?

### Description

The purpose of this web scraper is to scrape the levels.fyi website, which lets you compare salary information at different career levels for positions at various companies, in order to consolidate a fairly comprehensive list of software engineering internships. This dataset only shows information about the software engineering internships that are currently open for applications. For the ones that are still open for applications, the dataset shows which ones pay the most, if the companies provide housing accommodations, and the link to apply for the internship directly on the company’s website. With this information, students looking for software engineering internships have a great resource that lists higher-paying internships that they can still apply for.

### Metadata

#### Ethics

There are no public APIs that I could find for this information, but the information from this website is open to the public. Selenium, a browser automation tool, is used to establish a connection to the website, but since I am only scraping information from a single webpage rather than several webpages, there shouldn’t be an issue of creating repetitive connections that would potentially damage the website’s stability and start a DDoS attack. I also make sure to cite the source and give credit to the co-founders of the website so that I am respectful of the content creators’ work.

#### Sources:

https://www.levels.fyi/

#### Attribution:

Zaheer Mohiuddin and Zuhayeer Musa

