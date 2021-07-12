import aiohttp
import urllib
import asyncio
Api_BASEURL = "http://denzven.pythonanywhere.com/"
#Api_BASEURL = "https://denzven-graphing-api.herokuapp.com/"
#Api_BASEURL = "https://async-denzven-graphing-api.herokuapp.com/"
#Api_BASEURL = "http://127.0.0.1:5000/"

print("testing api speed")
print("10 formulas")

async def test():
    sample_json = {
        "../test/file1.png": "x-y",
        "../test/file2.png": "x+y",
        "../test/file3.png": "x**2+y",
        "../test/file4.png": "x+y**2",
        "../test/file5.png": "x**2+y**2",
        "../test/file6.png": "x**2+y**2-10",
        "../test/file7.png": "sin(x)-y",
        "../test/file8.png": "sin(y)-x",
        "../test/file9.png": "cos(x)-y",
        "../test/file10.png": "cos(y)-x",
    }

    for file in sample_json:
        async with aiohttp.ClientSession() as session:
            formula_output = urllib.parse.quote(sample_json[file], safe='')
            url = Api_BASEURL + f'/DenzGraphingApi/v1/flat_graph/test/plot?formula={formula_output}'
            async with session.get(url) as r:
                file_ = open(file, "wb")
                file_.write(await r.read())
                file_.close()
                print(f"Done => {formula_output}")

def test_prof():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        asyncio.run(test())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    #stats.dump_stats(filename='test_prof.prof')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_prof())

test_prof()