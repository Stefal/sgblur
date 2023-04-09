from fastapi import FastAPI, UploadFile, Response
import gc
from .blur import blur

app = FastAPI()
print("API is preparing to start...")


@app.get("/")
async def root():
	return {"message": "GeoVisio 'Speedy Gonzales' Blurring API"}


@app.post(
	"/blur/",
	responses = {200: {"content": {"image/jpeg": {}}}},
	response_class=Response
)
async def blur_picture(picture: UploadFile):
	blurredPic = blur.blurPicture(picture)

	# For some reason garbage collection does not run automatically after
	# a call to an AI model, so it must be done explicitely
	gc.collect()

	return Response(content=blurredPic, media_type="image/jpeg")