from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.responses import Response
import re
import json

from src.arbol import generate_json, parse_uvl_content
from src.sxfm_uvl import sxfm_to_uvl

app = FastAPI()


# Simulación de las funciones que transforman UVL a JSON y SXFM a UVL, y luego a JSON
def uvl_to_json(input_data):
    # Simulación de conversión de UVL a JSON
    elements, relationships = parse_uvl_content(input_data)
    json_data = generate_json(elements, relationships)
    print(json_data)
    return json_data


def sxfm_uvl(sxfm_data):
    # Simulación de conversión de SXFM a UVL
    uvl_content = sxfm_to_uvl(sxfm_data)
    return uvl_to_json(uvl_content)


@app.post("/process-file")
async def process_file(file: UploadFile = File(...)):
    content = await file.read()
    # Decodificar si es necesario, dependiendo de cómo se manejen los datos
    content = content.decode('utf-8')
    # Determinar si el contenido es UVL o SXFM
    if file.filename.endswith('.uvl'):
        json_data = uvl_to_json(content)
        return Response(content=json_data, media_type="application/json")
    elif file.filename.endswith('.xml'):
        json_data = sxfm_uvl(content)
        return Response(content=json_data, media_type="application/json")
    elif file.filename.endswith('.json'):
        return Response(content=content, media_type="application/json")
    else:
        return {"error": "Unsupported file format"}

