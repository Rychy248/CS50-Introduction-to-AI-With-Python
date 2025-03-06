from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowledge = And(  #conomiento
    Implication(Not(rain), hagrid),  
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))
print(knowledge.formula())  #mostrar informción de la oración basada en logica
