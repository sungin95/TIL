# 에러/예외 처리(Error/Exception Handling)



[예외 계층 구조](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

# 예외 처리



```python
# 파일이 없는 경우
try:
	f = open('nooofile.txt')
except FileNotFoundError:
	print('해당 파일이 없습니다.')
else:
	print('파일을 읽기 시작합니다.')
	print(f.read())
	print('파일을 모두 읽었습니다.')
	f.close()
finally:
	print('파일 읽기를 종료합니다.')
```





# 예외 발생 시키기

raise <표현식>(메시지)

```raise```

우리가 하는 에러가 raise를 통해 만들어 졌다. 



