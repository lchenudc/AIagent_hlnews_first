# README.md


## 🧠 What is MCP?

> From ["MCP Python SDK"](https://pypi.org/project/mcp/):
>
> **The Model Context Protocol (MCP)** lets you build AI servers that securely expose data and functionality to LLM applications — similar to a web API, but specifically designed for LLM interactions.

MCP servers can:
- 📄 Expose **data** through *Resources* (like GET endpoints).
- 🛠️ Provide **functionality** through *Tools* (like POST endpoints).
- ✍️ Define reusable prompt templates through *Prompts*.
- 🔌 And more!

---

## ⚙️ Method 1: Basic Python (No `uv`)

### 🧪 Step-by-Step

**Step 1: Create your project folder**

```bash
mkdir AIagent_hlnews_first
cd AIagent_hlnews_first
```

Copy or create your files here. For example:

- `client3.py`
- `server_headlinenews.py`

---

**Step 2: Launch the server**

```bash
python3 server_headlinenews.py  
```
(Note: Depending on your computer’s setup, the Python command might be python instead of python3. Use whichever command 
runs Python 3.x on your system.)


✅ If successful, you’ll see something like:  
`🚀 HeadlineNews MCP Server running via stdio…`

> You can also try:
```bash
mcp dev server_headlinenews.py
```

---

**Step 3: Run the client**

```bash
python3 client3.py
```

✅ This will start the client, which may also auto-launch the server depending on how it’s coded.

> Alternate:
```bash
mcp dev client
```

---

### 🛠 Notes

1. **Use virtual environments (recommended):**

```bash
python -m venv .venv
source .venv/bin/activate
```

2. **Install MCP and LangChain (if needed):**

```bash
pip install mcp
pip install langchain langchain-mcp-adapters langgraph
```

3. **Install dependencies (if using a `requirements.txt`):**

```bash
pip install -r requirements.txt
```

4. **API Keys**

If you need access to external APIs like NewsAPI or OpenAI:

Create a `.env` file:
```env
NEWSAPI_KEY=your_api_key
OPENAI_API_KEY=your_openai_key
```

Or set the key directly:
```python
NEWSAPI_KEY = "your_key_here"
```

---

## 🚀 Method 2: Using `uv` (Optional but Powerful)

[`uv`](https://github.com/astral-sh/uv) is a **fast Python package and project manager** written in Rust.

---

**Step 1: Create your project**

```bash
uv init AIagent_hlnews_simple
cd AIagent_hlnews_simple
```

Then copy or create your files: `client3.py`, `server_headlinenews.py`

---

**Step 2: Add MCP dependency**

```bash
uv add "mcp[cli]"
```

(Or if you're using pip: `pip install "mcp[cli]"`)

---

**Step 3: Run your MCP app**

```bash
uv run mcp
```

Or just run:
```bash
uv venv exec python client3.py
```

---

**Step 4: Run dev server**

```bash
uv run mcp dev server_headlinenews.py
```

🧠 This will start your MCP server in dev mode. MCP may also prompt to install a browser-based inspector.

---

**Step 5: Run your client**

```bash
uv venv exec python client3.py
```

---

## ✅ Summary

| Task                  | With Python             | With UV                    |
|-----------------------|-------------------------|----------------------------|
| Create project        | `mkdir my_project`      | `uv init my_project`       |
| Add dependencies      | `pip install ...`       | `uv add ...`               |
| Run server            | `python server.py`      | `uv run mcp dev server.py` |
| Run client            | `python client.py`      | `uv run mcp` or `uv exec`  |
| Virtual environment   | `python -m venv .venv`  | handled by `uv`            |

---

## 📜 License

MIT License – Feel free to adapt or reuse.


## Acknowledgment
This small code sample project was built with support and assistance from ChatGPT.




## Appendix about MIT License

Copyright (c) 2025 Thu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

