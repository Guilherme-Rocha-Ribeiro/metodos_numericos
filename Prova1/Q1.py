def func(x: float) -> float:
  y = 5*x**3 - 12*x**2 + 7*x - 1
  return float(y)

def func_derivada(x: float) -> float:
    y = 15*x**2 - 24*x + 7
    return float(y)

def bissection(a: float, b: float, tolerance = 10**-4):
  i = 0
  if func(a) * func(b) > 0:
    x = func(a)
    y = func(b)
    return  "Não ocorre mudança de sinal entre a e b", [float(x), float(y)]
  else:
    while True:
      mid_pnt = (a+b)/2
      if abs(func(mid_pnt)) <= tolerance:
        return mid_pnt, i
      
      i += 1
      if func(mid_pnt) * func(a) < 0:
        b = mid_pnt
      else:
        a = mid_pnt
     

def metodo_newton_raphson(guess: float, iteracoes: int = 100, tolerance = 0.001) -> float:
    
    x = guess
    for i in range(iteracoes):
        fx = func(x)
        dfx = func_derivada(x)

        # Verifica se a |f(x)| já é proximo de zero
        if abs(fx) <= tolerance:
            # print(f"Raiz encontrada: {x:.4f} em {i} iterações")
            return x, i

        # Verifica se a derivada é zero
        if dfx == 0:
            raise ValueError("Derivada(x) = zero encontrada")

        x_novo = x - fx / dfx

        if abs(x_novo - x) < tolerance:
            print(f"Convergência {x:.4f} alcançada após {i+1} iterações.")
            return x_novo, i
        
        x = x_novo

    print(f"Raiz não encontrada após {iteracoes} iterações.")
    return None

if __name__ == '__main__':
  zero_funcao, interacoes = bissection(0, 2)
  resultado_newton, interacoes2 = metodo_newton_raphson(2)
  print(f'Bissecao = {zero_funcao:.4f} em {interacoes} interacoes')
  print(f"Newton-raphson = {resultado_newton:.4f} em {interacoes2} interacoes" )
 


""""
Aluno: Guilherme Rocha
Referencias: https://uenf.br/cct/leciv/files/2016/02/Alexandre-Magno-Alves-de-Oliveira-e-Rodrigo-Moulin-Ribeiro-Pierrot.pdf


--- Analise do metodo de bisseção ---
Alterando a precisão para 10**-4 como solicitado, o resultado é x ~ 1.6057 com 4 casas decimais. 

Como o método da bisseção precisa de um intervalo bem definido para ser executado, o qual exista uma mudança de sinal, para que converja para a raiz. 
Alem disso,  o metodo da bisseção demora mais para convergir, pois ele vai dividindo e escolhendo os intervalos a direita ou a esquerda do mid_point a 
cada iteração. Como comparação, o método de Newton-Raphson convergiu em 3 iteração, com um chute inicial proximo do intervalo, enquanto o método da bisseção convergiu em 14 iterações.

"""