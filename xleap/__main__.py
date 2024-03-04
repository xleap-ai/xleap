import json

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command(help="hello world!! information about the package")
def hello():
    print("hello there")


@app.command(help="run evaluation on sample data")
def run_evaluation():
    import pandas as pd
    from rich.table import Table

    from xleap.metrics.base import prompt_length, response_length, response_space_count
    from xleap.metrics.common import ItemResult
    from xleap.metrics.evaluate import evaluate
    from xleap.metrics.scores import (
        # PromptSentiment,
        # PromptToxicity,
        # ResponseSentiment,
        # ResponseToxicity,
        text_stat_metrics,
    )

    df = pd.read_csv("./data.csv", index_col=0)

    df.rename(columns={"question": "prompt", "answer": "response"}, inplace=True)
    df: pd.DataFrame = df.loc[range(0, 100)]
    metrics = [
        prompt_length,
        # PromptSentiment(batch_size=12),
        # ResponseSentiment(batch_size=12),
        # PromptToxicity(batch_size=12),
        # ResponseToxicity(batch_size=12),
    ] + text_stat_metrics

    evaluate(df, metrics)

    evaluate(df, [prompt_length, response_space_count])
    evaluate(df, [prompt_length, response_length])
    evaluate(df, [prompt_length])
    # evaluate(df, [prompt_length] + metrics, force=True)
    evaluate(df, [prompt_length, response_space_count])
    evaluate(df, [prompt_length])
    evaluate(
        df, [prompt_length, response_length, response_space_count, response_length]
    )

    table = Table("Name", "Values")
    for k, v in df.items():
        v: list[ItemResult]
        table.add_row(k, ", ".join([str(ItemResult(*i).value) for i in v]))

    print(table)


@app.command(
    help="run analytics server to start capturing events from a web application"
)
def analytics(run_server: bool = False):
    print(run_server)
    if run_server:
        import uvicorn

        from xleap.analytics import serve

        uvicorn.run(app=serve.app)


@app.command()
def on_gpt():
    def build_data():
        # global all_data
        from xleap.parser import all_data, onload

        with open("cli/json-data.json") as fff:
            json_data = json.load(fff)
            onload(json_data, range(100, 120))

        with open("datalist.json", "w") as gg:
            gg.write(json.dumps(all_data, indent=1))

        print(len(all_data))

    build_data()
    # return

    from xleap.analytics.config import API_KEY, BASE_URL, DEFAULT_MODEL
    from xleap.analytics.prompt import SYSTEM_PROMPT
    from xleap.chat import ChatInterface

    with open("datalist.json") as gg:
        data: list[str] = json.load(gg)

    chat = []
    for i in data:
        ins = ChatInterface(
            id=i,
            model=DEFAULT_MODEL,
            system_prompt=SYSTEM_PROMPT,
            api_key=API_KEY,
            base_url=BASE_URL,
        )

        if i.startswith("## "):
            if len(chat) > 0:
                ins.append({"role": "user", "content": "\n".join(chat)})
                ins.dump()
            chat = []

        if i.startswith("### user"):
            chat.append(i[9:])
    print(chat)
    if len(chat) > 0:
        ins.append({"role": "user", "content": "\n".join(chat)})
        ins.dump()


@app.command()
def show_data():
    import os

    from xleap.utils.format import format

    m = []

    def read_files(base_path):
        files = os.listdir(base_path)
        for filename in files:
            if not filename.endswith(".json"):
                print(filename)
                continue
            with open(os.path.join(base_path, filename)) as r:
                chat_messages = json.loads(r.read())
                for chat_message in chat_messages[1:]:
                    model, session = filename.split("##")
                    m.append(
                        {
                            "model": model,
                            "session": session,
                            "role": chat_message["role"],
                            "content": chat_message["content"],
                        }
                    )

    read_files("conversations")
    # read_files("chats")

    newArr = []
    for i, j in zip(m[0::2], m[1::2]):
        print(i["session"] == j["session"], i["role"])

        newArr.append({**i, "agent_Reply": format(j["content"])})

    with open("abccc.json", "w") as rr:
        rr.write(json.dumps(m, indent=2))
    import pandas as pd

    df = pd.DataFrame.from_records(newArr)

    df.to_excel("output-format.xlsx")


if __name__ == "__main__":
    app()
