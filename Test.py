from great_tables import GT, md, html
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "year", "hp", "trq", "msrp"]].tail(10)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .tab_spanner(label=md("*Performance*"), columns=["hp", "trq"])
    .tab_header(
        title=html("Data listing from <strong>gtcars</strong>"),
        subtitle=html("A <span style='font-size:12px;'>small selection</span> of great cars."),
    )
    .cols_label(year="Year Produced", hp="HP", trq="Torque", msrp="Price (USD)")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .tab_source_note(source_note="Source: the gtcars dataset within the Great Tables package.")
)