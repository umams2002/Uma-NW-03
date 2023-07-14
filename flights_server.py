import pathlib
from shiny import render
import pandas as pd
import seaborn as sns

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

def get_flights_server_function(input, output, session):
    path_to_data = pathlib.Path(__file__).parent.joinpath("data").joinpath("flights.csv")
    original_df = pd.read_csv(path_to_data)
 
    total_count = len(original_df)

    @output
    @render.table
    def flights_table():
        return original_df
    
    @output
    @render.text
    def flights_record_count_string():
        message = f"Showing {total_count} records"
        logger.debug(f"filter message: {message}")
        return message

    @output
    @render.plot
    def flights_plot():
         plt =sns.barplot(
             data=original_df,
             x="year",
             y="passengers",
         )
         return plt

    
    
    return [
        flights_table,
        flights_record_count_string,
        flights_plot,
    ]