# Recommendation-Algorithm

One common way of increasing exposure to the long tail of products is by simply jittering the results at random. But injecting randomness has two issues: first, you need an awful lot of it to get products deep in the catalog to bubble up, and second, it breaks the framing of the recommendations and makes them less credible in the eyes of your customers.

Basic Approach

Before we dive into the code, let's outline the basic approach by visualizing the data. All the code for each intermediate step, and the visualizations, is included and explained later.

Here's the add-to-carts for product 542, from the sample dataset:

basic-trend

The first thing we'll do is add a low-pass filter (a smoothing function) so daily fluctuations are attentuated.

smoothed

Then we'll standardize the Y-axis, so popular products are comparable with less popular products. Note the change in the Y-axis values.

standardized

Last, we'll calculate the slopes of each line segment of the smoothed trend.

slopes

Our algorithm will perform these steps (in memory, of course, not visually) for each product in the dataset and then simply return the products with the greatest slope values in the past day, e.g. the max values of the red line at t=-1
