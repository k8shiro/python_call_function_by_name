# python_call_function_by_name
pythonで関数名をstringで渡して実行させるサンプル。


- 実行方法

```
docker run -v $(pwd)/samples:/samples  --rm python:3.9 python /samples/use_eval.py
docker run -v $(pwd)/samples:/samples  --rm python:3.10 python /samples/use_eval.py
```

※ @staticmethodの動作がpythonのバージョンで微妙に違う
