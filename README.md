# `Capital Asset Pricing Model (CAPM)`

The Capital Asset Pricing Model (CAPM) is a financial model used to determine the expected return on an investment, based on its risk relative to the overall market. It is widely used in finance for pricing risky securities, calculating the cost of equity, and assisting in portfolio management.

### `Key Components of CAPM`
The model is represented by the following formula:

$$ r_i = r_f + \beta_i(r_m - r_f). $$

- $r_i =$  Expected return of the investment (also called required return).
- $r_f =$ Risk-free rate (the return on a risk-free investment, typically government bonds).
- $B_i =$ Expected return of the market (often represented by a broad market index like the S&P 500).
- $r_m =$ Expected return of the market (often represented by a broad market index like the S&P 500).
- $r_m - r_f =$  Market risk premium (the excess return expected from the market over the risk-free rate).

### `Explanation of the Components`
- Risk-Free Rate ($r_f$): This is the return on an investment that is considered to have zero risk, typically government securities such as U.S. Treasury bonds. It represents the time value of money—how much investors would earn without taking any risk. Investors who are extremly risk adverse would prefer to buy the risk free asset to protect thier money and earn a low return.

- Market Porfolio Return: This includes all securities in the market. A good representation of the market portfolio is the `S&P 500`. Market portfolio return is the average return of the overall return of the `S&P 500`.

- Beta ($\beta$): Beta measures how much the price of an individual asset moves compared to the market. A beta of:
    - 1 means the asset moves in line with the market.
    - Greater than 1 means the asset is more volatile than the market (higher risk and potential return).
    - Less than 1 means the asset is less volatile than the market (lower risk and potential return).
    - Negative beta indicates the asset moves in the opposite direction of the market.

   Beta ($\beta$) can either be obtained using the covariance method or the Linear regression method. For the purpose fo this project, we will adopt the linear regression method.

   The Covariance method is calculated using:
   
   $$ \beta = \frac{\text{Cov}(R_{\text{stock}}, R_{\text{market}})}{\text{Var}(R_\text{market})} \,. $$

   Where:
   - **Cov** is the covariance between the stock's returns and the market's returns.
   - **Var** is the variance of the market's returns.
   
   
   The Linear Regression method (`np.polyfit`)  calculates Beta $\beta$ as the slope of the linear relationship between the stock’s returns and the market's returns.






$$y = \beta x + \alpha \,.$$
 

### `Interpreting the CAPM`
- High Beta ($\beta > 1$): If an asset has a $\beta$ greater than 1, it is considered riskier than the overall market. According to CAPM, it should have a higher expected return to compensate for the higher risk.

- Low Beta ($\beta  < 1$): If an asset has a $\beta$ less than 1, it is considered less risky than the market. Therefore, it is expected to have a lower return.

- Risk-Return Trade-Off: CAPM reinforces the principle of the risk-return trade-off: the more risk you take (higher beta), the more return you expect to earn, and vice versa.