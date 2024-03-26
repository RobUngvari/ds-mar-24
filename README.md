Based on our exploratory data analysis and modeling efforts, several patterns emerge regarding factors influencing attrition within the company:

1. **Age and Attrition**: The attrition rate appears to be highest among younger employees, suggesting that youthfulness may correlate with a higher likelihood of leaving the company. This trend could be attributed to factors such as lower job satisfaction among younger adults, which may increase the propensity for job switching.

2. **Income and Attrition**: Another notable finding is that employees in the lower income bracket are more prone to leaving the company. This indicates that income level is a significant predictor of attrition, especially when combined with younger age.

3. **Managerial Tenure**: Surprisingly, the length of time with a current manager does not strongly influence attrition rates, even when considering gender differences. However, for younger employees engaged in highly involving jobs, even with lower pay, the likelihood of attrition remains significant.

4. **Gender and Involvement**: Gender disparities also play a role, particularly for women in less involving roles, where the probability of leaving the company is higher. This tendency is more pronounced in older age groups.

5. **Distance from Home**: Contrary to previous studies, the distance from home to the workplace shows low predictive power for attrition. However, among colleagues with lower income, those who live closer to the workplace tend to leave the company more frequently.

6. **Salary Hikes and Age**: Salary increases seem to have a mitigating effect on attrition among employees aged 40 and above. Conversely, in the youngest age range, salary hikes may slightly elevate attrition rates.

In terms of modeling, we uncovered additional nuanced patterns. For instance, overtime is also an indicator of leaving, as well as having a lower number of work experiences. Additionally, the stock option level could contribute to attrition.

Overall, our analysis suggests that age, income, job involvement, gender dynamics, overtime, work experience, and stock option level are key factors influencing attrition within the company. While some trends align with prior expectations, others challenge conventional wisdom. These findings underscore the complexity of attrition dynamics and highlight the importance of considering multiple factors in retention strategies.

After preprocessing the data by removing correlated features, we delved into exploring tree-based feature importances and SHAP values to identify and eliminate features with zero SHAP values and low feature importances. Furthermore, columns with high Variance Inflation Factor (VIF) scores were also removed. Additionally, we utilized CatBoost to gain insights into label importances.
As a final step, we encoded all categorical features using one-hot encoding. Fortunately, the dataset did not contain many high-cardinality features, making this approach suitable. Subsequently, we trained logistic regression, XGBoost, and LightGBM models without extensive hyperparameter tuning at this stage.
Among these models, the boosting methodology of LightGBM demonstrated the most promising performance, achieving a 42% recall rate. This metric holds particular significance for our analysis, as it emphasizes capturing as many true positives as possible, enabling us to identify actionable patterns. Although the final LightGBM model could potentially be further optimized, the overall results suggest room for improvement but still provide valuable insights.
