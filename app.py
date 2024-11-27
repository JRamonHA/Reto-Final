from shiny import render
from shiny.express import input, ui
import pandas as pd
import matplotlib.pyplot as plt
import settings.funciones as fu

f = fu.cargar_anio("2010")
esol = pd.read_parquet(f)
nombres = list(esol)

with ui.sidebar(bg="#f8f8f8"):  
    ui.input_select("year", "Año", list(fu.years)) 
    ui.input_select("columna", "Variable", nombres)
    ui.input_checkbox("maximos", "Resample max")  

@render.plot() 
def plot_columna():  
    year_selected = input.year()
    f = fu.cargar_anio(year_selected)
    esol = pd.read_parquet(f)

    fig, ax = plt.subplots()
    ax.plot(esol[input.columna()])
    if input.maximos():
        ax.plot(esol[input.columna()].resample("D").max(), color="red")

    return fig
