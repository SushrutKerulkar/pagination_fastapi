from fastapi import FastAPI
import json

app = FastAPI()


with open('posts.json') as f:
    data = json.load(f)

data_length = len(data)

@app.get('/')

def getName():
    return {'name': 'Welcome to pagination API'}



@app.get('/posts')


#page_size: how many posts do you want on the selected page number
def read_posts(page_num: int = 1, page_size: int = 10):
    start = (page_num - 1) * page_size
    end = start + page_size
    

    response = {
        "data": data[start:end],
        "total": data_length,
        "count": page_size,
        "pagination":{}
    }

    if end >= data_length:
        response['pagination']['next'] = None

        if page_num > 1:
            response['pagination']['previous'] = f"/posts?page_num={page_num-1}&page_size={page_size}"
        else:
            response['pagination']['previous'] = None
    else:
        if page_num > 1:
            response['pagination']['previous'] = f"/posts?page_num={page_num-1}&page_size={page_size}"
        else:
            response['pagination']['previous'] = None
        
        response['pagination']['next'] = f"/posts?page_num={page_num+1}&page_size={page_size}"
    
    return response






