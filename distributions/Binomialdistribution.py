
# coding: utf-8

# In[2]:


# TODO: import necessary libraries
import math
import matplotlib.pyplot as plt
from Generaldistribution import Distribution


class Binomial(Distribution):

    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))

    #

    def __init__(self, p = 0.5, n = 20, mu = 0, sigma = 1):
        Distribution.__init__(self, mu, sigma)
        self.data = []
        self.p = p
        self.n = n

        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
    def calculate_mean(self):
        self.mean = self.p * self.n
        return self.mean

        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """

    def calculate_stdev(self):
        stdev = math.sqrt(self.n * self.p * (1 - self.p))
        self.sigma = stdev
        return stdev


        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
    def replace_stats_with_data(self, *args, **kwargs):
        super(Binomial, self).read_data_file(*args, **kwargs)
        
        self.n = len(self.data)
        self.p = sum(self.data) / len(self.data)

        self.mean = self.calculate_mean()
        self.sigma = self.calculate_stdev()
        p = self.p
        n = self.n
        return p,n

    # TODO: write a method plot_bar() that outputs a bar chart of the data set according to the following specifications.
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
    def plot_bar(self):
        x_height = self.mean
        y_height = len(self.data) - sum(self.data)
        x = [0,1]
        plt.bar(x, [x_height, y_height])
        plt.xticks(x, (0,1))
        plt.title('Histogram of the data')
        plt.show();

    #TODO: Calculate the probability density function of the binomial distribution
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
    def pdf(self, k):
        n = self.n
        p = self.p
        numerator = math.factorial(int(n))
        denominator = math.factorial(int(k)) * math.factorial(int(n - k))
        
        f = (numerator / denominator) * (p**k) * ((1-p)**(n-k))
        return f


    # write a method to plot the probability density function of the binomial distribution

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """


    def plot_bar_pdf(self):
        x = []
        y = []
        n = self.n
        for k in range(n):
            x.append(k)
            y.append(self.pdf(k))

        plt.bar(x,y)
        plt.xticks(range(n))
        plt.xlabel('k')
        plt.ylabel('probability density')
        plt.title('Histogram of probability density')
        plt.show();
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.

        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """
    def __add__(self,other):

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n

        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.

    # use the __repr__ magic method to output the characteristics of the binomial distribution object.

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """

        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format

    def __repr__(self):
        return("mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.sigma, self.p, self.n))


# In[3]:


bin = Binomial()


# In[4]:


bin.replace_stats_with_data('numbers_binomial.txt')


# In[5]:


bin.calculate_mean()

