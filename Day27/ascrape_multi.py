import asyncio
from aiohttp import ClientSession
import pathlib


async def fetch(url, session, year=None):
    async with session.get(url) as response:
        html_body = await response.read()
        return {"body": html_body, "year": year}


async def fetch_with_sem(url, session, year, sem):
    async with sem:
        return await fetch(url, session, year)


async def main(start_year=2021, years_ago=20):
    tasks = []
    html_body = ""

    # semafor - prevent zahltenia servera
    sem = asyncio.Semaphore(10)    # limit, kolko taskov môže bezať simultanne
    async with ClientSession() as session:
        for i in range(0, years_ago):
            year = start_year - i
            url = f'https://www.boxofficemojo.com/year/{year}/'
            print("year: ", year, url)
            tasks.append(
                asyncio.create_task(
                    fetch_with_sem(url, session, year, sem)
                )
            )
        pages_content = await asyncio.gather(*tasks)
        return pages_content


results = asyncio.run(main())
output_dir = pathlib.Path().resolve() / "snapshots"
output_dir.mkdir(parents=True, exist_ok=True)

for result in results:
    current_year = result.get("year")
    html_data = result.get('body')
    output_file = output_dir / f"{current_year}.html"
    output_file.write_text(html_data.decode())
    # with open('path/to/output', 'w') as f:
    #   f.write(html_data.decode())
