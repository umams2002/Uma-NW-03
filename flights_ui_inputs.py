from shiny import ui

def get_flights_inputs():
    return ui.panel_sidebar(
        ui.h2("Flights Passenger travelled"),
        ui.tags.hr(),
        ui.input_slider(
            "Passenger_Travelled",
            "Year",
            min=1949,
            max=1960,
            value=[1949,1960],
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Passenger per Year Table"),
            ui.tags.p("Description of each field in the table"),
            ui.tags.ul(
                    ui.tags.li("year: Year"),
                    #ui.tags.li("month: Month"),
                    ui.tags.li("passengers: Passengers"),
            ),
            ui.output_table("pasengers_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
