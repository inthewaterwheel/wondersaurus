### Instructions for running the API server

- Unzip `dict.json.zip` and `webster_or_100k_filtered_w2v.bin.zip` in the `data/` subdirectory
- `cd api_server`
- Install requirements `pip install -r requirements.txt`
- Run `python3 app.py`

Using the API server:
Postman is probably your best call, but CURL should work in a pinch.
It expects a `POST` request to `http://127.0.0.1:5000/neighbors` with json body of form:
`{"pos_words":{"hello": 1, "bye": 1}, "neg_words":{"no": 0.1}}`

### Other notes:

- `app.py` might break because it expects some files that are missing, there's instructions in it re: commenting those out for now though

- If you want to regenerate the `w2v.bin` file with different conditions, `filter_w2v.py` is your friend, it'll need you to download the full `w2v` and point to it though.

- The `dict.json` was generated using `WebsterParser` - which you should be able to find by googling it. 