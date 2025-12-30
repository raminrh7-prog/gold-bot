name: UpdateGoldPrice

on:
  schedule:
    - cron: "*/5 * * * *"  # هر ۵ دقیقه یکبار
  workflow_dispatch:

jobs:
  update_price:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run update_price
        run: python update_price.py
