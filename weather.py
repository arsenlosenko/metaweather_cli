import click
import requests

from typing import List, Dict


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

    print_msg("Searching for entered location...", bg="blue", fg="white", bold=True)
    woeids = get_woeids(query_params)
    results = get_weather_forecast(woeids)
    print_msg("Showing results:", fg="white", bg="blue", bold=True)
    for result in results:
        msg = f"""
        City: {result["location"]}\n
        """
        for forecast in result["forecast"]:
            msg += f"""
            Weather briefly: {forecast["weather_state_name"]}
            Date: {forecast["applicable_date"]}
            Min Temp: {round_temp(forecast["min_temp"])} C
            Max Temp: {round_temp(forecast["max_temp"])} C
            Avg Temp: {round_temp(forecast["the_temp"])} C
            Humidity: {forecast["humidity"]} C
            """
        click.echo(msg)


def print_msg(text, fg=None, bg=None, bold=False):
    click.echo(click.style(text, fg=fg, bg=bg, bold=bold))


def round_temp(temp):
    if temp:
        return round(float(temp))
    return temp


def get_woeids(query_params: Dict) -> List[str]:
    url = "https://www.metaweather.com/api/location/search/"
    resp = requests.get(url, params=query_params)
    woeids = list()
    if resp.json():
        for result in resp.json():
            woeids.append(result["woeid"])
    return woeids

def get_weather_forecast(woeids: List[str]) -> List[Dict]:
    results = list()
    for woeid in woeids:
        url = f"https://www.metaweather.com/api/location/{woeid}/"
        resp = requests.get(url)
        if resp.json():
            results.append({
                "location": resp.json()["title"],
                "forecast": resp.json()["consolidated_weather"]
            })
    return results
        
if __name__ == "__main__":
    forecast()