import asyncio

import speedtest
from pyrogram import filters
from pyrogram.types import Message

from MoonXMusic import app
from MoonXMusic.misc import SUDOERS
from MoonXMusic.utils.decorators.language import language


def testspeed(m, _):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit_text(_["server_12"])
        test.download()
        m = m.edit_text(_["server_13"])
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit_text(_["server_14"])
    except Exception as e:
        return m.edit_text(f"<code>{e}</code>")
    return result


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
@language
async def speedtest_function(client, message: Message, _):
    m = await message.reply_text(_["server_11"])
    loop = asyncio.get_event_loop()

    try:
        # Run the speed test in an executor
        result = await loop.run_in_executor(None, testspeed, m, _)
        
        # Validate the result structure
        if not isinstance(result, dict) or "client" not in result or "server" not in result:
            raise ValueError("Invalid result format from testspeed")

        # Prepare the output message
        output = _["server_15"].format(
            result["client"]["isp"],
            result["client"]["country"],
            result["server"]["name"],
            result["server"]["country"],
            result["server"]["cc"],
            result["server"]["sponsor"],
            result["server"]["latency"],
            result["ping"],
        )
        # Send the result photo with the output message
        msg = await message.reply_photo(photo=result["share"], caption=output)
    except Exception as e:
        # Handle errors gracefully
        await message.reply_text(f"Error: {str(e)}")
    finally:
        # Clean up the temporary message
        await m.delete()
