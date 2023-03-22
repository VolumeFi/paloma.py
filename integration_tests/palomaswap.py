import asyncio
from pathlib import Path

import uvloop
from terra_proto.cosmwasm.wasm.v1 import AccessType
from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.core.wasm import MsgInstantiateContract, MsgStoreCode
from paloma_sdk.key.mnemonic import MnemonicKey
from paloma_sdk.core.wasm.data import AccessConfig
from paloma_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64


async def main():
    paloma = AsyncLCDClient(url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-15")
    paloma.gas_prices = "0.01ugrain"

    acc = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    acc2 = MnemonicKey(
        mnemonic="index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred"
    )
    test1 = paloma.wallet(acc)
    test2 = paloma.wallet(acc2)

    # store_code_tx = await test1.create_and_sign_tx(
    #     CreateTxOptions(
    #         msgs=[
    #             MsgStoreCode(
    #                 test1.key.acc_address,
    #                 read_file_as_b64(Path(__file__).parent / "./cw20_base.wasm"),
    #                 AccessConfig(AccessType.ACCESS_TYPE_EVERYBODY, ""),
    #             )
    #         ],
    #         gas_adjustment=1.75,
    #     )
    # )
    # store_code_tx_result = await paloma.tx.broadcast(store_code_tx)
    # print(store_code_tx_result)

    # code_id = get_code_id(store_code_tx_result)

    # code_id = 32
    # print(f"code_id:{code_id}")

    # result = await paloma.cw20.instantiate(
    #     test1, code_id, "CW20 Test Token 0", "CWFT-A", 9, 1_000_000_000_000_000
    # )
    # print(result)
    
    # contract_address = result.logs[0].events_by_type["instantiate"][
    #         "_contract_address"
    #     ][0]
    # token0 = contract_address
    # print(contract_address)
    
    # result = await paloma.cw20.instantiate(
    #     test1, code_id, "CW20 Test Token 1", "CWFT-B", 9, 1_000_000_000_000_000
    # )
    # print(result)
    
    # contract_address = result.logs[0].events_by_type["instantiate"][
    #         "_contract_address"
    #     ][0]
    # token1 = contract_address
    # print(contract_address)
    
    token0 = "paloma19usnw37lvx8jm6wehqqk56lxxcjd807py5l3trhrv92zy2s7rxsqdp6gee"
    token1 = "paloma1h8ch6gu7nrq4nk8gatn7wj0gnn0f4nhuqd3xj5elpjr4g5mvmpmq442wjj"
    # result = await paloma.cw20.transfer(test1, token0, test2.key.acc_address, 1_000_000_000)
    result = await paloma.palomaswap.create_stable_pair(test1, "paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t", [token0,token1])
    print(result)
    await paloma.session.close()
"""
https://lcd.testnet.palomaswap.com/cosmos/auth/v1beta1/accounts/paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8
BlockTxBroadcastResult(height=920183, txhash='903B567F551D7D8DDE5146C907B3590843A0DEAEEAFA0CEC93CEA8378DE11123', raw_log='[{"events":[{"type":"execute","attributes":[{"key":"_contract_address","value":"paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t"}]},{"type":"instantiate","attributes":[{"key":"_contract_address","value":"paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn"},{"key":"code_id","value":"36"},{"key":"_contract_address","value":"paloma1cm60qwjptgep3s6nke033cpe73d345zqls8talh8zcn09tdfv65qnu2h0s"},{"key":"code_id","value":"2"}]},{"type":"message","attributes":[{"key":"action","value":"/cosmwasm.wasm.v1.MsgExecuteContract"},{"key":"module","value":"wasm"},{"key":"sender","value":"paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8"}]},{"type":"reply","attributes":[{"key":"_contract_address","value":"paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn"},{"key":"_contract_address","value":"paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t"}]},{"type":"wasm","attributes":[{"key":"_contract_address","value":"paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t"},{"key":"action","value":"create_pair"},{"key":"pair","value":"paloma19usnw37lvx8jm6wehqqk56lxxcjd807py5l3trhrv92zy2s7rxsqdp6gee-paloma1h8ch6gu7nrq4nk8gatn7wj0gnn0f4nhuqd3xj5elpjr4g5mvmpmq442wjj"},{"key":"_contract_address","value":"paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn"},{"key":"liquidity_token_addr","value":"paloma1cm60qwjptgep3s6nke033cpe73d345zqls8talh8zcn09tdfv65qnu2h0s"},{"key":"_contract_address","value":"paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t"},{"key":"action","value":"register"},{"key":"pair_contract_addr","value":"paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn"}]}]}]', gas_wanted=963520, gas_used=564724, logs=[TxLog(msg_index=0, log='', events=[{'type': 'execute', 'attributes': [{'key': '_contract_address', 'value': 'paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t'}]}, {'type': 'instantiate', 'attributes': [{'key': '_contract_address', 'value': 'paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn'}, {'key': 'code_id', 'value': '36'}, {'key': '_contract_address', 'value': 'paloma1cm60qwjptgep3s6nke033cpe73d345zqls8talh8zcn09tdfv65qnu2h0s'}, {'key': 'code_id', 'value': '2'}]}, {'type': 'message', 'attributes': [{'key': 'action', 'value': '/cosmwasm.wasm.v1.MsgExecuteContract'}, {'key': 'module', 'value': 'wasm'}, {'key': 'sender', 'value': 'paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8'}]}, {'type': 'reply', 'attributes': [{'key': '_contract_address', 'value': 'paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn'}, {'key': '_contract_address', 'value': 'paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t'}]}, {'type': 'wasm', 'attributes': [{'key': '_contract_address', 'value': 'paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t'}, {'key': 'action', 'value': 'create_pair'}, {'key': 'pair', 'value': 'paloma19usnw37lvx8jm6wehqqk56lxxcjd807py5l3trhrv92zy2s7rxsqdp6gee-paloma1h8ch6gu7nrq4nk8gatn7wj0gnn0f4nhuqd3xj5elpjr4g5mvmpmq442wjj'}, {'key': '_contract_address', 'value': 'paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn'}, {'key': 'liquidity_token_addr', 'value': 'paloma1cm60qwjptgep3s6nke033cpe73d345zqls8talh8zcn09tdfv65qnu2h0s'}, {'key': '_contract_address', 'value': 'paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t'}, {'key': 'action', 'value': 'register'}, {'key': 'pair_contract_addr', 'value': 'paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn'}]}], events_by_type={'execute': {'_contract_address': ['paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t']}, 'instantiate': {'_contract_address': ['paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn', 'paloma1cm60qwjptgep3s6nke033cpe73d345zqls8talh8zcn09tdfv65qnu2h0s'], 'code_id': ['36', '2']}, 'message': {'action': ['/cosmwasm.wasm.v1.MsgExecuteContract'], 'module': ['wasm'], 'sender': ['paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8']}, 'reply': {'_contract_address': ['paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn', 'paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t']}, 'wasm': {'_contract_address': ['paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t', 'paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn', 'paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t'], 'action': ['create_pair', 'register'], 'pair': ['paloma19usnw37lvx8jm6wehqqk56lxxcjd807py5l3trhrv92zy2s7rxsqdp6gee-paloma1h8ch6gu7nrq4nk8gatn7wj0gnn0f4nhuqd3xj5elpjr4g5mvmpmq442wjj'], 'liquidity_token_addr': ['paloma1cm60qwjptgep3s6nke033cpe73d345zqls8talh8zcn09tdfv65qnu2h0s'], 'pair_contract_addr': ['paloma1y5qk468ch9k86nlm5ltqgasenvvm3n97vsqkpf8adwp73mzns08st8kwrn']}})], code=0, codespace='', info=None, data=None, timestamp=None)
"""

uvloop.install()
asyncio.run(main())
