make helloworld:
	uvicorn hello_world:app --reload

make server:
	uvicorn main:app --reload