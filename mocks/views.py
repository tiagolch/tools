from django.shortcuts import render

from ninja import NinjaAPI

mock = NinjaAPI()

data_json = [

    {
        "id": 530857789,
        "operacao": {
            "id": 531968406,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857817,
        "operacao": {
            "id": 531968434,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857838,
        "operacao": {
            "id": 531968455,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857868,
        "operacao": {
            "id": 531968485,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857905,
        "operacao": {
            "id": 531968522,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857932,
        "operacao": {
            "id": 531968549,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857958,
        "operacao": {
            "id": 531968575,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530857984,
        "operacao": {
            "id": 531968601,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858011,
        "operacao": {
            "id": 531968628,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858039,
        "operacao": {
            "id": 531968656,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858066,
        "operacao": {
            "id": 531968683,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858093,
        "operacao": {
            "id": 531968710,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858119,
        "operacao": {
            "id": 531968736,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-06",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858162,
        "operacao": {
            "id": 531968779,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858188,
        "operacao": {
            "id": 531968805,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858220,
        "operacao": {
            "id": 531968838,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858246,
        "operacao": {
            "id": 531968865,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858275,
        "operacao": {
            "id": 531968895,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858303,
        "operacao": {
            "id": 531968923,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858340,
        "operacao": {
            "id": 531968960,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858412,
        "operacao": {
            "id": 531969022,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858778,
        "operacao": {
            "id": 531969389,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-07",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530858921,
        "operacao": {
            "id": 531969582,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-08",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859581,
        "operacao": {
            "id": 531970648,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-12",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859609,
        "operacao": {
            "id": 531970676,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-12",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859639,
        "operacao": {
            "id": 531970706,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-12",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859811,
        "operacao": {
            "id": 531970853,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-13",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859928,
        "operacao": {
            "id": 531970952,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-14",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859958,
        "operacao": {
            "id": 531970983,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-14",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530859988,
        "operacao": {
            "id": 531971014,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-14",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530860035,
        "operacao": {
            "id": 531971061,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-15",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530860083,
        "operacao": {
            "id": 531971107,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-15",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530860170,
        "operacao": {
            "id": 531971194,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-16",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530860283,
        "operacao": {
            "id": 531971358,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-16",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530860430,
        "operacao": {
            "id": 531971505,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-19",
            "status": 0,
            "descricao": ""
        }
    },
    {
        "id": 530860463,
        "operacao": {
            "id": 531971538,
            "tipo": "cte",
            "instrucao": "emitir",
            "data": "2024-02-19",
            "status": 0,
            "descricao": ""
        }
    }
]


@mock.get("/v1/tarifas/pendentes")
def get_data(request):
    return data_json
