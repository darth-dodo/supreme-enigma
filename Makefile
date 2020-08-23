make helloworld:
	uvicorn hello_world:app --reload

make server:
	uvicorn main:app --reload --h=0.0.0.0
