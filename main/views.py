from django.shortcuts import render
from .models import FormatJson, Regex
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import re
import json
import os
import pandas as pd
from django.db import connections
from datetime import datetime, timedelta


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
        response, nome_arquivo = execute_sql_and_export_csv(result)
        context = {'result': result, 'nome_arquivo': nome_arquivo}

        return render(request, 'main/extract_code_result.html', context)

    return render(request, 'main/extract_code.html', context)


def download(request, nome_arquivo):
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


def query(awbs):
    data_hoje = datetime.now()
    data_hoje_menos_30_dias = data_hoje - timedelta(days=30)
    data_formatada = data_hoje_menos_30_dias.strftime('%Y-%m-%d')

    sql = f"""
    Select
    cte.fatctestat_id as 'Cod Status',
    status.fatctestat_nome 'Status',
    rem.doc_fiscal_cte as 'Cod CTe_Tipo no cad Rem',
    CASE
        when rem.doc_fiscal_cte = 0 then 'normal'
        when rem.doc_fiscal_cte = 1 then 'subcontratação'
        when rem.doc_fiscal_cte = 2 then 'redespacho'
        when rem.doc_fiscal_cte = 3 then 'subcontratação com remetente originário'
        when rem.doc_fiscal_cte = 4 then 'redespacho intermediário'
        when rem.doc_fiscal_cte = 5 then 'operação consolidada'
    END as 'CTe_Tipo no cad Rem',
    CASE
        when cte.fatcte_tipo_cte = 0 then 'Normal'
        when cte.fatcte_tipo_cte = 1 then 'Complemento'
        when cte.fatcte_tipo_cte = 1 then 'Anulação'
        when cte.fatcte_tipo_cte = 3 then 'Substituição'
    END as TipoCte,
    cte.fatcte_tipo_servico as 'Cod Tipo Servico',
    CASE
        when cte.fatcte_tipo_servico = 0 then 'normal'
        when cte.fatcte_tipo_servico = 1 then 'subcontratação'
        when cte.fatcte_tipo_servico = 2 then 'redespacho'
        when cte.fatcte_tipo_servico = 3 then 'subcontratação com remetente originário'
        when cte.fatcte_tipo_servico = 4 then 'redespacho intermediário'
        when cte.fatcte_tipo_servico = 5 then 'operação consolidada'
    END as 'Tipo de Servico',
    CASE
        when cte.fatcte_modal = '01' then 'Rodoviário'
        when cte.fatcte_modal = '02' then 'Aéreo'
        when cte.fatcte_modal = '03' then 'Aquaviário'
        when cte.fatcte_modal = '04' then 'Ferroviário'
        when cte.fatcte_modal = '05' then 'Dutoviário'
        when cte.fatcte_modal = '06' then 'Multimodal'
    END as 'Modal',
    rem.ramo_atividade,
    rem.fat_contribuinte,
    CASE
       when rem.fat_contribuinte = 1 then 'SIM'
       when rem.fat_contribuinte = 0 then 'NAO'
    END as 'Contribuinte ICMS',
    cte.encoid, cte.reid, awb,
    fatcte_chave_origem as 'Chave Origem',
    fatcte_chave_acesso as 'Chave acesso CTE',
    cte.fatcte_classificacao_tributaria as 'Cod Classificacao Tributaria',
    fatcte_cfop as 'CFOP',
    fatcte_natureza_operacao as 'Natureza Operacao',
    cte.fatcte_codigo_numerico as 'Codigo Numerico',
    cte.fatcte_serie as 'Serie',
    cte.fatcte_data as 'Data',
    cte.fatcte_hora as Hora,
    cte.fatcte_municipio_envio as 'Municipio Envio',
    cte.fatcte_municipio_inicio as 'Municipio Inicio',
    cte.fatcte_uf_inicio as 'UF Inicio',
    cte.fatcte_uf_envio as 'UF Envio',
    cte.fatcte_municipio_fim as 'Municipio Fim',
    cte.fatcte_uf_fim as 'UF Fim',
    cte.fatcte_frete_peso as 'Frete Peso',
    cte.fatcte_frete_valor as 'Frete Valor',
    cte.fatcte_outros as Outros,
    cte.fatcte_total_prestacao as 'Total Prestacao',
    cte.fatcte_classificacao_tributaria as 'Classificacao Tributaria',
    cte.fatcte_base_calculo as 'Base Calculo',
    cte.fatcte_aliquota as Aliquota,
    cte.fatcte_valor_icms as 'Valor ICMS',
    cte.fatcte_valor_mercadoria as 'Valor Mercadoria',
    cte.fatcte_natureza as Natureza,
    cte.fatcte_peso as Peso,
    cte.fatcte_cubagem as Cubagem,
    cte.fatcte_observacoes as 'Observacoes',
    imp.fatctetribimp_obs as 'Descricao Documento IDT',
    cte.fatcte_data_cancelamento as 'Data Cancelamento',
    cte.fatcte_isencao_icms as 'Isencao ICMS',
    cte.fatcte_emitente_cnpj as 'Emitente CNPJ',
    cte.fatcte_emitente_nome as 'Emitente Nome',
    cte.fatcte_emitente_fantasia as 'Emitente Fantasia',
    cte.fatcte_emitente_municipio as 'Emitente Municipio',
    cte.fatcte_emitente_uf as 'Emitente UF',
    cte.fatcte_remetente_cnpj as 'Remetente CNPJ',
    cte.fatcte_remetente_nome as 'Remetente Nome',
    cte.fatcte_remetente_fantasia as 'Remetente Fantasia',
    cte.fatcte_remetente_municipio as 'Remetente Municipio',
    cte.fatcte_remetente_uf as 'Remetente UF',
    cte.fatcte_destinatario_cnpj as 'Destinatario CNPJ',
    cte.fatcte_destinatario_cpf as 'Destinatario CPF',
    cte.fatcte_destinatario_nome as 'Destinatario Nome',
    cte.fatcte_destinatario_suframa as 'Destinatario Suframa',
    cte.fatcte_destinatario_end_bairro as 'Destinatario End Bairro',
    cte.fatcte_destinatario_municipio as 'Destinatario Municipio',
    cte.fatcte_destinatario_uf as 'Destinatario UF',
    cte.fatcte_tomador_servico as 'Tomador Servico',
    cte.fatcte_tomador_cnpj as 'Tomador CNPJ',
    cte.fatcte_tomador_cpf as 'Tomador CPF',
    cte.fatcte_tomador_ie as 'Tomador IE',
    cte.fatcte_tomador_nome as 'Tomador Nome',
    cte.fatcte_tomador_fantasia as 'Tomador Fantasia',
    cte.fatcte_tomador_municipio as 'Tomador Municipio',
    cte.fatcte_tomador_uf as 'Tomador UF'
# Select count(*), awb
From corrier_fat.fat_cte cte
    inner join corrier.encomendas e using(encoid)
    inner join corrier_fat.fat_cte_tributos cteTrib using (fatcte_id)
    inner join corrier_fat.fat_cte_tributos_complemento cteComp using (fatctetrib_id)
    inner join corrier.remetentes rem on e.reid = rem.reid
    inner join corrier_fat.fat_cte_tributos_impostos imp using (fatctetrib_id)
    inner join corrier_fat.fat_cte_status status using (fatctestat_id)
where 1=1
	and awb in ({awbs})
    and cteComp.fatctetribcom_motorfiscal = 'IDT'
    and imp.fatctetribimp_imposto = 'ICMS'
    and cte.fatcte_data >= {str(data_formatada)}     
order by awb
"""
    return sql


def execute_sql_and_export_csv(awbs):
    sql_query = query(awbs)
    try:
        with connections['external_database'].cursor() as cursor:
            cursor.execute(sql_query)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

        df = pd.DataFrame(data, columns=columns)

        csv_filename = f'{datetime.today()}.csv'
        df.to_csv(csv_filename, index=False)

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f'attachment; filename="{csv_filename}"'
        df.to_csv(response, index=False)
    except Exception as e:
        print(str(e))
        raise str(e)
    return response, csv_filename


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
