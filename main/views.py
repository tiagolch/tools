from django.shortcuts import render
from .models import FormatJson, Regex
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import re
import json
import os


def home(request):
    return render(request, 'main/home.html')


def extract_code(request):
    regex_list = Regex.objects.all()
    context = {'regex_list': regex_list}

    if request.method == 'POST':
        regex_id = request.POST.get('regex')
        data = request.POST.get('data')

        regex = Regex.objects.get(id=int(regex_id))

        schema = re.compile(f"{regex.regex}")

        codes = schema.findall(data)

        result = ', '.join(f'"{code}"' for code in codes)

        context = {'result': result}
        return render(request, 'main/extract_code_result.html', context)

    return render(request, 'main/extract_code.html', context)


def format_json(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        json_string = texto_para_json(texto)
        nome_arquivo = request.POST.get('nome_arquivo')

        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'

        salvar_json_em_arquivo(json_string, nome_arquivo)

        FormatJson.objects.create(name=nome_arquivo, json=json_string)

        return render(request, 'main/json_download.html', {'nome_arquivo': nome_arquivo})
    return render(request, 'main/format_json.html')


def json_download(request, nome_arquivo):
    caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)

    try:
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'rb') as arquivo:
                resposta = HttpResponse(FileWrapper(
                    arquivo), content_type='application/force-download')
                resposta[
                    'Content-Disposition'] = f'attachment; filename={os.path.basename(caminho_arquivo)}'
                os.remove(caminho_arquivo)
                return resposta
        else:
            return HttpResponse('O arquivo não foi encontrado.', status=404)
    except Exception as e:
        return HttpResponse(f'Ocorreu um erro: {str(e)}', status=500)


def texto_para_json(texto):
    texto = texto.replace("'", '"')
    texto = texto.replace("True", "true")
    texto = texto.replace("False", "false")

    try:
        return json.loads(json.dumps(texto, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print('ERRROOOOOOOOOO')
        texto_corrigido = texto.replace("'", '"')
        return json.loads(texto_corrigido)


def salvar_json_em_arquivo(json_string, nome_arquivo='document'):

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(str(json_string))


def excluir_arquivo(nome_arquivo):
    try:
        os.remove(nome_arquivo)
    except Exception as e:
        print(f"Erro ao excluir o arquivo: {e}")
