import pytest
from matematica.Calculadora import soma,sub,multiplicacao,divisao,media_lista_valores
import numpy as np


@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1,v2)

@pytest.mark.op_simples

def test_sub_dois_valores_positivos():
    v1 = 10.0
    v2 = 5.0
    assert 5 == sub(v1,v2)

@pytest.mark.op_simples
def test_multiplica_dois_valores_positivos():
    v1 = 1.0
    v2 = 5.0
    assert 5 == multiplicacao(v1,v2)

@pytest.mark.op_simples
def test_divisao_dois_valores_positivos():
    v1 = 10.0
    v2 = 2.0
    assert 5 == divisao(v1,v2)

@pytest.mark.op_complex
def test_media_lista_positivos():
    assert 2.5 == media_lista_valores([1,2,3,4])


@pytest.mark.exercicio_1
def test_divisao_por_zero():
    v1 = 5
    v2 = 0
    assert np.inf == divisao(v1,v2)

@pytest.mark.exercicio_1
def test_ignorar_numero_se_nao_for_enviado_media():
    assert 0 == media_lista_valores([])

@pytest.mark.exercicio_1
def test_ignorar_se_nao_for_numerico_media():
    assert 2 == media_lista_valores([1,2,True,'a'])