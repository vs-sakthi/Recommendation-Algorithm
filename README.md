# Recommendation-Algorithm

One common way of increasing exposure to the long tail of products is by simply jittering the results at random. But injecting randomness has two issues: first, you need an awful lot of it to get products deep in the catalog to bubble up, and second, it breaks the framing of the recommendations and makes them less credible in the eyes of your customers.

Implementing a Trending Products Engine

First, let's get our add-to-cart data. From our database, this is relatively simple; we track the creation time of every cart-product (we call it a 'shipment item') so we can just extract this using SQL. I've taken the last 20 days of cart data so we can see some trends (though really only a few days of data is needed to determine what's trending):

Each row represents the number of cart adds for a particular product on a particular day in the past 20 days. I use 'age' as -20 (20 days ago) to -1 (yesterday) so that, when visualizing the data, it reads left-to-right, past-to-present, intuitively.

Here's sample data(In the repo) for 100 random products from our database. I'm anonymized both the product IDs and the cart-adds in such a way that, when standardized, the results are completely real, but the individual data points don't represent our actual business.

Basic Approach

Before we dive into the code, let's outline the basic approach by visualizing the data. All the code for each intermediate step, and the visualizations, is included and explained later.

basic-trend

The first thing we'll do is add a low-pass filter (a smoothing function) so daily fluctuations are attentuated.

smoothed

Then we'll standardize the Y-axis, so popular products are comparable with less popular products. Note the change in the Y-axis values.

standardized

Last, we'll calculate the slopes of each line segment of the smoothed trend.

slopes

Our algorithm will perform these steps (in memory, of course, not visually) for each product in the dataset and then simply return the products with the greatest slope values in the past day, e.g. the max values of the red line at t=-1
