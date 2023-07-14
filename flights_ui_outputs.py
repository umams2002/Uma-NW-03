from shiny import ui


def get_flights_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Output (Not Yet Reactive)"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Passenger Chart (Seaborn Scatter Plot)"),
            ui.output_plot("flights_plot"),
            ui.tags.hr(),
            ui.h3("Passenger Table"),
            ui.output_text("flights_record_count_string"),
            ui.output_table("flights_table"),
            ui.tags.hr(),
        ),
    )