# Windows11 使用WSL搭建 DeepSeek模型(本地部署 vLLM + DeepSeek-Coder-1.3B 实践总结)

## 配置


* **显卡**：RTX 3060（12GB 显存）
* **内存**：16GB
* **操作系统**：Windows（建议用 WSL2 + Ubuntu）
* **用途**：私有 Agent、SQL 智能查询、代码生成、问答系统等

✅ **推荐模型（适配 12GB 显存）：**

| 模型                    | 说明                                     |
| --------------------- | -------------------------------------- |
| `deepseek-coder-1.3B` | 高质量代码生成模型，中文支持好                        |
| `TinyLlama-1.1B`      | 通用对话模型，显存要求低                           |
| `Qwen1.5-0.5B-Chat`   | 阿里的中文能力优秀的小模型                          |
| `Mistral-7B`          | 可尝试，使用 `int4` 量化（QLoRA）可以压缩到 8GB 显存内运行 |

❗**不建议部署：** llama2-13B, deepseek-33B, chatglm3-6B，除非你用远程 A100 服务器

## 步骤

1. 升级 WSL : `wsl.exe --update`

2. Ubuntu 替换 apt 镜像源 
    
    ```bash
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
    sudo nano /etc/apt/sources.list
    ```

    将所有 `http://archive.ubuntu.com/ubuntu` 和 `http://security.ubuntu.com/ubuntu` 替换为：`http://mirrors.aliyun.com/ubuntu/    `

    然后 `sudo apt update`

3. 配置国内 PyPI 镜像源
 
    ```bash
    mkdir -p ~/.pip
    nano ~/.pip/pip.conf
    ```
    
    然后粘贴以下内容（以清华源为例）：

    ```ini
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    ```
    
    保存后按 `Ctrl + O` 保存，`Ctrl + X` 退出。

4. 为 WSL Ubuntu 22.04 添加 NVIDIA CUDA APT 源并安装 `cuda-toolkit-12-3`

    ```bash
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
    sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600

    sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub

    sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"

    sudo apt update
    sudo apt install -y cuda-toolkit-12-3
    ```

    防止报错：`ImportError: libcudart.so.12: cannot open shared object file: No such file or directory`

5. 理论上安装这个就行 `pip install "vllm[torch]==0.4.0" --extra-index-url https://download.pytorch.org/whl/cu118`，实际上我走了以下几步路
   
    4.1 安装以下

    `pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118`

    校验：

    报错 Killed：
    
    ```bash
    # 报Killed错误添加参数 --no-cache-dir
    sudo pip install --no-cache-dir torch==2.1.2+cu118 torchvision==0.16.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118 
    # 或着 下载到本地 
    wget https://download.pytorch.org/whl/cu118/torch-2.1.2%2Bcu118-cp310-cp310-linux_x86_64.whl
    wget https://download.pytorch.org/whl/cu118/torchvision-0.16.2%2Bcu118-cp310-cp310-linux_x86_64.whl
    ```


    ```bash
    python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
    ```
   
    检查是否输出如下：

    ```graphql
    2.1.2+cu118
    True
    ```

   > 我遇到的问题： `A module that was compiled using NumPy 1.x cannot be run in NumPy 2.2.6 as it may crash... Failed to initialize NumPy: _ARRAY_API not found`

    降低版本就好了 `pip install --upgrade numpy==1.25.2`

    4.2 安装 vLLM

    `pip install "vllm[torch]==0.4.0" --extra-index-url https://download.pytorch.org/whl/cu118`

    测试 vLLM（是否 GPU 启用）

    ```bash
    python3 -c "from vllm import LLM; llm = LLM(model='facebook/opt-125m'); print('OK')"
    ```

    补充一下需要下载本地模型：
    gpt 推荐这个 `huggingface-cli download deepseek-ai/deepseek-coder-1.3b-instruct --local-dir ./models/deepseek` 访问不到。使用了一个 `modelscope`

    ```bash
    pip install modelscope

    modelscope download --model deepseek-ai/deepseek-coder-1.3b-instruct --local_dir ./   # 下载到当前文件夹 modelscope download --model TheBloke/deepseek-coder-6.7B-base-GPTQ --local_dir ./
    # 废话一下后面这个是量化模型 使用GPU内存小
    ln -s /d/models/deepseek-coder-1.3b-instruct /d/models/deepseek  # 为了简化调用，建立软链接
    ```

    修改校验部分，加载本地模型：
    
    ```bash
    python3 -c "from vllm import LLM; llm = LLM(model='/d/models/deepseek'); print('OK')"
    ```

    报错：`ValueError: The model's max seq len (65536) is larger than the maximum number of tokens that can be stored in KV cache (26816). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.`

    默认使用了 vLLM 的 max_seq_len=65536，但是 GPU（RTX 3060，12GB）不够用来缓存这么多 token.

    ```bash
    python3 -c "from vllm import LLM; llm = LLM(model='/d/models/deepseek', max_model_len=2048); print('OK')"
    ```

6. 搭建服务

    ```bash
    python3 -m vllm.entrypoints.openai.api_server   --model /d/models/deepseek --served-model-name deepseek   --host 0.0.0.0   --port 8800   --max-model-len 2048
    ```

    测试：

    ```bash
    curl http://localhost:8800/v1/completions -H "Content-Type: application/json" -d '{"model":"deepseek", "prompt":"用Python写一个快速排序算法.", "max_tokens":500 }'
    ```

    ```cmd
    curl "http://localhost:8800/v1/completions" -H "Content-Type: application/json"   -d "{ \"model\": \"deepseek\", \"prompt\": \"用Python写一个快速排序算法。\", \"max_tokens\": 500 }"
    ```

    返回

    ```json
    {"id":"cmpl-984ad3d429ec4e4caf47425b9968b16d","object":"text_completion","created":1751968456,"model":"deepseek","choices":[{"index":0,"text":"\n\n  \n  快速排序是一种广泛使用的排序算法，它比其他一些算法（如归并排序）更高效。它的平均情况下的时间复杂度为O(n log n)。\n  \n  快速排序算法的步骤如下 ：\n\n  1. 从数组中选择一个元素作为基准，并根据它将其他元素分成两个子数组，根据它们与基准的大小关系进行划分。\n  \n  2. 对子数组递归地应用上述步骤。\n  \n  3. 此时，基准元素所在的位置和所有小于基准元素的元素和所有大于基准元素的元素都已被排序，只需交替进行。\n  \n  下面是Python中快速排序的代码实 现：\n\"\"\"\n\ndef quicksort(lst):\n    if len(lst) <= 1:\n        return lst\n    else:\n        pivot = lst[0]\n        less_than_pivot = [x for x in lst[1:] if x <= pivot]\n        greater_than_pivot = [x for x in lst[1:] if x > pivot]\n        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)\n\nprint(quicksort([3,6,8,10,1,2,1]))\n# 输出结果: [1, 1, 2, 3, 6, 8, 10]\n```\n\n这个实现非常容易实现，但对于已排序或 几乎已排序的输入，需要进行很多不必要的排序操作。因此，如果算法适用于已排序的输入，应优先使用快速排序而不是其他算法。\n","logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":11,"total_tokens":435,"completion_tokens":424}}
    ```
    




    
