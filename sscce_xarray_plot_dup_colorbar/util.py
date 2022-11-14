import cartopy.crs as crs
import matplotlib
import xarray as xra

matplotlib.use('Agg')


def make_plot():
    """Plot air temp in a way that reproduces duplicate colorbar issue."""
    air_temp = xra.tutorial.open_dataset("air_temperature").air.isel(time=0)

    plot = air_temp.plot(
        subplot_kws={
            'projection': crs.Orthographic(-45, 90),
            'facecolor': "gray"
        },
        transform=crs.PlateCarree(),
        # Uncomment to fix the behavior:
        # figsize=(6, 6),
    )
    plot.axes.coastlines(resolution='110m', color='white', linewidth=0.5)

    fig = plot.figure
    return fig
