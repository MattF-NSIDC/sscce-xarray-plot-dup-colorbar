import cartopy.crs as crs
import matplotlib
import xarray as xra

# The app crashes on second load if the following setting is not applied.
#     https://matplotlib.org/stable/users/explain/backends.html
# Error:
#     UserWarning: Starting a Matplotlib GUI outside of the main thread will likely
#     fail.
matplotlib.use('Agg')


def make_plot():
    """Plot air temp in a way that reproduces duplicate colorbar issue.

    One additional colorbar will be added for each page load.
    """
    air_temp = xra.tutorial.open_dataset("air_temperature").air.isel(time=0)

    plot = air_temp.plot(
        subplot_kws={
            'projection': crs.Orthographic(-45, 75),
            'facecolor': "gray"
        },
        transform=crs.PlateCarree(),
        # Uncomment to fix the duplicate colorbar behavior:
        # figsize=(6, 6),
    )
    plot.axes.coastlines(resolution='110m', color='white', linewidth=0.5)

    fig = plot.figure
    return fig
