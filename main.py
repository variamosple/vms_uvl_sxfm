from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import re

from src.arbol import generate_json, parse_uvl_content
from src.sxfm_uvl import sxfm_to_uvl

app = FastAPI()


# Simulación de las funciones que transforman UVL a JSON y SXFM a UVL, y luego a JSON
def uvl_to_json(input_data):
    # Simulación de conversión de UVL a JSON
    elements, relationships = parse_uvl_content(input_data)
    json_data = generate_json(elements, relationships)
    return json_data


def sxfm_uvl(sxfm_data):
    # Simulación de conversión de SXFM a UVL
    uvl_content = sxfm_to_uvl(sxfm_data)
    elements, relationships = parse_uvl_content(uvl_content)
    json_data = generate_json(elements, relationships)
    return json_data


@app.post("/process-file")
async def process_file(file: UploadFile = File(...)):
    content = await file.read()
    # Decodificar si es necesario, dependiendo de cómo se manejen los datos
    content = content.decode('utf-8')

    # Determinar si el contenido es UVL o SXFM
    if file.filename.endswith('.uvl'):
        json_data = uvl_to_json(content)
        return JSONResponse(content=json_data)
    elif file.filename.endswith('.sxfm'):
        uvl_content = sxfm_uvl(content)
        json_data = uvl_to_json(uvl_content)
        return JSONResponse(content=json_data)
    elif file.filename.endswith('.json'):
        return JSONResponse(content=content)
    else:
        return {"error": "Unsupported file format"}

