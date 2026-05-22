class Procedimento:
  def __init__(self, descricao_procedimento: str, custo: float):
    self._descricao_procedimento = descricao_procedimento
    self._custo = custo

  @property
  def descricao_procedimento(self) -> str:
    return self._descricao_procedimento
  @descricao_procedimento.setter
  def descricao_procedimento(self, descricao_procedimento: str):
    self._descricao_procedimento = descricao_procedimento

  @property
  def custo(self) -> float:
    return self._custo
  @custo.setter
  def custo(self, custo: float):
    self._custo = custo