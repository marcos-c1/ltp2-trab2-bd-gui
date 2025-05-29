from utils.main import validaCPF, validaCNPJ

class Cliente():
    def __init__(self, nome: str, isEmpresa: bool, registro: str, cep: str, uf: str):
        if(len(nome) == 0):
            raise Exception("Nome do cliente não definido")
        if(len(cep) == 0):
            raise Exception("CEP não definido")
        
        if(len(uf) > 2):
            raise Exception("UF não encontrada")
        if(isEmpresa):
            if(validaCNPJ(registro)):
                self.registro = registro
            else:
                raise Exception("CNPJ não é válido")
        else:
            if(validaCPF(registro)):
                self.registro = registro
            else:
                raise Exception("CPF não é válido")
        self.nome = nome 
        self.isEmpresa = isEmpresa            
        self.cep = cep
        self.uf = uf
