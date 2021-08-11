import click

from utils import print_styled_message, round_temp
from api_client import get_weather_forecast, get_woeids


@click.command()
@click.option('--query', help='Name of the location')
@click.option('--latt', help="Lattitude of location", type=float)
@click.option("--long", help="Longitude of location", type=float)
def forecast(query, latt, long):
    if query:
        query_params = {
            "query": query
        }
    elif latt and long:
        query_params = {
            "lattlong": f"{latt},{long}"
        }
    else:
        click.echo("please use either a '--query' command, or '--latt' and '--long' commands")
        return

    print_styled_message("Searching for entered location...", bg="blue", fg="white", bold=True)
    woeids = get_woeids(query_params)
    results = get_weather_forecast(woeids)
    print_styled_message("Showing results:", fg="white", bg="blue", bold=True)
    for result in results:
        msg = f"""
        City: {result["location"]}\n
        """
        for forecast in result["forecast"]:
            msg += f"""
            Date: {forecast["applicable_date"]}
            Weather briefly: {forecast["weather_state_name"]}
            Min Temp: {round_temp(forecast["min_temp"])} C
            Max Temp: {round_temp(forecast["max_temp"])} C
            Avg Temp: {round_temp(forecast["the_temp"])} C
            Humidity: {forecast["humidity"]} C
            """
        click.echo(msg)


if __name__ == "__main__":
    forecast()