## Copyright 2025 rbao2018. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import time
from typing import Any, Dict, Optional


from okx.Grid import GridAPI
from okx.Trade import TradeAPI


def init_api_keys():
    api_key = os.getenv("OKX_READ_AK")
    secret_key = os.getenv("OKX_READ_SK")
    passphrase = os.getenv("OKX_READ_PASS")
    FLAG_REAL_OR_PAPER = "0"  # 实盘: 0 , 模拟盘：1

    return api_key, secret_key, passphrase, FLAG_REAL_OR_PAPER

# def fetch_recent_spot_orders(days: int = 30, limit: int = 100) -> Optional[Dict[str, Any]]:
#     """Fetch recent spot orders within the last `days` using OKX Trade API.

#     Returns the raw response dict on success, or None on failure.
#     """

#     api_key, secret_key, passphrase, FLAG_REAL_OR_PAPER = init_api_keys()

#     trade_api = TradeAPI(
#         api_key=api_key,
#         api_secret_key=secret_key,
#         passphrase=passphrase,
#         use_server_time=False,
#         flag=FLAG_REAL_OR_PAPER,
#     )

#     # 计算最近 `days` 天的时间戳（毫秒级）
#     end_time_ms = int(time.time() * 1000)
#     begin_time_ms = end_time_ms - days * 24 * 60 * 60 * 1000

#     try:
#         # 调用历史订单查询接口（3个月内）
#         response = trade_api.get_orders_history_archive(
#             instType="SPOT",  # 可改为 "FUTURES"、"SWAP" 等
#             ordType="post_only,fok,ioc",
#             begin=str(begin_time_ms),
#             end=str(end_time_ms),
#             limit=str(limit),  # OKX SDK 接口期望字符串
#         )
#         return response
#     except Exception as error:  # noqa: BLE001 - 外部 SDK 可能抛出任意异常
#         print("查询失败：", error)
#         return None

def get_grid_trigger_orders():
    api_key, secret_key, passphrase, FLAG_REAL_OR_PAPER = init_api_keys()

    grid_api = GridAPI(
        api_key=api_key,
        api_secret_key=secret_key,
        passphrase=passphrase,
        use_server_time=False,
        flag=FLAG_REAL_OR_PAPER,
    )

    # 查询未完成的条件单（ordType="conditional"）
    response = grid_api.grid_orders_algo_history(
        algoOrdType="grid"
    )
    
    return response
    

def main() -> None:
    # 获取未完成的算法条件单
    response = get_grid_trigger_orders()
    print(response)


if __name__ == "__main__":
    main()