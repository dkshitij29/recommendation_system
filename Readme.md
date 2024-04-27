# Recommendation System
---
## Overview

This recommendation system is designed to suggest relevant items based on a given category and price range. It uses pandas dataframes to filter and select items from various categories.

## Files

- `Project.ipynb`: Contains the Python code for the recommendation system.
- `merged_df.csv`: CSV file containing the dataset with item details.
- `README.md`: This README file.

## Setup

1. Ensure you have Python installed on your system.

2. Install the required dependencies using pip, or you can refer this [link](https://jupyter.org/install):

   ```
   pip install notebook
   ```
2. clone this repo.
    ```
    git clone https://github.com/dkshitij29/recommendation_system.git
    ```
3. Now navigate to the recommendation_system directory

    ```
    cd recommendation_system
    ```
4. If you have configured the notebook correctly you can run the jupyter notebook with this command.
    ```
    jupyter notebook
    ```

alternatively you could upload this notebook in [collab](https://colab.research.google.com).

## Usage

1. Open the `Project.ipynb` file in a text editor or an notebook or collab.
4. Follow the prompts to enter a category and price range.
5. The system will then suggest relevant items based on the given category and price range.

## Example

For testing we included recommendations for "Gift Wrapping Supplies" with a price range of $8.89 ± $5. You would run the script and input the category and price range accordingly.

## Notes

- Ensure that the `merged_df.csv` dataset contains the necessary columns (`title`, `category_name`, `price`, etc.) and is properly formatted.
- The recommendation system uses pandas dataframes for efficient data manipulation and selection.

---

Feel free to customize this README file further based on your specific needs or additional information about the recommendation system.

## Future Improvements:
- Designing an addon system which can categories the items into parent categories which will act as a input to the system.
- We are specific to one data set in other works we are data specific and data driven, An data independent system can be designed using our design as a base.
