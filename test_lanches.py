import pytest 

from lanches import Lanches

@pytest.fixture
def lanche_fila_vazia():
    return Lanches("Big Burger")

@pytest.fixture
def lanche_fila_com_um_pedido():
    return Lanches("Big Burger", 1)

@pytest.fixture
def lanche_fila_vazia_de_entrega():
    return Lanches("Big Burger")

@pytest.fixture
def lanche_fila_com_um_pedido_de_entrega ():
    return Lanches("Big Burger", 1)

def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero(lanche_fila_vazia):
    assert lanche_fila_vazia.pedidos_na_fila == 0
    
def test_pedidos_na_fila_valor_inicial_maior_que_zero(lanche_fila_com_um_pedido):
    assert lanche_fila_com_um_pedido.pedidos_na_fila == 1
  
def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Lanches("Big Burger", -1)

def test_adicionar_pedido_na_fila(lanche_fila_com_um_pedido):
    lanche_fila_com_um_pedido.adiciona_pedido()
    assert lanche_fila_com_um_pedido.pedidos_na_fila == 2

def test_remover_pedido_na_fila(lanche_fila_com_um_pedido):
    lanche_fila_com_um_pedido.remove_pedido()
    assert lanche_fila_com_um_pedido.pedidos_na_fila == 0

def test_remover_pedido_na_fila_vazia(lanche_fila_vazia):
    lanche_fila_vazia.remove_pedido()
    assert lanche_fila_vazia.pedidos_na_fila == 0

def test_pedidos_na_fila_de_entrega_valor_inicial_padrao_igual_a_zero(lanche_fila_vazia_de_entrega):
    assert lanche_fila_vazia_de_entrega.pedidos_na_fila_de_entrega == 0
    
def test_pedidos_na_fila_de_entrega_valor_inicial_maior_que_zero(lanche_fila_com_um_pedido_de_entrega):
    assert lanche_fila_com_um_pedido_de_entrega.pedidos_na_fila_de_entrega == 1
  
def test_pedidos_na_fila_de_entrega_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Lanches("Big Burger", -1)
        
def test_adicionar_pedido_na_fila_de_entrega(lanche_fila_com_um_pedido_de_entrega):
    lanche_fila_com_um_pedido_de_entrega.adiciona_pedido_entrega()
    assert lanche_fila_com_um_pedido_de_entrega.pedidos_na_fila_de_entrega == 2

def test_remover_pedido_na_fila_de_entrega(lanche_fila_com_um_pedido_de_entrega):
    lanche_fila_com_um_pedido_de_entrega.remove_pedido_entrega()
    assert lanche_fila_com_um_pedido_de_entrega.pedidos_na_fila_de_entrega == 0

def test_remover_pedido_na_fila_vazia_de_entrega(lanche_fila_vazia_de_entrega):
    lanche_fila_vazia_de_entrega.remove_pedido_entrega()
    assert lanche_fila_vazia_de_entrega.pedidos_na_fila_de_entrega == 0