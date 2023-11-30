# Run project

Create a virtual enviroment

    python3 -m venv morfy-search-venv

Use the virtual enviroment before created

    source morfy-search-venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Run project

    uvicorn main:app --host 127.0.0.1 --port 3003 --reload
