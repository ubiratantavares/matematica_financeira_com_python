import numpy as np
import numpy_financial as npf

class Simples:      
     
    def juros(self, capital, taxa, periodo):
        return capital * taxa * periodo;

    def montante(self, capital, taxa, periodo):
        return capital + self.juros(capital, taxa, periodo)

    def taxa_pelo_juros(self, juros, capital, periodo):
        return (juros/(capital * periodo))
    
    def taxa_pelo_montante(self, montante, capital, periodo):
        return (montante / capital - 1) / periodo
    
    def taxa_equivalente(self, taxa1, periodo1, periodo2):
        return (taxa1 * periodo1) / periodo2
    
    def periodo_pelo_juros(self, juros, capital, taxa):
        return juros/(capital*taxa)
    
    def periodo_pelo_montante(self, montante, capital, taxa):
        return (montante / capital - 1) / taxa 

    def capital_pelo_juros(self, juros, taxa, periodo):
        return juros/(taxa * periodo)

    def capital_pelo_montante(self, montante, taxa, periodo):
        return montante/(1 + taxa * periodo)


class Composto:    
    
    def juros(self, capital, taxa, periodo):
        return capital * ((taxa + 1)**periodo - 1)
    
    def montante(self, capital, taxa, periodo):
        return capital + self.juros(capital, taxa, periodo)
    
    def montante_para_taxas_acumuladas(self, capital, taxas):
        produto = 1.0
        for taxa in taxas:
            produto *= (1 + taxa)
        return capital * produto
    
    def taxa_pelo_juros(self, juros, capital, periodo):
        return (1 + juros/capital)**(1/periodo) - 1   
    
    def taxa_pelo_montante(self, montante, capital, periodo):
        return (montante/capital)**(1/periodo) - 1
    
    def taxa_equivalente(self, taxa1, periodo1, periodo2):
        return ((taxa1 + 1)**(periodo1/periodo2) - 1)

    def periodo_pelo_juros(self, juros, capital, taxa):
        return round((np.log(1 + juros/capital) / np.log(1 + taxa)))
    
    def periodo_pelo_montante(self, montante, capital, taxa):
        return round(np.log(montante/capital) / np.log(1 + taxa))
    
    def capital_pelo_juros(self, juros, taxa, periodo):
        return juros / ((1 + taxa)**periodo - 1)
    
    def capital_pelo_montante(self, montante, taxa, periodo):
        return montante/(1 + taxa)**periodo
    
class TaxasDeMercado:
    
    from capitalizacao import Composto   
    
    # calculando o %DI
    def percentual_DI_ano(self, taxa_anual, percentual_di):        
        c = Composto()
        
        # DI em base % a.a
        periodo_anual = 1
        periodo_dias_uteis = 252
        
        # taxas equivalentes: DI em base % ao dia (ad)
        taxa_dias_uteis = c.taxa_equivalente(taxa_anual, periodo_anual, periodo_dias_uteis)
               
        
        # aplicação de percentual: taxa base % ao dia
        taxa_dia = percentual_di * taxa_dias_uteis # a.d
        
        
        # taxas equivalentes: taxa base % ao ano
        taxa_anual = c.taxa_equivalente(taxa_dia, periodo_dias_uteis, periodo_anual)
        return taxa_anual # a.a
    
    # calculando o %DI
    def percentual_DI_dia(self, taxa_anual, percentual_di):        
        c = Composto()
        
        # DI em base % a.a
        periodo_anual = 1
        periodo_dias_uteis = 252
        
        # taxas equivalentes: DI em base % ao dia (ad)
        taxa_dias_uteis = c.taxa_equivalente(taxa_anual, 
                                             periodo_anual, 
                                             periodo_dias_uteis)               
        
        # aplicação de percentual: taxa base % ao dia
        taxa_dia = percentual_di * taxa_dias_uteis # a.d

        return taxa_dia


class Indicadores:
    
    def valor_presente_liquido(self, cf, k):
        soma = 0.0
        # k: custo de oportunidade do projeto
        # cf: valor líquido de entradas e saídas no tempo n
        for i in range(0, len(cf)):
            soma += (cf[i]) / ((1 + k)**i)
        return soma
    
    def valor_futuro_liquido(self, cf, k, periodo):
        soma = 0.0
        # k: custo de oportunidade do projeto
        # cf: valor líquido de entradas e saídas no tempo n
        for i in range(0, len(cf)):
            soma += (cf[i] * (1 + k)**(periodo - i))
        return soma
    
    def taxa_interna_de_retorno(self, cf):
        return npf.irr(cf)
    
    def indice_de_rentabilidade(self, cf, k):
        soma = 0.0
        # k: custo de oportunidade do projeto
        # cf: valor líquido de entradas e saídas no tempo n
        for i in range(1, len(cf)):
            soma += (cf[i]) / ((1 + k)**i)
        return soma / (np.abs(cf[0]))
    
    def payback(self, cf):
        ganhos = 0.0
        investimentos = 0.0
        for i in range(0, len(cf)):
            if (cf[i] > 0):
                ganhos += cf[i]
            else:
                investimentos += np.abs(cf[i])
            
            if ganhos >= investimentos:
                return i          
    
    def retorno_sobre_investimento(self, cf):
        ganhos = 0.0
        investimentos = 0.0
        for i in range(0, len(cf)):
            if (cf[i] > 0):
                ganhos += cf[i]
            else:
                investimentos += np.abs(cf[i])
        return (ganhos - investimentos) / investimentos      
            