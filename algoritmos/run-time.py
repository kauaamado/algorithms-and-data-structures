# Uma maneira de avaliar um algoritmo
# é pelo seu tempo de execução (run time)

import time

start = time.time()
for i in range(1, 6):
    print(i)

end = time.time()

# O run time varia de acordo com o poder
# de processamento e a linguagem de programação

print(f"{(end - start):.10f}")