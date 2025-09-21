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
import okx.Account as Account

def print_recursive(obj, indent=0, is_list_item=False):
    """
    递归打印字典或列表，处理嵌套结构并显示层级关系
    
    参数:
        obj: 要打印的对象（可以是字典、列表、字符串、数字等）
        indent: 缩进空格数，用于显示层级
        is_list_item: 是否为列表中的元素，用于调整输出格式
    """
    # 定义缩进字符串
    indent_str = '  ' * indent
    
    # 如果是字典类型
    if isinstance(obj, dict):
        # 列表元素中的字典需要特殊处理前缀
        prefix = '' if is_list_item else indent_str
        print(f"{prefix}{{")
        
        # 遍历字典键值对
        for key, value in obj.items():
            print(f"{indent_str}  {key}: ", end='')
            # 递归处理值
            print_recursive(value, indent + 1)
        
        print(f"{indent_str}}}")
    
    # 如果是列表类型
    elif isinstance(obj, list):
        prefix = '' if is_list_item else indent_str
        print(f"{prefix}[")
        
        # 遍历列表元素
        for i, item in enumerate(obj):
            print(f"{indent_str}  [{i}]: ", end='')
            # 递归处理列表项，标记为列表元素
            print_recursive(item, indent + 1, is_list_item=True)
        
        print(f"{indent_str}]")
    
    # 其他基本类型
    else:
        print(obj)


if __name__ == "__main__":
    flag = "0" # 实盘:0 , 模拟盘：1

    api_key = os.getenv("OKX_READ_AK", None)
    secret_key = os.getenv("OKX_READ_SK", None)
    passphrase = os.getenv("OKX_READ_PASS", None)

    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)

    result = accountAPI.get_account_balance()
    