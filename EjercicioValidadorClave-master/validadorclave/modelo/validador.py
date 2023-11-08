from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoTieneNumeroError, NoCumpleLongitudMinimaError, NoTieneCaracterEspecialError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,NoTienePalabraSecretaError
class ReglaValidador(ABC):

    def __init__(self,_longitud_esperada:int):
        self._longitud_esperada:int = _longitud_esperada

    @abstractmethod
    def es_valida(self):
        pass

    def  _validar_longitud(self,clave:str):
        self._longiud_clave:list=[]
        for i in clave:
            self._longiud_clave.append(i)
        if len(self._longiud_clave) > self._longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self,clave:str)->bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minisula(self,clave:str)->bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False
    def _contiene_numeros(self,clave:str)->bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

class Validador:

    def __init__(self,regla:ReglaValidador):
        self.regla_validacion:ReglaValidador=regla

    def es_valida(self,clave:str)->bool:
        return self.regla_validacion.es_valida(clave)

class ReglavalidacionGanimedes(ReglaValidador):
    carecteres_especiales:list[str]=[ "@", "_" ,"#" ,"$" ,"%"]
    longitud_esperada:int=8
    def __init__(self) -> None:
        super().__init__(self.longitud_esperada)

    def contiene_caracter_especial(self, clave:str)->str:
        for caracter in clave:
            if caracter in self.carecteres_especiales:
                return True
        return False
    
    def es_valida(self,clave:str)->bool:
        if self._contiene_mayuscula(clave):
            if self._contiene_minisula(clave):
                if self._contiene_numeros(clave):
                    if self.contiene_caracter_especial(clave):
                        if self._validar_longitud(clave):
                            return True
                        else:
                            raise NoCumpleLongitudMinimaError()
                    else:
                        raise NoTieneCaracterEspecialError()
                else:
                    raise NoTieneNumeroError
            else:
                raise NoTieneLetraMinusculaError()
        else:
            raise NoTieneLetraMayusculaError()
        
    

class ReglavalidacionCalisto(ReglaValidador):
    longitud_esperada:int=6

    def __init__(self) -> None:
        super().__init__(self.longitud_esperada)


    def contiene_calisto(self, clave:str)->str:
        clave_minusculas = clave.lower()
        
        indice = clave_minusculas.find("calisto")
        
        if indice != -1:
            mayusculas_en_calisto = sum(1 for letra in clave[indice:indice+7] if letra.isupper())
            if mayusculas_en_calisto >= 2 and mayusculas_en_calisto < 7:
                return True
        
        return False
    

    def es_valida(self,clave:str)->bool:
            if self.contiene_calisto(clave):
                if self._contiene_numeros(clave):
                    if self._validar_longitud(clave):
                        return True
                    else:
                        raise NoCumpleLongitudMinimaError()
                else:
                    raise NoTieneNumeroError()
            else:
                raise NoTienePalabraSecretaError()
            