import pandas as pd
import matplotlib.pyplot as plt
import re
import os 

class DataPipeline:
    """
    A data processing pipeline for employee survey data.

    Usage (once implemented):
    pipeline = DataPipeline("messy_employee_survey.csv")
    results = pipeline.run()
    """
    # Canonical spelling for normalization - clean() method uses this dicts
    DEPT_MAP = {
            "engineering": "Engineering",
            "eng": "Engineering",
            "marketing":"Marketing",
            "mktg": "Marketing",
            "sales": "Sales",
            "hr": "HR",
            "h.r.": "HR",
            "finance": "Finance",
            "fin": "Finance",
    }

    LOC_MAP = {
        "new york": "New York",
        "nyc": "New York",
        "chicago": "Chicago",
        "chi":"Chicago",
        "austin":"Austin",
        "austin tx":"Austin",
        "atx":"Austin",
        "seattle":"Seattle",
        "sea":"Seattle",
        "remote":"Remote",
        "work from home":"Remote",
    }
    def __init__(self, filepath: str) -> None:
        """ Load the csv at 'filepath' into self.df(a pandas DataFrame).
         print how many rows and columns were loaded.
          Args : 
           filepath to the messy CSV  file 
        """
        try:
            self.df = pd.read_csv(filepath)
            rows, columns = self.df.shape
            print(f"Rows: {rows} Columns: {columns}")
        except FileNotFoundError:
            
            print(f"Error: {filepath} not found")
            self.df = None

    

    def clean(self):
        """
        Clean the DataFrame stored in self.df and print a summary.
        Steps to implement (in order):
        1. Remove rows with duplicate employee_id (keep first occurance).
        2. Standardize 'name' - strip whitespace, title case.
        3. Normalize 'department' - map messy variants to canonical names.
        4. Normalize 'office_location' - same pattern as department
        5. Convert 'salary' to float - strip "$" and "," first, set negatives to None.
        6. Convert 'years_exprience' to numeric: set values > 50 to None (outliers).
        7. Convert 'satisfaction_score' to numeric; will set values outside of 1-10 to None
        8. Parse 'survey_date'  - multiple formats exist (MM/DD/YYYY, YYYY-MM-DD, DD-MM-YYYY).
        """
        self.df = self.df.drop_duplicates(subset=["employee_id"], keep="first")
        self.df["name"] = self.df["name"].str.strip().str.title()
        self.df["department"] = self.df["department"].str.strip().str.lower().map(self.DEPT_MAP)
        self.df["office_location"] = self.df["office_location"].str.strip().str.lower().map(self.LOC_MAP)

        def clean_salary(val):
            try:
                cleaned = re.sub(r"[$,]", "", str(val))
                salary = float(cleaned)

                if salary < 0:
                    return None

                return salary

            except ValueError:
                return None
        self.df["salary"] = self.df["salary"].apply(clean_salary)
        self.df["years_experience"] = pd.to_numeric(self.df["years_experience"], errors="coerce")
        self.df.loc[self.df["years_experience"] > 50, "years_experience"] = pd.NA
        self.df["satisfaction_score"] = pd.to_numeric(self.df["satisfaction_score"], errors="coerce")
        self.df.loc[(self.df["satisfaction_score"] < 1) | (self.df["satisfaction_score"] > 10), "satisfaction_score"] = pd.NA

        def parse_date(val):
            formats = [
                "%m/%d/%Y",
                "%Y-%m-%d",
                "%d-%m-%Y"
            ]
            for fmt in formats:
                try:
                    return pd.to_datetime(val, format=fmt)
                except ValueError:
                    continue

            return None
        self.df["survey_date"] = self.df["survey_date"].apply(parse_date)
        print(f"Missing Values: {self.df.isnull().sum()}")
        return self
    def analyze(self):
        """ Compute summary statistics from the cleaned self.df.
        Compute and print:
        1. Average salary by department
        2. Average satisfaction score by department
        3. Headcount by office location
        4. Pearson correlation between years_exprience and salary
        5. One additional insight.
        Return dict with all results so main.py can use them.
        Keys to use: "avg_salary_by_dept", "avg_satisfaction_by_dept",
        "headcount_by_location", "experieence_salary_correlation", "avg_salary_by_location"

        """
        avg_salary_by_dept = self.df.groupby("department")["salary"].mean().round(0).sort_values(ascending=False)
        avg_satisfaction_by_dept = self.df.groupby("department")["satisfaction_score"].mean().round(2).sort_values(ascending=False)
        headcount_by_location = self.df["office_location"].value_counts()
        temp_df = self.df.dropna(subset=["years_experience", "salary"])
        experience_salary_correlation = temp_df["years_experience"].corr(temp_df["salary"])
        max_salary_by_location = self.df.groupby("office_location")["salary"].max()

        print(f"Average Salary by department:\n{avg_salary_by_dept}")
        print(f"Average satisfaction score by department:\n{avg_satisfaction_by_dept}")
        print(f"headcount by location:\n{headcount_by_location}")
        print(f"Experience Salary correlation\n{experience_salary_correlation}")
        print(f"Maximum Salary at each location:\n{max_salary_by_location}")
        return {
            "avg_salary_by_dept" : avg_salary_by_dept,
            "avg_satisfaction_by_dept": avg_satisfaction_by_dept,
            "headcount_by_location":headcount_by_location,
            "experience_salary_correlation":experience_salary_correlation,
            "max_salary_by_location": max_salary_by_location
        }
    def visualize(self, output_path="output/charts.png"):
        """Create and visualizations to 'output_path
        Required Charts:
            - Bar char: average salary by department
            -  Histogram: satisfaction score distribution (bins 1-10)
            Bonus:
            - Horizontal  bar: headcount by office location
        Args: 
         output_path: where to save the PNG file


        """
        if self.df is None:
            raise ValueError("No DataFrame is loaded.")
        
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        results = self.analyze()
        #Chart 1 average salary by department

        avg_sal_dept = results["avg_salary_by_dept"]
        head_count_offices = results["headcount_by_location"]
        axes[0].bar(avg_sal_dept.index, avg_sal_dept.values, color="steelblue" )
        axes[0].set_title("Average Salary by Department")
        axes[0].set_xlabel("Department $")
        axes[0].set_ylabel("Average salary $")
        axes[0].tick_params(axis="x", rotation=45)

        #Chart 2 satisfaction score distribution
        axes[1].hist(self.df["satisfaction_score"].dropna(), bins=range(1,12), color="coral", edgecolor="black", align="left",rwidth=0.85)
        axes[1].set_title("Satisfaction score Distribution")
        axes[1].set_xlabel("satisfaction score")
        axes[1].set_ylabel("Frequency")
        axes[1].set_xticks(range(1, 11))
        #Chart 3: Head count by office location
 
        axes[2].barh(head_count_offices.index, head_count_offices.values, color="steelblue")
        axes[2].set_title("Number offices at each location")
        axes[2].set_xlabel("total office")


        fig.tight_layout()
        fig.savefig(output_path, dpi=120, bbox_inches="tight")
        plt.close(fig)
        print(f"Charts saved to {output_path}")
        
    def export(self, output_path="output/clean_employess.csv"):
        """ Save the cleaned self.df to a CSV at 'outputh_path
        Create the output directory if it does not exist.
        
        """
        if self.df is None:
            raise ValueError("No DataFrame is loaded.")
        try:
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                self.df.to_csv(output_path, index=False)
                print(f"Cleaned data exported to {output_path}")
        except (OSError, ValueError) as error:
            print(f"Error exporting data: {error}")
    def run(self):
        """
        Execute the full pipeline: clean → analyze → visualize → export
        Build output paths using os.path.join(os.path.dirname(__file__), "output", ...)
        Return the results dict from analyze()
        """
        base_dir = os.path.dirname(__file__)
        charts_path = os.path.join(
            base_dir,"output","charts.png"
        )
        csv_path = os.path.join(
            base_dir,
            "output",
            "clean_employees.csv"
        )
        self.clean()
        results = self.analyze()
        self.visualize(charts_path)
        self.export(csv_path)
        return results






                  





