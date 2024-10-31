import asyncio

import uvloop

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.key.mnemonic import MnemonicKey
import time


async def main():
    paloma = AsyncLCDClient(
        url="https://lcd.palomachain.com/", chain_id="tumbler"
    )
    paloma.gas_prices = "0.01ugrain"

    acc = MnemonicKey(
        mnemonic=""
    )

    test1 = paloma.wallet(acc)
    print(test1.key.acc_address)
    eth_dest = "0x0000000000000000000000000000000000000000"
    creator = test1.key.acc_address
    signers = [test1.key.acc_address]
    result = await paloma.skyway.send_tx(test1, eth_dest, "ugrain", 1000000, "base-main", creator, signers)
    print(result)
    result = await paloma.skyway.cancel_tx(test1, 17, creator, signers)
    print(result)
    await paloma.session.close()

uvloop.install()
asyncio.run(main())
